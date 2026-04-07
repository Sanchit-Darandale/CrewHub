import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb+srv://database2:database2@cluster0.p4ztr4z.mongodb.net/?appName=Cluster0'
    MONGO_DB_NAME = 'crewhub_db'
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    ADMIN_USERNAME = 'admin@crewhub.org'
    ADMIN_PASSWORD = 'admin123'  
    
    # Mail Configuration
    # To send actual emails, put your Gmail and a 16-character App Password here
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'support.crewhub@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'eahbsppwpavvecwo')
    
    # Upload Configuration
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads', 'documents')
    
    # Cloudinary Configuration
    CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL') or 'cloudinary://557494597539112:zaaMyyIlJboxW6Ca0_mDFxXi56k@decubga08'
    
    WORKER_TYPES = [
        'Electrician',
        'Plumber',
        'Carpenter',
        'Painter',
        'Mason',
        'Welder',
        'Gardener',
        'House Cleaning',
        'Pest Control',
        'AC Repair',
        'Other'
    ]
