from app import app, db
from models import User, Category, FutureTech
from werkzeug.security import generate_password_hash
import os

def setup_database():
    """Initialize the database with default data"""
    with app.app_context():
        # Create tables
        print("Creating database tables...")
        db.create_all()
        
        # Create admin user
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                email='admin@autotechfuture.com',
                password_hash=generate_password_hash('admin123'),
                is_admin=True,
                bio='System Administrator - AutoTech Future',
                avatar_url='/static/images/admin-avatar.png'
            )
            db.session.add(admin)
            print("Created admin user: admin / admin123")
        
        # Create default categories
        categories = [
            ('Electric Vehicles', 'EV technology and battery innovations', 'fas fa-bolt'),
            ('Autonomous Driving', 'Self-driving cars and ADAS systems', 'fas fa-robot'),
            ('Sustainable Tech', 'Green automotive solutions', 'fas fa-leaf'),
            ('AI & Machine Learning', 'AI applications in automotive', 'fas fa-brain'),
            ('Materials Science', 'Advanced materials and manufacturing', 'fas fa-cogs'),
            ('Future Concepts', 'Concept vehicles and futuristic designs', 'fas fa-rocket'),
            ('Industry News', 'Latest automotive industry updates', 'fas fa-newspaper'),
            ('Technical Guides', 'In-depth engineering tutorials', 'fas fa-book')
        ]
        
        for name, description, icon in categories:
            if not Category.query.filter_by(name=name).first():
                category = Category(name=name, description=description, icon=icon)
                db.session.add(category)
        
        # Create sample future tech
        sample_tech = [
            {
                'title': 'Solid-State Battery Revolution',
                'description': 'Next-generation batteries offering 2x energy density, faster charging, and improved safety over traditional lithium-ion batteries.',
                'category': 'Electric Vehicles',
                'timeline': '2024-2026',
                'impact_level': 5,
                'status': 'Prototype'
            },
            {
                'title': 'Level 5 Full Autonomy',
                'description': 'Completely autonomous vehicles capable of operating in all conditions without human intervention.',
                'category': 'Autonomous Driving',
                'timeline': '2030+',
                'impact_level': 5,
                'status': 'Research'
            },
            {
                'title': 'Wireless EV Charging Roads',
                'description': 'Dynamic wireless charging infrastructure embedded in roads for continuous EV charging while driving.',
                'category': 'Electric Vehicles',
                'timeline': '2027-2029',
                'impact_level': 4,
                'status': 'Testing'
            }
        ]
        
        for tech in sample_tech:
            if not FutureTech.query.filter_by(title=tech['title']).first():
                future_tech = FutureTech(**tech)
                db.session.add(future_tech)
        
        db.session.commit()
        print("Database setup complete!")
        print("\nDefault Categories Created:")
        for cat in Category.query.all():
            print(f"  - {cat.name}")
        
        print("\nAccess the application at: http://localhost:5000")
        print("Admin login: admin / admin123")

if __name__ == '__main__':
    setup_database()