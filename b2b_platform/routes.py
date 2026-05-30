from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from b2b_platform import db
# Import models from package
from b2b_platform.models import User, Company, Post, Project, Message
from b2b_platform import login_manager
main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login"""
    return User.query.get(int(user_id))
@main.route('/')
def index():
    """Home page - redirects to dashboard or login"""
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.home'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('login.html')

@main.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page"""
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        company_name = request.form.get('company_name')
        full_name = request.form.get('full_name')
        
        # Check if user exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return render_template('register.html')
        
        # Create new user
        user = User(
            email=email,
            password=generate_password_hash(password),
            full_name=full_name
        )
        
        # Create company
        company = Company(name=company_name, owner_id=user.id)
        
        from __init__ import db
        db.session.add(user)
        db.session.commit()
        
        company.owner_id = user.id
        db.session.add(company)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')

@main.route('/home')
@login_required
def home():
    """Home screen with welcome message, quick actions, AI recommendations, and activity feed"""
    # Get recent posts for activity feed
    posts = Post.query.order_by(Post.created_at.desc()).limit(10).all()
    
    return render_template('home.html', posts=posts)

@main.route('/dashboard')
@login_required
def dashboard():
    """Workspace dashboard with stats and services"""
    # Get user stats
    projects_count = Project.query.filter_by(user_id=current_user.id).count()
    messages_count = Message.query.filter(
        (Message.sender_id == current_user.id) | (Message.receiver_id == current_user.id)
    ).count()
    opportunities_count = 7  # This would be calculated based on business logic
    
    return render_template('dashboard.html', 
                         projects_count=projects_count,
                         messages_count=messages_count,
                         opportunities_count=opportunities_count)

@main.route('/profile/<int:user_id>')
@login_required
def profile(user_id):
    """User profile page"""
    user = User.query.get_or_404(user_id)
    company = Company.query.filter_by(owner_id=user_id).first()
    
    # Calculate stats
    posts_count = Post.query.filter_by(company_id=company.id if company else None).count()
    connections_count = 0  # Would need a connections table
    
    return render_template('profile.html', user=user, company=company,
                         posts_count=posts_count, connections_count=connections_count)

@main.route('/feed')
@login_required
def feed():
    """Social feed page"""
    # Get posts with filters
    filter_type = request.args.get('filter', 'recommended')
    
    if filter_type == 'following':
        # Get posts from followed companies/users
        posts = Post.query.order_by(Post.created_at.desc()).all()
    else:
        # Recommended posts
        posts = Post.query.order_by(Post.created_at.desc()).all()
    
    return render_template('feed.html', posts=posts, filter_type=filter_type)

@main.route('/search')
@login_required
def search():
    """Search page"""
    query = request.args.get('q', '')
    search_type = request.args.get('type', 'all')  # all, companies, posts
    
    results = {
        'companies': [],
        'posts': []
    }
    
    if query:
        if search_type in ['all', 'companies']:
            results['companies'] = Company.query.filter(Company.name.ilike(f'%{query}%')).limit(10).all()
        
        if search_type in ['all', 'posts']:
            results['posts'] = Post.query.filter(Post.title.ilike(f'%{query}%')).limit(10).all()
    
    return render_template('search.html', results=results, query=query)
