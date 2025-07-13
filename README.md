# EZSem - End Semester Preparation Portal

A Django-based web application for end semester preparation with PDF document management and chatbot functionality.

## Features

- User authentication and authorization
- PDF document upload and management
- Chatbot integration with Gemini API
- Document search and retrieval
- Student portal with course materials

## Tech Stack

- **Backend**: Django 5.2.4
- **Database**: PostgreSQL (production), SQLite (development)
- **Web Server**: Gunicorn
- **PDF Processing**: PyMuPDF
- **AI Integration**: Google Gemini API

## Quick Start (Development)

1. **Clone the repository**
   ```bash
   git clone https://github.com/shubhi-gupta03/EndPrep.git
   cd EndPrep
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   GEMINI_API_KEY=your-gemini-api-key
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Deployment Options

### Option 1: Railway (Recommended)

1. **Sign up** at [Railway.app](https://railway.app)
2. **Connect your GitHub repository**
3. **Add environment variables**:
   - `SECRET_KEY`: Generate a secure secret key
   - `DEBUG`: Set to `False`
   - `GEMINI_API_KEY`: Your Gemini API key
   - `DATABASE_URL`: Railway will provide this automatically
4. **Deploy** - Railway will automatically detect Django and deploy

### Option 2: Render

1. **Sign up** at [Render.com](https://render.com)
2. **Create a new Web Service**
3. **Connect your GitHub repository**
4. **Configure the service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn shumarit.wsgi:application`
   - **Environment Variables**: Add the same variables as Railway
5. **Deploy**

### Option 3: Heroku

1. **Install Heroku CLI** and sign up
2. **Login to Heroku**:
   ```bash
   heroku login
   ```
3. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```
4. **Add PostgreSQL**:
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```
5. **Set environment variables**:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set GEMINI_API_KEY=your-gemini-api-key
   ```
6. **Deploy**:
   ```bash
   git push heroku main
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

### Option 4: DigitalOcean App Platform

1. **Sign up** at [DigitalOcean](https://digitalocean.com)
2. **Create a new App**
3. **Connect your GitHub repository**
4. **Configure the app**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `gunicorn shumarit.wsgi:application`
   - **Environment Variables**: Add required variables
5. **Deploy**

## Environment Variables

Create a `.env` file with the following variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False

# Database Settings (for PostgreSQL)
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432

# API Keys
GEMINI_API_KEY=your-gemini-api-key

# Allowed Hosts (comma-separated)
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

## Production Checklist

Before deploying to production:

- [ ] Set `DEBUG=False`
- [ ] Generate a new `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Set up PostgreSQL database
- [ ] Configure static file serving
- [ ] Set up SSL/HTTPS
- [ ] Configure logging
- [ ] Set up backup strategy
- [ ] Test all functionality

## File Structure

```
EZSem/
├── Accounts/          # User authentication app
├── portal/           # Main application logic
├── shumarit/         # Django project settings
├── static/           # Static files (CSS, JS, images)
├── Templates/        # HTML templates
├── media/           # User-uploaded files
├── manage.py        # Django management script
├── requirements.txt # Python dependencies
├── Procfile        # Deployment configuration
└── runtime.txt     # Python version specification
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions, please open an issue on GitHub. 