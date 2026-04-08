import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    MONGO_URI = os.environ.get('MONGO_URI', "") 
    MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', "")
    
    CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')

    WITHDRAWAL_DATES = [5, 15, 25] 
    PLATFORM_FEE_PERCENTAGE = 15

    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', '')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', '')
    
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
    
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads', 'documents')
        
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
    