#!/usr/bin/env python3
"""
Run script for B2B Traders Platform
"""
import os
import sys


# Add the parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from b2b_platform import create_app, db
from b2b_platform.models import User, Company, Post

def seed_database():
    """Seed the database with sample data"""
    print("Seeding database with sample data...")

    # Create sample user
    user = User.query.filter_by(email='demo@b2bplatform.com').first()
    
    if not user:
        user = User(
            email='demo@b2bplatform.com',
            full_name='Masoud kh',
            is_verified=True
        )
        user.set_password('demo123')
        db.session.add(user)
        db.session.commit()
        
        # Create sample company
        company = Company(
            name='Tehran Trading Company',
            description='Professional trading company specializing in international commerce and business partnerships. We connect businesses across borders.',
            location='Tehran, Iran',
            industry='General Trading',
            is_verified=True,
            rating=4.8,
            owner_id=user.id
        )
        db.session.add(company)
        db.session.commit()
        
        # Create sample posts
        posts_data = [
            {
                'title': 'Wheat Export Opportunity to Iraq',
                'content': 'Looking for reliable partners for wheat export to Iraq market. High quality products with competitive pricing.',
                'industry_tag': 'Agriculture & Food',
                'details': {'quantity': '5000 tons', 'deadline': '2026/06/14'}
            },
            {
                'title': 'Steel Products Import from China',
                'content': 'Seeking suppliers for steel products import. Long-term partnership opportunity available.',
                'industry_tag': 'Manufacturing',
                'details': {'quantity': '2000 tons', 'deadline': '2025/12/31'}
            },
            {
                'title': 'Textile Manufacturing Partnership',
                'content': 'Established textile manufacturer looking for distribution partners in Middle East region.',
                'industry_tag': 'Textiles',
                'details': {}
            }
        ]
        
        for post_data in posts_data:
            post = Post(
                title=post_data['title'],
                content=post_data['content'],
                industry_tag=post_data['industry_tag'],
                details=post_data['details'],
                company_id=company.id,
                views_count=249,
                comments_count=29
            )
            db.session.add(post)
        
        db.session.commit()
        print("✓ Sample data created successfully!")
        print(f"  - User: demo@b2bplatform.com / demo123")
        print(f"  - Company: {company.name}")
        print(f"  - Posts: {len(posts_data)}")
    else:
        print("✓ Database already seeded")

if __name__ == '__main__':
    app = create_app()
    
    # Check if we should seed the database
    if len(sys.argv) > 1 and sys.argv[1] == '--seed':
        with app.app_context():
            try:
                seed_database()
            except Exception as e:
                print(f"Error seeding database: {e}")
                import traceback

                traceback.print_exc()
    else:
        # Run the application
        print("=" * 50)
        print("B2B Traders Platform")
        print("=" * 50)
        print("\nStarting development server...")
        print("\nAccess the application at: http://localhost:5000")
        print("\nDemo credentials:")
        print("  Email: demo@b2bplatform.com")
        print("  Password: demo123")
        print("\nPress Ctrl+C to quit\n")
        
        app.run(debug=True, host='0.0.0.0', port=5000)
