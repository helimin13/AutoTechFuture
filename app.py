import os
import sys
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from datetime import datetime
import markdown
from werkzeug.utils import secure_filename

# Add current directory to Python path for Windows
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.config.from_object('config.Config')

# Initialize extensions
from extensions import db, bcrypt, login_manager
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

# Import models
from models import User, BlogPost, Category, FutureTech, Comment, Like

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import AI generator
from ai_content import AIContentGenerator
ai_gen = AIContentGenerator()

# Helper functions
def generate_slug(title):
    """Create URL-friendly slug"""
    slug = title.lower().strip()
    slug = slug.replace(' ', '-')
    slug = slug.replace('--', '-')
    # Remove special characters (Windows safe)
    import re
    slug = re.sub(r'[^a-z0-9\-]', '', slug)
    return slug

def save_upload(file):
    """Save uploaded file on Windows"""
    if file and file.filename:
        # Secure filename for Windows
        filename = secure_filename(file.filename)
        # Add timestamp for uniqueness
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_name = f"{timestamp}_{filename}"
        
        # Ensure upload directory exists
        upload_dir = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        # Save file
        file_path = os.path.join(upload_dir, unique_name)
        file.save(file_path)
        
        # Return relative URL
        return f"/static/uploads/{unique_name}"
    return None

# ============ ROUTES ============
@app.route('/')
def index():
    """Home page"""
    try:
        featured = BlogPost.query.filter_by(is_featured=True)\
            .order_by(BlogPost.created_at.desc())\
            .limit(3).all()
        
        future_tech = FutureTech.query.order_by(FutureTech.created_at.desc())\
            .limit(3).all()
        
        categories = Category.query.all()
        
        # Sample data if no posts exist
        if not featured:
            featured = []
        
        return render_template('index.html',
                             posts=featured,
                             future_tech=future_tech,
                             categories=categories)
    except Exception as e:
        print(f"Error loading index: {e}")
        return render_template('index.html', posts=[], future_tech=[], categories=[])

@app.route('/blog')
def blog():
    """Blog listing"""
    page = request.args.get('page', 1, type=int)
    cat_id = request.args.get('category', type=int)
    
    query = BlogPost.query
    
    if cat_id:
        query = query.filter_by(category_id=cat_id)
    
    posts = query.order_by(BlogPost.created_at.desc())\
        .paginate(page=page, per_page=6, error_out=False)
    
    categories = Category.query.all()
    
    return render_template('blog.html',
                         posts=posts,
                         categories=categories,
                         current_category=cat_id)

@app.route('/blog/<slug>')
def blog_detail(slug):
    """Blog post detail"""
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    post.views += 1
    db.session.commit()
    
    # Convert markdown to HTML
    post.content_html = markdown.markdown(post.content)
    
    # Get related posts
    related = BlogPost.query\
        .filter(BlogPost.category_id == post.category_id, BlogPost.id != post.id)\
        .order_by(BlogPost.created_at.desc())\
        .limit(3).all()
    
    return render_template('blog_detail.html',
                         post=post,
                         related_posts=related)

@app.route('/future-tech')
def future_tech():
    """Future technology showcase"""
    tech = FutureTech.query.order_by(FutureTech.created_at.desc()).all()
    return render_template('future_tech.html', technologies=tech)

@app.route('/create-post', methods=['GET', 'POST'])
@login_required
def create_post():
    """Create new post"""
    if request.method == 'POST':
        try:
            title = request.form.get('title', '').strip()
            content = request.form.get('content', '').strip()
            category_id = request.form.get('category', type=int)
            tags = request.form.get('tags', '').strip()
            is_featured = 'is_featured' in request.form
            
            # Validation
            if not title or not content or not category_id:
                flash('Please fill all required fields', 'error')
                return redirect(url_for('create_post'))
            
            # Generate slug
            slug = generate_slug(title)
            
            # Check for duplicate slug
            if BlogPost.query.filter_by(slug=slug).first():
                slug = f"{slug}-{datetime.now().strftime('%Y%m%d')}"
            
            # Handle image upload
            image_url = '/static/images/default-blog.jpg'
            if 'image' in request.files:
                image_file = request.files['image']
                if image_file.filename:
                    saved = save_upload(image_file)
                    if saved:
                        image_url = saved
            
            # Create post
            post = BlogPost(
                title=title,
                content=content,
                slug=slug,
                author_id=current_user.id,
                category_id=category_id,
                tags=tags,
                image_url=image_url,
                is_featured=is_featured,
                excerpt=content[:150] + '...' if len(content) > 150 else content
            )
            
            db.session.add(post)
            db.session.commit()
            
            flash('Post created successfully!', 'success')
            return redirect(url_for('blog_detail', slug=slug))
            
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating post: {str(e)}', 'error')
            return redirect(url_for('create_post'))
    
    # GET request - show form
    categories = Category.query.all()
    return render_template('create_post.html', categories=categories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')
        
        # Basic validation
        errors = []
        if len(username) < 3:
            errors.append('Username must be at least 3 characters')
        if '@' not in email:
            errors.append('Invalid email address')
        if len(password) < 6:
            errors.append('Password must be at least 6 characters')
        if password != confirm:
            errors.append('Passwords do not match')
        
        # Check existing
        if User.query.filter_by(username=username).first():
            errors.append('Username already exists')
        if User.query.filter_by(email=email).first():
            errors.append('Email already registered')
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return redirect(url_for('register'))
        
        # Create user
        hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(
            username=username,
            email=email,
            password_hash=hashed
        )
        
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = 'remember' in request.form
        
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            flash('Login successful!', 'success')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.route('/ai-generate', methods=['POST'])
@login_required
def ai_generate():
    """AI content generation"""
    if not current_user.is_admin:
        return jsonify({'error': 'Admin access required'}), 403
    
    try:
        data = request.get_json()
        topic = data.get('topic', '').strip()
        content_type = data.get('type', 'blog_post')
        
        if not topic:
            return jsonify({'error': 'Topic required'}), 400
        
        content = ai_gen.generate_content(topic, content_type)
        return jsonify(content)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/3d-visualization')
def visualization_3d():
    """3D visualization page"""
    return render_template('3d_visualization.html')

# API Endpoints
@app.route('/api/trending')
def api_trending():
    posts = BlogPost.query.order_by(BlogPost.views.desc()).limit(5).all()
    data = [{
        'id': p.id,
        'title': p.title,
        'slug': p.slug,
        'views': p.views,
        'author': p.author.username,
        'created_at': p.created_at.strftime('%Y-%m-%d')
    } for p in posts]
    return jsonify(data)

@app.route('/api/stats')
def api_stats():
    stats = {
        'posts': BlogPost.query.count(),
        'users': User.query.count(),
        'categories': Category.query.count(),
        'tech': FutureTech.query.count()
    }
    return jsonify(stats)

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# Context processor
@app.context_processor
def inject_data():
    categories = Category.query.all()
    return dict(categories=categories)

# Create tables on startup
# Create tables on startup
with app.app_context():
    # Ensure database directory exists (Critical for PythonAnywhere)
    try:
        db_uri = app.config['SQLALCHEMY_DATABASE_URI']
        if db_uri.startswith('sqlite:///'):
            db_path = db_uri.replace('sqlite:///', '')
            db_dir = os.path.dirname(db_path)
            if db_dir and not os.path.exists(db_dir):
                print(f"Creating database directory: {db_dir}")
                os.makedirs(db_dir)
            print(f"Database path: {db_path}")
    except Exception as e:
        print(f"Error checking database path: {e}")

    db.create_all()

if __name__ == '__main__':
    print("\n" + "="*50)
    print("AutoTech Future - Automotive Engineering Blog")
    print("="*50)
    print(f"Access URL: http://localhost:5000")
    print(f"Admin login: admin / admin123")
    print("="*50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
