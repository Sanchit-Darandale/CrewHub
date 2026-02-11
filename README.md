# CrewHub - Service Marketplace Platform

## Project Overview

CrewHub is a comprehensive service marketplace web application that connects workers (electricians, plumbers, carpenters, etc.) with people who need their services. The platform supports three distinct user roles: Users, Worker, admin each with tailored functionality.

## Target Market Identification

- **B2C (Primary consumer segment):**
  - Homeowners, renters, and individuals needing home maintenance or repairs.
  - Examples: busy professionals, elderly residents, students.

- **B2B (Commercial segment):**
  - Small businesses, local retail, and SMEs that need maintenance or facility services.

- **B2G (Institutional segment):**
  - Residential societies, housing associations, or municipal agencies coordinating area services.

- **Recommended initial focus:** Launch with B2C (urban homeowners and renters) plus B2G (residential societies). Societies provide recurring demand and faster uptake via community-level adoption.

## Market Segmentation

- **Geographic:**
  - Phase 1: Single-city pilot (focus on one metro area). Lower operational overhead and easier local marketing.
  - Phase 2: Expand to nearby cities and then region/statewide.

- **Demographic:**
  - Primary: Adults 25–60 (homeowners, working professionals), middle to upper-middle income.
  - Secondary: Society managers/secretaries and small-business facility managers.

- **Usage-based:**
  - Regular users: Society managers, property managers, businesses (recurring maintenance).
  - Occasional users: Individual residents with occasional repair needs.

- **Initial launch segment (focus):** Urban residential societies in a single city (B2G-first within the broader B2C/B2G mix) to capture recurring contracts and resident sign-ups.

## Operational & Growth Suggestions

- **MVP (current):** Discovery, registration, role-based dashboards, pincode-based search, secure login. Good for a pilot in one city.

- **Next features to prioritize:**
  1. Booking / job request flow (user books a worker, scheduling)
  2. Ratings & reviews for quality signals
  3. In-app messaging or phone-masked contact
  4. Admin dashboard and analytics


## Monetization (brief)
- Commission on transactions (percentage per job)
- Subscription plans for societies / businesses for premium features
- Featured listings / promoted worker profiles for increased visibility

## Technology Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: MongoDB
- **Authentication**: Session-based with hashed passwords (Werkzeug)
- **Architecture**: MVC Pattern
- **Environment**: `python-dotenv` for environment variables


### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Custom responsive design
- **JavaScript**: Vanilla JS for client-side functionality

### Key Features
- Role-based authentication and authorization
- Worker discovery by service type and location, rating, etc
- Profile management for all user types
- Real-time search and filtering
- Responsive design for all devices

### Key benefits:
  - **Efficiency:** Faster discovery through indexed search and filters.
  - **Cost saving:** Societies and repeat B2B customers gain negotiated/bulk options.
  - **Automation:** Role-based dashboards reduce manual coordination overhead.
  - **Safety & Trust:** Password hashing, role separation, and identity-backed profiles.
  - **Scalability:** Modular MVC code structure and database indexes for performant queries.

## Project Structure

```
CrewHub/
├── app.py                      # Main Flask application (Controller)
├── models.py                   # Database models (Model)
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css          # Complete stylesheet
│   └── js/
│       └── main.js            # Client-side JavaScript
└── templates/                  # HTML templates (View)
    ├── base.html              # Base layout template
    ├── index.html             # Homepage
    ├── admin.html             # Admin Dashboard
    ├── login.html             # Login page
    ├── register.html          # Role selection
    ├── register_user.html     # User registration
    ├── register_worker.html   # Worker registration
    ├── register_society.html  # Society registration
    ├── dashboard.html         # Role-based dashboard
    ├── workers.html           # Worker listing
    └── worker_profile.html    # Worker profile page
```

## Using the Application

### 1. Register an Account

**Register as User:**
1. Click "Register" → "Register as User"
2. Fill in all required fields
3. Submit the form

**Register as Worker:**
1. Click "Register" → "Register as Worker"
2. Select your service type
3. Fill in experience and other details
4. Submit the form

### 2. Login
1. Go to login page
2. Enter your email and password
3. You'll be redirected to your role-specific dashboard

**Login as Admin:**
1. Click "Login" → "Admin Creditials"
2. Admin dashboard
3. make changes as per report 

### 3. User Features

- Search workers by service type, ratings and pincode (add more soon)
- View worker profiles
- Access contact information (phone/email)
- send request to worker
- Browse workers in your area

### 4. Worker Features

- View your profile
- Check visibility status
- Get client request 
- See your profile information


### Available Worker Types
- Electrician
- Plumber
- Carpenter
- Painter
- Mason
- Welder
- Gardener
- House Cleaning
- Pest Control
- AC Repair
- Other i will add soon

## API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Homepage |
| `/login` | GET, POST | Login page |
| `/register` | GET | Role selection |
| `/register/user` | GET, POST | User registration |
| `/register/worker` | GET, POST | Worker registration |
| `/register/society` | GET, POST | Society registration |
| `/dashboard` | GET | Role-based dashboard |
| `/workers` | GET | Worker listing with filters |
| `/worker/<id>` | GET | Individual worker profile |
| `/logout` | GET | Logout and clear session |

I will add the remaining endpoints when I get some free time.

## Database Collections

### users
```javascript
{
  _id: ObjectId,
  full_name: String,
  mobile: String,
  email: String (unique),
  address: String,
  pincode: String,
  password: String (hashed),
  role: "user",
  created_at: Date,
  updated_at: Date
}
```

### workers
```javascript
{
  _id: ObjectId,
  full_name: String,
  mobile: String,
  email: String (unique),
  address: String,
  pincode: String,
  worker_type: String,
  password: String (hashed),
  role: "worker",
  is_active: Boolean,
  created_at: Date,
  updated_at: Date
}
```

## Security Features

1. **Password Hashing**: All passwords are hashed using Werkzeug's security functions
2. **Session Management**: Secure session-based authentication
3. **Role-Based Access Control**: Different permissions for each user role
4. **Input Validation**: Both client-side and server-side validation
5. **CSRF Protection**: Built into Flask forms

## Scalability Considerations

The application is designed with scalability in mind:

1. **Database Indexing**: Indexes on email, pincode, and worker_type for faster queries
2. **Modular Architecture**: Separate models, views, and controllers
3. **RESTful Design**: Clean URL structure
4. **Connection Pooling**: MongoDB driver handles connection pooling automatically
5. **Session Management**: Can be scaled with Redis/Memcached

## Future Enhancements

Potential features for commercialization:

1. **Rating & Review System**: User feedback for workers
2. **Real-time Chat**: In-app messaging between users and workers
3. **Booking System**: Schedule appointments
4. **Worker Verification**: Document upload and verification
5. **Analytics Dashboard**: Business insights for admin
6. **Multi-language Support**: Localization

## License

This project is developed as an academic project for Technology Commercialization and Startup Development.

## Credits

Developed as a complete full-stack web application demonstrating:
- Modern web development practices
- MVC architecture
- Database design
- User authentication & authorization
- Responsive design
- Business logic implementation
