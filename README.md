# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate


# Install dependencies
pip install -r requirements.txt
```

### 3. Database Setup

```bash
# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 4. Start Redis Server

```bash
# Start Redis server (keep this running)
redis-server
```

### 5. Run the Application

```bash
# Start Django development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.
