# create_templates.py
import os

# Create login.html
login_html = """{% extends "base.html" %}

{% block title %}Login - AutoTech Future{% endblock %}

{% block content %}
<div class="max-w-md mx-auto py-12 px-4">
    <div class="bg-white rounded-xl shadow-lg p-8">
        <h1 class="text-2xl font-bold mb-6 text-center">Login to AutoTech Future</h1>
        
        <form method="POST" action="{{ url_for('login') }}">
            <div class="mb-4">
                <label class="block text-gray-700 mb-2">Username</label>
                <input type="text" 
                       name="username" 
                       required
                       class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div class="mb-6">
                <label class="block text-gray-700 mb-2">Password</label>
                <input type="password" 
                       name="password" 
                       required
                       class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div class="flex items-center mb-6">
                <input type="checkbox" 
                       name="remember" 
                       id="remember"
                       class="mr-2">
                <label for="remember" class="text-gray-700">Remember me</label>
            </div>
            
            <button type="submit" 
                    class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 font-medium transition duration-300">
                Login
            </button>
        </form>
        
        <div class="mt-6 text-center">
            <p class="text-gray-600">Don't have an account?</p>
            <a href="{{ url_for('register') }}" 
               class="text-blue-600 hover:text-blue-800 font-medium">
                Register here
            </a>
        </div>
    </div>
</div>
{% endblock %}"""

# Create register.html
register_html = """{% extends "base.html" %}

{% block title %}Register - AutoTech Future{% endblock %}

{% block content %}
<div class="max-w-md mx-auto py-12 px-4">
    <div class="bg-white rounded-xl shadow-lg p-8">
        <h1 class="text-2xl font-bold mb-6 text-center">Create Account</h1>
        
        <form method="POST" action="{{ url_for('register') }}">
            <div class="mb-4">
                <label class="block text-gray-700 mb-2">Username</label>
                <input type="text" 
                       name="username" 
                       required
                       class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div class="mb-4">
                <label class="block text-gray-700 mb-2">Email</label>
                <input type="email" 
                       name="email" 
                       required
                       class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div class="mb-4">
                <label class="block text-gray-700 mb-2">Password</label>
                <input type="password" 
                       name="password" 
                       required
                       class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <div class="mb-6">
                <label class="block text-gray-700 mb-2">Confirm Password</label>
                <input type="password" 
                       name="confirm_password" 
                       required
                       class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <button type="submit" 
                    class="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 font-medium transition duration-300">
                Register
            </button>
        </form>
        
        <div class="mt-6 text-center">
            <p class="text-gray-600">Already have an account?</p>
            <a href="{{ url_for('login') }}" 
               class="text-blue-600 hover:text-blue-800 font-medium">
                Login here
            </a>
        </div>
    </div>
</div>
{% endblock %}"""

# Create blog.html
blog_html = """{% extends "base.html" %}

{% block title %}Blog - AutoTech Future{% endblock %}

{% block content %}
<div class="max-w-7xl mx-auto px-4 py-8">
    <!-- Page Header -->
    <div class="mb-12 text-center">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">Automotive Engineering Blog</h1>
        <p class="text-xl text-gray-600">Latest insights, innovations, and technical discussions</p>
    </div>
    
    <div class="flex flex-col lg:flex-row gap-8">
        <!-- Main Content -->
        <div class="lg:w-2/3">
            <!-- Category Filter -->
            <div class="mb-8 flex flex-wrap gap-2">
                <a href="{{ url_for('blog') }}" 
                   class="px-4 py-2 rounded-lg {% if not current_category %}bg-blue-600 text-white{% else %}bg-gray-200 text-gray-700 hover:bg-gray-300{% endif %}">
                    All Categories
                </a>
                {% for category in categories %}
                <a href="{{ url_for('blog') }}?category={{ category.id }}" 
                   class="px-4 py-2 rounded-lg {% if current_category == category.id %}bg-blue-600 text-white{% else %}bg-gray-200 text-gray-700 hover:bg-gray-300{% endif %}">
                    <i class="{{ category.icon }} mr-2"></i>{{ category.name }}
                </a>
                {% endfor %}
            </div>
            
            <!-- Blog Posts -->
            {% if posts.items %}
            <div class="space-y-8">
                {% for post in posts.items %}
                <article class="bg-white rounded-xl shadow-md overflow-hidden card-hover">
                    <div class="md:flex">
                        <div class="md:w-1/3">
                            <img src="{{ post.image_url }}" 
                                 alt="{{ post.title }}"
                                 class="w-full h-64 md:h-full object-cover">
                        </div>
                        <div class="md:w-2/3 p-6">
                            <div class="flex items-center justify-between mb-3">
                                <span class="bg-blue-100 text-blue-600 px-3 py-1 rounded-full text-sm font-medium">
                                    {{ post.category.name }}
                                </span>
                                <span class="text-gray-500 text-sm">
                                    {{ post.created_at.strftime('%b %d, %Y') }}
                                </span>
                            </div>
                            
                            <h2 class="text-2xl font-bold mb-3">
                                <a href="{{ url_for('blog_detail', slug=post.slug) }}" 
                                   class="text-gray-900 hover:text-blue-600">
                                    {{ post.title }}
                                </a>
                            </h2>
                            
                            <p class="text-gray-600 mb-4">
                                {{ post.excerpt|default(post.content[:200] + '...' if post.content|length > 200 else post.content) }}
                            </p>
                            
                            <div class="flex items-center justify-between">
                                <div class="flex items-center">
                                    <img src="{{ post.author.avatar_url }}" 
                                         class="w-8 h-8 rounded-full mr-2">
                                    <span class="text-gray-700">{{ post.author.username }}</span>
                                </div>
                                <div class="flex items-center space-x-4">
                                    <span class="text-gray-500">
                                        <i class="far fa-eye mr-1"></i>{{ post.views }}
                                    </span>
                                    <a href="{{ url_for('blog_detail', slug=post.slug) }}" 
                                       class="text-blue-600 hover:text-blue-800 font-medium">
                                        Read More <i class="fas fa-arrow-right ml-1"></i>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </article>
                {% endfor %}
            </div>
            
            <!-- Pagination -->
            {% if posts.pages > 1 %}
            <div class="mt-12 flex justify-center">
                <nav class="flex items-center space-x-2">
                    {% if posts.has_prev %}
                    <a href="{{ url_for('blog', page=posts.prev_num, category=current_category) }}" 
                       class="px-4 py-2 rounded-lg bg-gray-200 text-gray-700 hover:bg-gray-300">
                        <i class="fas fa-chevron-left"></i>
                    </a>
                    {% endif %}
                    
                    {% for page_num in posts.iter_pages(left_edge=2, right_edge=2, left_current=2, right_current=2) %}
                        {% if page_num %}
                            {% if page_num == posts.page %}
                            <span class="px-4 py-2 rounded-lg bg-blue-600 text-white">{{ page_num }}</span>
                            {% else %}
                            <a href="{{ url_for('blog', page=page_num, category=current_category) }}" 
                               class="px-4 py-2 rounded-lg bg-gray-200 text-gray-700 hover:bg-gray-300">
                                {{ page_num }}
                            </a>
                            {% endif %}
                        {% else %}
                            <span class="px-2">...</span>
                        {% endif %}
                    {% endfor %}
                    
                    {% if posts.has_next %}
                    <a href="{{ url_for('blog', page=posts.next_num, category=current_category) }}" 
                       class="px-4 py-2 rounded-lg bg-gray-200 text-gray-700 hover:bg-gray-300">
                        <i class="fas fa-chevron-right"></i>
                    </a>
                    {% endif %}
                </nav>
            </div>
            {% endif %}
            
            {% else %}
            <div class="text-center py-16 bg-white rounded-xl shadow">
                <i class="fas fa-newspaper text-5xl text-gray-300 mb-4"></i>
                <h3 class="text-xl font-bold text-gray-700 mb-2">No Posts Yet</h3>
                <p class="text-gray-600 mb-4">Be the first to create amazing content!</p>
                {% if current_user.is_authenticated %}
                <a href="{{ url_for('create_post') }}" 
                   class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 inline-flex items-center">
                    <i class="fas fa-plus mr-2"></i> Create First Post
                </a>
                {% endif %}
            </div>
            {% endif %}
        </div>
        
        <!-- Sidebar -->
        <div class="lg:w-1/3">
            <!-- AI Assistant Card -->
            {% if current_user.is_authenticated %}
            <div class="bg-gradient-to-r from-blue-500 to-purple-600 rounded-xl p-6 text-white mb-8">
                <h3 class="text-xl font-bold mb-4">
                    <i class="fas fa-robot mr-2"></i>AI Content Assistant
                </h3>
                <p class="mb-4 opacity-90">
                    Need inspiration? Let AI help you create compelling automotive content.
                </p>
                <a href="{{ url_for('create_post') }}" 
                   class="block text-center bg-white text-blue-600 py-2 rounded-lg font-medium hover:bg-gray-100">
                    Try AI Assistant
                </a>
            </div>
            {% endif %}
            
            <!-- Categories -->
            <div class="bg-white rounded-xl shadow-md p-6 mb-8">
                <h3 class="text-xl font-bold mb-4">Categories</h3>
                <ul class="space-y-2">
                    {% for category in categories %}
                    <li>
                        <a href="{{ url_for('blog') }}?category={{ category.id }}" 
                           class="flex items-center justify-between p-3 rounded-lg hover:bg-gray-50">
                            <span class="flex items-center">
                                <i class="{{ category.icon }} mr-3 text-blue-600"></i>
                                {{ category.name }}
                            </span>
                            <span class="bg-gray-100 text-gray-600 px-2 py-1 rounded-full text-sm">
                                {{ category.posts|length }}
                            </span>
                        </a>
                    </li>
                    {% endfor %}
                </ul>
            </div>
            
            <!-- Trending Posts -->
            <div class="bg-white rounded-xl shadow-md p-6">
                <h3 class="text-xl font-bold mb-4">Trending Now</h3>
                <div id="trendingPosts" class="space-y-4">
                    <!-- Will be populated by JavaScript -->
                    <div class="text-center py-4">
                        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto"></div>
                        <p class="text-gray-500 mt-2">Loading trending posts...</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// Load trending posts
async function loadTrendingPosts() {
    try {
        const response = await fetch('/api/trending');
        if (response.ok) {
            const posts = await response.json();
            const container = document.getElementById('trendingPosts');
            
            if (posts.length > 0) {
                let html = '';
                posts.forEach(post => {
                    html += `
                    <div class="flex items-start space-x-3 p-2 hover:bg-gray-50 rounded-lg">
                        <div class="flex-shrink-0">
                            <div class="w-12 h-12 bg-gray-200 rounded-lg overflow-hidden">
                                <img src="${post.image_url}" alt="${post.title}" class="w-full h-full object-cover">
                            </div>
                        </div>
                        <div>
                            <a href="/blog/${post.slug}" class="font-medium text-gray-900 hover:text-blue-600 line-clamp-2">
                                ${post.title}
                            </a>
                            <div class="text-sm text-gray-500 mt-1">
                                ${post.author} • ${post.created_at}
                            </div>
                        </div>
                    </div>
                    `;
                });
                container.innerHTML = html;
            } else {
                container.innerHTML = '<p class="text-gray-500 text-center py-4">No trending posts yet</p>';
            }
        }
    } catch (error) {
        console.error('Error loading trending posts:', error);
    }
}

// Initialize
document.addEventListener('DOMContentLoaded', loadTrendingPosts);
</script>
{% endblock %}"""

# Save all templates
templates = {
    'login.html': login_html,
    'register.html': register_html,
    'blog.html': blog_html,
    'create_post.html': '''
{% extends "base.html" %}

{% block title %}Create Post - AutoTech Future{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto py-8 px-4">
    <h1 class="text-3xl font-bold mb-8">Create New Blog Post</h1>
    
    <div class="bg-white rounded-xl shadow-lg p-8">
        <form method="POST" action="{{ url_for('create_post') }}" enctype="multipart/form-data">
            <!-- Title -->
            <div class="mb-6">
                <label class="block text-gray-700 mb-2 font-medium">Title *</label>
                <input type="text" 
                       name="title" 
                       required
                       placeholder="Enter your post title"
                       class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            
            <!-- Category -->
            <div class="mb-6">
                <label class="block text-gray-700 mb-2 font-medium">Category *</label>
                <select name="category" 
                        required
                        class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
                    <option value="">Select a category</option>
                    {% for category in categories %}
                    <option value="{{ category.id }}">{{ category.name }}</option>
                    {% endfor %}
                </select>
            </div>
            
            <!-- Featured Image -->
            <div class="mb-6">
                <label class="block text-gray-700 mb-2 font-medium">Featured Image</label>
                <div class="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center hover:border-blue-500 transition duration-300">
                    <input type="file" 
                           name="image" 
                           id="imageInput"
                           accept="image/*"
                           class="hidden">
                    <label for="imageInput" class="cursor-pointer">
                        <i class="fas fa-cloud-upload-alt text-4xl text-gray-400 mb-2"></i>
                        <p class="text-gray-600">Click to upload an image</p>
                        <p class="text-sm text-gray-500 mt-1">Recommended: 1200x630 pixels</p>
                    </label>
                    <div id="imagePreview" class="mt-4 hidden">
                        <img id="previewImage" class="max-h-48 mx-auto rounded-lg">
                    </div>
                </div>
            </div>
            
            <!-- Content -->
            <div class="mb-6">
                <label class="block text-gray-700 mb-2 font-medium">Content *</label>
                <textarea name="content" 
                          required
                          rows="15"
                          placeholder="Write your post content here... (Markdown supported)"
                          class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono"></textarea>
                <p class="text-sm text-gray-500 mt-2">
                    <i class="fas fa-info-circle mr-1"></i> 
                    You can use Markdown for formatting. Need help? 
                    <a href="https://www.markdownguide.org/basic-syntax/" target="_blank" class="text-blue-600 hover:underline">
                        View Markdown Guide
                    </a>
                </p>
            </div>
            
            <!-- Tags -->
            <div class="mb-6">
                <label class="block text-gray-700 mb-2 font-medium">Tags</label>
                <input type="text" 
                       name="tags" 
                       placeholder="e.g., electric vehicles, battery technology, innovation"
                       class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
                <p class="text-sm text-gray-500 mt-2">
                    Separate tags with commas
                </p>
            </div>
            
            <!-- Featured Post -->
            <div class="mb-8">
                <label class="flex items-center">
                    <input type="checkbox" 
                           name="is_featured"
                           class="mr-2">
                    <span class="text-gray-700">Feature this post on homepage</span>
                </label>
            </div>
            
            <!-- Submit -->
            <div class="flex gap-4">
                <button type="submit" 
                        class="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 font-medium transition duration-300">
                    <i class="fas fa-paper-plane mr-2"></i> Publish Post
                </button>
                <a href="{{ url_for('blog') }}" 
                   class="bg-gray-200 text-gray-700 px-8 py-3 rounded-lg hover:bg-gray-300 font-medium transition duration-300">
                    Cancel
                </a>
            </div>
        </form>
    </div>
</div>

<script>
// Image preview
document.getElementById('imageInput').addEventListener('change', function(e) {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.getElementById('previewImage');
            preview.src = e.target.result;
            document.getElementById('imagePreview').classList.remove('hidden');
        }
        reader.readAsDataURL(file);
    }
});
</script>
{% endblock %}
''',
    'blog_detail.html': '''
{% extends "base.html" %}

{% block title %}{{ post.title }} - AutoTech Future{% endblock %}

{% block content %}
<div class="max-w-4xl mx-auto px-4 py-8">
    <!-- Back Button -->
    <a href="{{ url_for('blog') }}" 
       class="inline-flex items-center text-blue-600 hover:text-blue-800 mb-8">
        <i class="fas fa-arrow-left mr-2"></i> Back to Blog
    </a>
    
    <!-- Article -->
    <article class="bg-white rounded-xl shadow-lg overflow-hidden">
        <!-- Featured Image -->
        <div class="relative h-96">
            <img src="{{ post.image_url }}" 
                 alt="{{ post.title }}"
                 class="w-full h-full object-cover">
            <div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black/70 to-transparent p-6">
                <div class="max-w-4xl mx-auto">
                    <span class="bg-blue-600 text-white px-4 py-1 rounded-full text-sm inline-block mb-3">
                        {{ post.category.name }}
                    </span>
                    <h1 class="text-3xl md:text-4xl font-bold text-white mb-2">{{ post.title }}</h1>
                    <div class="flex items-center text-white/90">
                        <img src="{{ post.author.avatar_url }}" 
                             class="w-10 h-10 rounded-full mr-3">
                        <div>
                            <div class="font-medium">{{ post.author.username }}</div>
                            <div class="text-sm">
                                {{ post.created_at.strftime('%B %d, %Y') }} • 
                                {{ post.views }} views
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Content -->
        <div class="p-8">
            <!-- Tags -->
            {% if post.tags %}
            <div class="mb-8">
                <div class="flex flex-wrap gap-2">
                    {% for tag in post.tags.split(',') %}
                    <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm">
                        {{ tag.strip() }}
                    </span>
                    {% endfor %}
                </div>
            </div>
            {% endif %}
            
            <!-- Article Content -->
            <div class="prose prose-lg max-w-none mb-12">
                {{ post.content_html|safe }}
            </div>
            
            <!-- Author Bio -->
            <div class="border-t border-b border-gray-200 py-8 mb-8">
                <div class="flex items-center">
                    <img src="{{ post.author.avatar_url }}" 
                         class="w-16 h-16 rounded-full mr-4">
                    <div>
                        <h3 class="text-xl font-bold">{{ post.author.username }}</h3>
                        {% if post.author.bio %}
                        <p class="text-gray-600 mt-1">{{ post.author.bio }}</p>
                        {% endif %}
                    </div>
                </div>
            </div>
            
            <!-- Share -->
            <div class="mb-12">
                <h3 class="text-lg font-bold mb-4">Share this article</h3>
                <div class="flex space-x-4">
                    <a href="#" class="bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700">
                        <i class="fab fa-twitter"></i>
                    </a>
                    <a href="#" class="bg-blue-800 text-white p-3 rounded-lg hover:bg-blue-900">
                        <i class="fab fa-facebook-f"></i>
                    </a>
                    <a href="#" class="bg-gray-800 text-white p-3 rounded-lg hover:bg-black">
                        <i class="fab fa-linkedin-in"></i>
                    </a>
                    <a href="#" class="bg-red-600 text-white p-3 rounded-lg hover:bg-red-700">
                        <i class="fab fa-pinterest-p"></i>
                    </a>
                </div>
            </div>
        </div>
    </article>
    
    <!-- Related Posts -->
    {% if related_posts %}
    <div class="mt-16">
        <h2 class="text-2xl font-bold mb-8">Related Articles</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            {% for related in related_posts %}
            <div class="bg-white rounded-xl shadow-md overflow-hidden card-hover">
                <img src="{{ related.image_url }}" 
                     alt="{{ related.title }}"
                     class="w-full h-48 object-cover">
                <div class="p-6">
                    <h3 class="text-lg font-bold mb-2">
                        <a href="{{ url_for('blog_detail', slug=related.slug) }}" 
                           class="text-gray-900 hover:text-blue-600">
                            {{ related.title }}
                        </a>
                    </h3>
                    <p class="text-gray-600 text-sm mb-3">
                        {{ related.created_at.strftime('%b %d, %Y') }}
                    </p>
                    <a href="{{ url_for('blog_detail', slug=related.slug) }}" 
                       class="text-blue-600 text-sm font-medium">
                        Read Article
                    </a>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
    {% endif %}
</div>
{% endblock %}
''',
    'future_tech.html': '''
{% extends "base.html" %}

{% block title %}Future Technology - AutoTech Future{% endblock %}

{% block content %}
<div class="max-w-7xl mx-auto px-4 py-8">
    <!-- Header -->
    <div class="text-center mb-12">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">Future Automotive Technologies</h1>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
            Explore groundbreaking innovations that will redefine transportation in the coming decades
        </p>
    </div>
    
    <!-- Timeline -->
    <div class="mb-16">
        <h2 class="text-2xl font-bold mb-8 text-center">Technology Roadmap 2024-2035</h2>
        <div class="relative">
            <div class="absolute left-0 right-0 h-1 bg-blue-200 top-1/2 transform -translate-y-1/2"></div>
            <div class="relative flex justify-between" id="timelineContainer">
                <!-- Timeline will be populated by JavaScript -->
            </div>
        </div>
    </div>
    
    <!-- Technologies Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        {% for tech in technologies %}
        <div class="bg-white rounded-xl shadow-lg overflow-hidden card-hover">
            <div class="p-6">
                <div class="flex justify-between items-start mb-4">
                    <span class="bg-blue-100 text-blue-600 px-3 py-1 rounded-full text-sm font-medium">
                        {{ tech.category }}
                    </span>
                    <div class="text-yellow-500">
                        {% for i in range(5) %}
                            {% if i < tech.impact_level %}
                                <i class="fas fa-star"></i>
                            {% else %}
                                <i class="far fa-star"></i>
                            {% endif %}
                        {% endfor %}
                    </div>
                </div>
                
                <h3 class="text-xl font-bold mb-3">{{ tech.title }}</h3>
                <p class="text-gray-600 mb-4">{{ tech.description }}</p>
                
                <div class="flex justify-between items-center text-sm">
                    <span class="text-gray-500">
                        <i class="far fa-calendar mr-1"></i>{{ tech.timeline }}
                    </span>
                    <span class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full">
                        {{ tech.status }}
                    </span>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
    
    <!-- Innovation Areas -->
    <div class="bg-gray-900 text-white rounded-2xl p-8">
        <h2 class="text-2xl font-bold mb-8 text-center">Key Innovation Areas</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="text-center p-6 bg-gray-800 rounded-xl hover:bg-gray-700 transition duration-300">
                <div class="w-16 h-16 rounded-full bg-blue-600 flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-bolt text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold mb-2">Electrification</h3>
                <p class="text-gray-300">Next-gen batteries and charging</p>
            </div>
            
            <div class="text-center p-6 bg-gray-800 rounded-xl hover:bg-gray-700 transition duration-300">
                <div class="w-16 h-16 rounded-full bg-green-600 flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-robot text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold mb-2">Autonomy</h3>
                <p class="text-gray-300">AI-driven self-driving systems</p>
            </div>
            
            <div class="text-center p-6 bg-gray-800 rounded-xl hover:bg-gray-700 transition duration-300">
                <div class="w-16 h-16 rounded-full bg-purple-600 flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-recycle text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold mb-2">Sustainability</h3>
                <p class="text-gray-300">Circular economy solutions</p>
            </div>
            
            <div class="text-center p-6 bg-gray-800 rounded-xl hover:bg-gray-700 transition duration-300">
                <div class="w-16 h-16 rounded-full bg-red-600 flex items-center justify-center mx-auto mb-4">
                    <i class="fas fa-wifi text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold mb-2">Connectivity</h3>
                <p class="text-gray-300">V2X communication networks</p>
            </div>
        </div>
    </div>
</div>

<script>
// Load timeline data
async function loadTimeline() {
    try {
        const response = await fetch('/api/tech-timeline');
        const timeline = await response.json();
        
        const container = document.getElementById('timelineContainer');
        container.innerHTML = '';
        
        timeline.forEach((item, index) => {
            const itemDiv = document.createElement('div');
            itemDiv.className = 'text-center relative z-10';
            itemDiv.innerHTML = `
                <div class="w-6 h-6 bg-blue-600 rounded-full mx-auto mb-4"></div>
                <div class="bg-white p-4 rounded-lg shadow-lg min-w-32">
                    <div class="font-bold text-blue-600">${item.year}</div>
                    <div class="font-medium">${item.tech}</div>
                    <div class="text-sm text-gray-500 mt-1">${item.description}</div>
                </div>
            `;
            container.appendChild(itemDiv);
        });
    } catch (error) {
        console.error('Error loading timeline:', error);
    }
}

document.addEventListener('DOMContentLoaded', loadTimeline);
</script>
{% endblock %}
''',
    '3d_visualization.html': '''
{% extends "base.html" %}

{% block title %}3D Visualization - AutoTech Future{% endblock %}

{% block content %}
<div class="max-w-7xl mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-2">3D Automotive Visualizations</h1>
    <p class="text-gray-600 mb-8">Interactive 3D models of future automotive technologies</p>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- 3D Viewer -->
        <div class="bg-gray-900 rounded-xl p-4">
            <div id="modelCanvas" class="w-full h-96 rounded-lg"></div>
            <div class="mt-4 text-white text-center">
                <p>Interactive 3D Model Viewer</p>
                <p class="text-sm text-gray-400 mt-1">
                    Drag to rotate • Scroll to zoom • Right-click to pan
                </p>
            </div>
        </div>
        
        <!-- Controls -->
        <div class="bg-white rounded-xl shadow-lg p-6">
            <h2 class="text-xl font-bold mb-6">Model Controls</h2>
            
            <div class="space-y-6">
                <!-- Model Selection -->
                <div>
                    <label class="block text-gray-700 mb-2">Select Model</label>
                    <select id="modelSelect" 
                            class="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500">
                        <option value="car">Future Electric Car</option>
                        <option value="engine">Electric Powertrain</option>
                        <option value="battery">Solid-State Battery</option>
                        <option value="chassis">Lightweight Chassis</option>
                    </select>
                </div>
                
                <!-- View Options -->
                <div>
                    <label class="block text-gray-700 mb-2">View Presets</label>
                    <div class="grid grid-cols-2 gap-2">
                        <button onclick="setView('front')" 
                                class="bg-gray-100 hover:bg-gray-200 p-3 rounded-lg text-center">
                            <i class="fas fa-eye mb-2 block text-lg"></i>
                            Front View
                        </button>
                        <button onclick="setView('top')" 
                                class="bg-gray-100 hover:bg-gray-200 p-3 rounded-lg text-center">
                            <i class="fas fa-arrow-up mb-2 block text-lg"></i>
                            Top View
                        </button>
                        <button onclick="setView('side')" 
                                class="bg-gray-100 hover:bg-gray-200 p-3 rounded-lg text-center">
                            <i class="fas fa-arrow-right mb-2 block text-lg"></i>
                            Side View
                        </button>
                        <button onclick="setView('perspective')" 
                                class="bg-gray-100 hover:bg-gray-200 p-3 rounded-lg text-center">
                            <i class="fas fa-cube mb-2 block text-lg"></i>
                            3D View
                        </button>
                    </div>
                </div>
                
                <!-- Animation -->
                <div>
                    <label class="flex items-center justify-between mb-2">
                        <span class="text-gray-700">Rotation Animation</span>
                        <input type="checkbox" 
                               id="animateToggle" 
                               checked
                               class="toggle">
                    </label>
                    <div class="text-sm text-gray-500">
                        Continuously rotate the model for better visualization
                    </div>
                </div>
                
                <!-- Model Info -->
                <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
                    <h3 class="font-bold text-blue-800 mb-2">Model Information</h3>
                    <div id="modelInfo" class="text-blue-700">
                        <p><strong>Model:</strong> Future Electric Car Concept</p>
                        <p><strong>Scale:</strong> 1:20</p>
                        <p><strong>Components:</strong> 1,247 parts</p>
                        <p><strong>Features:</strong> Aerodynamic design, integrated sensors, modular battery system</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Technology Descriptions -->
    <div class="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-white rounded-xl shadow p-6">
            <div class="text-blue-600 text-2xl mb-3">
                <i class="fas fa-car-battery"></i>
            </div>
            <h3 class="font-bold mb-2">Battery Systems</h3>
            <p class="text-gray-600 text-sm">3D models of advanced battery packs and thermal management</p>
        </div>
        
        <div class="bg-white rounded-xl shadow p-6">
            <div class="text-green-600 text-2xl mb-3">
                <i class="fas fa-cogs"></i>
            </div>
            <h3 class="font-bold mb-2">Powertrain</h3>
            <p class="text-gray-600 text-sm">Electric motor assemblies and transmission systems</p>
        </div>
        
        <div class="bg-white rounded-xl shadow p-6">
            <div class="text-purple-600 text-2xl mb-3">
                <i class="fas fa-satellite-dish"></i>
            </div>
            <h3 class="font-bold mb-2">Sensors</h3>
            <p class="text-gray-600 text-sm">LIDAR, radar, and camera systems for autonomy</p>
        </div>
        
        <div class="bg-white rounded-xl shadow p-6">
            <div class="text-red-600 text-2xl mb-3">
                <i class="fas fa-shield-alt"></i>
            </div>
            <h3 class="font-bold mb-2">Safety</h3>
            <p class="text-gray-600 text-sm">Crash structures and safety system integration</p>
        </div>
    </div>
</div>

<script>
// Simple 3D viewer implementation
let isAnimating = true;

function setView(view) {
    alert('In a full implementation, this would change the 3D view to: ' + view);
    // Implementation would use Three.js to adjust camera position
}

document.getElementById('animateToggle').addEventListener('change', function(e) {
    isAnimating = e.target.checked;
    if (isAnimating) {
        console.log('Animation started');
    } else {
        console.log('Animation stopped');
    }
});

document.getElementById('modelSelect').addEventListener('change', function(e) {
    const model = e.target.value;
    const info = document.getElementById('modelInfo');
    
    const modelInfo = {
        'car': {
            name: 'Future Electric Car Concept',
            scale: '1:20',
            parts: '1,247',
            features: 'Aerodynamic design, integrated sensors, modular battery system'
        },
        'engine': {
            name: 'Electric Powertrain System',
            scale: '1:5',
            parts: '892',
            features: 'Dual motor setup, regenerative braking, thermal management'
        },
        'battery': {
            name: 'Solid-State Battery Pack',
            scale: '1:10',
            parts: '356',
            features: 'Modular design, liquid cooling, energy management system'
        },
        'chassis': {
            name: 'Lightweight Carbon Fiber Chassis',
            scale: '1:15',
            parts: '1,042',
            features: 'Carbon fiber composite, crash structures, battery integration'
        }
    };
    
    const data = modelInfo[model];
    info.innerHTML = `
        <p><strong>Model:</strong> ${data.name}</p>
        <p><strong>Scale:</strong> ${data.scale}</p>
        <p><strong>Components:</strong> ${data.parts} parts</p>
        <p><strong>Features:</strong> ${data.features}</p>
    `;
});

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    console.log('3D Visualization page loaded');
    // In production, you would initialize Three.js here
});
</script>

<style>
.toggle {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
}

.toggle input {
    opacity: 0;
    width: 0;
    height: 0;
}

.toggle-slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: .4s;
    border-radius: 34px;
}

.toggle-slider:before {
    position: absolute;
    content: "";
    height: 26px;
    width: 26px;
    left: 4px;
    bottom: 4px;
    background-color: white;
    transition: .4s;
    border-radius: 50%;
}

input:checked + .toggle-slider {
    background-color: #3b82f6;
}

input:checked + .toggle-slider:before {
    transform: translateX(26px);
}
</style>
{% endblock %}
'''
}

# Create error pages
error_pages = {
    '404.html': '''
{% extends "base.html" %}

{% block title %}Page Not Found - AutoTech Future{% endblock %}

{% block content %}
<div class="min-h-[70vh] flex items-center justify-center px-4">
    <div class="text-center">
        <div class="text-9xl font-bold text-blue-600 mb-4">404</div>
        <h1 class="text-3xl font-bold text-gray-900 mb-4">Page Not Found</h1>
        <p class="text-gray-600 mb-8 max-w-md mx-auto">
            The page you're looking for doesn't exist or has been moved.
        </p>
        <div class="space-x-4">
            <a href="{{ url_for('index') }}" 
               class="inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 font-medium">
                Go Home
            </a>
            <a href="{{ url_for('blog') }}" 
               class="inline-block bg-gray-200 text-gray-700 px-6 py-3 rounded-lg hover:bg-gray-300 font-medium">
                Browse Blog
            </a>
        </div>
    </div>
</div>
{% endblock %}
''',
    '500.html': '''
{% extends "base.html" %}

{% block title %}Server Error - AutoTech Future{% endblock %}

{% block content %}
<div class="min-h-[70vh] flex items-center justify-center px-4">
    <div class="text-center">
        <div class="text-9xl font-bold text-red-600 mb-4">500</div>
        <h1 class="text-3xl font-bold text-gray-900 mb-4">Server Error</h1>
        <p class="text-gray-600 mb-8 max-w-md mx-auto">
            Something went wrong on our end. Please try again later.
        </p>
        <div class="space-x-4">
            <a href="{{ url_for('index') }}" 
               class="inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 font-medium">
                Go Home
            </a>
            <button onclick="window.location.reload()" 
                    class="inline-block bg-gray-200 text-gray-700 px-6 py-3 rounded-lg hover:bg-gray-300 font-medium">
                Try Again
            </button>
        </div>
    </div>
</div>
{% endblock %}
'''
}

# Create static files
static_css = '''/* static/css/style.css */
/* AutoTech Future - Main Stylesheet */

/* Custom Utilities */
.line-clamp-1 {
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
}

.line-clamp-2 {
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
}

.line-clamp-3 {
    overflow: hidden;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.animate-fade-in {
    animation: fadeIn 0.5s ease-out;
}

.animate-slide-up {
    animation: slideUp 0.5s ease-out;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: #555;
}

/* Article Content Styling */
.prose {
    color: #374151;
}

.prose h2 {
    font-size: 1.875rem;
    font-weight: bold;
    margin-top: 2rem;
    margin-bottom: 1rem;
    color: #1f2937;
}

.prose h3 {
    font-size: 1.5rem;
    font-weight: bold;
    margin-top: 1.5rem;
    margin-bottom: 0.75rem;
    color: #374151;
}

.prose p {
    margin-bottom: 1rem;
    line-height: 1.8;
}

.prose ul {
    list-style-type: disc;
    padding-left: 1.5rem;
    margin-bottom: 1rem;
}

.prose ol {
    list-style-type: decimal;
    padding-left: 1.5rem;
    margin-bottom: 1rem;
}

.prose li {
    margin-bottom: 0.5rem;
}

.prose blockquote {
    border-left: 4px solid #3b82f6;
    padding-left: 1rem;
    font-style: italic;
    color: #6b7280;
    margin: 1rem 0;
}

.prose code {
    background-color: #f3f4f6;
    padding: 0.2rem 0.4rem;
    border-radius: 0.25rem;
    font-family: 'Courier New', monospace;
    font-size: 0.875em;
}

.prose pre {
    background-color: #1f2937;
    color: #f3f4f6;
    padding: 1rem;
    border-radius: 0.5rem;
    overflow-x: auto;
    margin: 1rem 0;
}

.prose pre code {
    background-color: transparent;
    padding: 0;
    color: inherit;
}

.prose a {
    color: #3b82f6;
    text-decoration: underline;
}

.prose a:hover {
    color: #2563eb;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2.5rem !important;
    }
    
    .prose h2 {
        font-size: 1.5rem;
    }
    
    .prose h3 {
        font-size: 1.25rem;
    }
}

/* Print Styles */
@media print {
    .no-print {
        display: none !important;
    }
    
    .prose {
        font-size: 12pt;
        line-height: 1.5;
    }
}
'''

static_js = '''// static/js/main.js
// AutoTech Future - Main JavaScript

// DOM Ready
document.addEventListener('DOMContentLoaded', function() {
    initializeComponents();
    setupEventListeners();
});

// Initialize all components
function initializeComponents() {
    // Initialize tooltips
    initTooltips();
    
    // Initialize lazy loading
    initLazyLoading();
    
    // Initialize smooth scrolling
    initSmoothScroll();
    
    // Initialize forms
    initForms();
}

// Setup event listeners
function setupEventListeners() {
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            mobileMenu.classList.toggle('hidden');
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!mobileMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                mobileMenu.classList.add('hidden');
            }
        });
    }
    
    // Flash messages auto-dismiss
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = '0';
            setTimeout(() => {
                if (msg.parentNode) {
                    msg.parentNode.removeChild(msg);
                }
            }, 300);
        }, 5000);
    });
}

// Initialize tooltips
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', showTooltip);
        element.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(event) {
    const tooltipText = event.target.getAttribute('data-tooltip');
    if (!tooltipText) return;
    
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = tooltipText;
    tooltip.style.cssText = `
        position: absolute;
        background: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 6px 12px;
        border-radius: 4px;
        font-size: 14px;
        z-index: 1000;
        pointer-events: none;
        transform: translateY(-100%);
        margin-top: -8px;
        max-width: 200px;
        word-wrap: break-word;
    `;
    
    const rect = event.target.getBoundingClientRect();
    tooltip.style.left = `${rect.left + (rect.width / 2)}px`;
    tooltip.style.top = `${rect.top}px`;
    tooltip.style.transform = 'translate(-50%, -100%)';
    
    document.body.appendChild(tooltip);
    event.target._tooltip = tooltip;
}

function hideTooltip(event) {
    if (event.target._tooltip) {
        event.target._tooltip.remove();
        event.target._tooltip = null;
    }
}

// Initialize lazy loading
function initLazyLoading() {
    if ('IntersectionObserver' in window) {
        const lazyImages = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.add('loaded');
                    observer.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(img => imageObserver.observe(img));
    } else {
        // Fallback for older browsers
        document.querySelectorAll('img[data-src]').forEach(img => {
            img.src = img.dataset.src;
        });
    }
}

// Initialize smooth scrolling
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#' || href === '') return;
            
            e.preventDefault();
            const targetElement = document.querySelector(href);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Initialize forms
function initForms() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        // Add loading state to submit buttons
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            form.addEventListener('submit', function() {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i> Processing...';
            });
        }
    });
}

// API Helper Functions
class API {
    static async get(endpoint) {
        try {
            const response = await fetch(endpoint);
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error('API GET Error:', error);
            throw error;
        }
    }
    
    static async post(endpoint, data) {
        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || `HTTP ${response.status}`);
            }
            
            return await response.json();
        } catch (error) {
            console.error('API POST Error:', error);
            throw error;
        }
    }
}

// Image Upload Helper
class ImageUploader {
    static preview(inputId, previewId) {
        const input = document.getElementById(inputId);
        const preview = document.getElementById(previewId);
        
        if (!input || !preview) return;
        
        input.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.classList.remove('hidden');
                };
                reader.readAsDataURL(file);
            }
        });
    }
}

// Utility Functions
const Utils = {
    // Format date
    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    },
    
    // Truncate text
    truncate(text, length = 100) {
        if (text.length <= length) return text;
        return text.substring(0, length) + '...';
    },
    
    // Debounce function
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },
    
    // Throttle function
    throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
};

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { API, ImageUploader, Utils };
}
'''

# Save all files
for filename, content in templates.items():
    with open(f'templates/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)

for filename, content in error_pages.items():
    with open(f'templates/{filename}', 'w', encoding='utf-8') as f:
        f.write(content)

# Save static files
with open('static/css/style.css', 'w', encoding='utf-8') as f:
    f.write(static_css)

with open('static/js/main.js', 'w', encoding='utf-8') as f:
    f.write(static_js)

print("All templates created successfully!")