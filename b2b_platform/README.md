# B2B Traders Platform

A professional B2B trading platform built with Flask, PostgreSQL, and modern web technologies.

## Features

- **User Authentication**: Secure login and registration system
- **Company Profiles**: Professional business profiles with verification badges
- **Social Feed**: Business opportunities and trade posts
- **Dashboard**: Workspace with statistics and service cards
- **Mobile-First Design**: Optimized for mobile devices with responsive layout
- **Professional UI**: Clean, minimal design following the provided design system

## Tech Stack

- **Backend**: Python 3, Flask
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Authentication**: Flask-Login

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

### 1. Clone and Setup

```bash
cd b2b_platform
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL Database

```bash
# Create database
createdb b2b_platform

# Or using psql
psql -U postgres
CREATE DATABASE b2b_platform;
\q
```

### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://postgres:password@localhost:5432/b2b_platform
FLASK_ENV=development
```

### 6. Initialize Database

```bash
# Using Flask-Migrate
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

Or use the run script with seed data:

```bash
python run.py --seed
```

### 7. Run the Application

```bash
python run.py
```

The application will start at: http://localhost:5000

## Demo Credentials

After seeding the database:

- **Email**: demo@b2bplatform.com
- **Password**: demo123

## Project Structure

```
b2b_platform/
├── __init__.py              # Application factory
├── models.py                # Database models
├── routes.py                # Application routes
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   ├── home.html           # Home screen
│   ├── dashboard.html      # Workspace dashboard
│   ├── profile.html        # User profile
│   └── feed.html           # Social feed
├── static/                  # Static assets
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # Main JavaScript
│   └── images/             # Image assets
└── migrations/             # Database migrations
```

## Design System

### Colors

- **Primary Navy**: #1E3A5F
- **Primary Green**: #2ECC71
- **Accent Orange**: #F39C12
- **Accent Purple**: Gradient #667eea to #764ba2

### Typography

- **Font Family**: Inter, system fonts
- **Display**: 24-28px, Bold
- **Title**: 18-20px, SemiBold
- **Body**: 14-16px, Regular
- **Caption**: 12px, Medium

### Components

- Cards with shadow effects
- Rounded buttons (12px radius)
- Mobile-optimized navigation
- Floating Action Button (FAB)
- Progress bars
- Stats cards

## API Endpoints

### Authentication
- `GET /login` - Login page
- `POST /login` - Authenticate user
- `GET /register` - Registration page
- `POST /register` - Create new account
- `GET /logout` - Logout user

### Pages
- `GET /` - Index (redirects to home or login)
- `GET /home` - Home screen
- `GET /dashboard` - Workspace dashboard
- `GET /profile/<user_id>` - User profile
- `GET /feed` - Social feed
- `GET /search` - Search page

## Database Models

- **User**: User accounts and authentication
- **Company**: Company profiles
- **Post**: Social feed posts
- **Comment**: Post comments
- **Like**: Post likes
- **Service**: Company services
- **Project**: User projects
- **Message**: User messages
- **Connection**: User connections

## Development

### Running Tests

```bash
pytest
```

### Database Migrations

```bash
# Create new migration
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade

# Rollback migrations
flask db downgrade
```

## Deployment

### Production Settings

1. Set `FLASK_ENV=production`
2. Use a production WSGI server (Gunicorn)
3. Configure proper database credentials
4. Set strong SECRET_KEY
5. Enable HTTPS

### Using Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## License

This project is proprietary software. All rights reserved.

## Support

For support and questions, please contact the development team.
