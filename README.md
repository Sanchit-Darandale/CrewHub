# CrewHub - Advanced Service Marketplace Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4.6-green?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

CrewHub is a high-performance, full-stack service marketplace that connects skilled professionals (Electricians, Plumbers, Carpenters, etc.) with local customers. Built with a robust **MVC architecture**, the platform focuses on trust, security, and absolute financial transparency.

---

## 🚀 Key Modules

### 👤 Customer Experience
*   **Smart Discovery**: Multi-filter search (Category, City, Pincode) with real-time availability.
*   **Multimedia Reporting**: A unique dispute resolution system allowing users to file reports with **integrated Image/Video evidence** powered by Cloudinary.
*   **Appointment Lifecycle**: End-to-end booking flow from request to professional invoice generation.

### ⚒️ Worker Earning Hub
*   **Dynamic Earnings Tracking**: Real-time income calculation based on "Verified Invoices."
*   **Localized Payout Windows**: Supports multiple withdrawal dates (e.g., 5th, 15th, 25th) synchronized with the **Asia/Kolkata** timezone using `pytz`.
*   **Digital Statements**: Automated generation of payout slips with dynamic platform fee deduction.

### 🛡️ Admin Command Center
*   **Verification Engine**: A secure portal for approving/rejecting new workers based on Aadhar and Certificate verification.
*   **Granular Sanctions**: Advanced banning system (Temporary/Permanent) with automated unban logic upon expiration.
*   **Audit Logging**: Comprehensive system-wide logging for all payments, appointments, and status changes.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.10+, Flask |
| **Database** | MongoDB (Atlas) |
| **Media** | Cloudinary (Secure multimedia hosting) |
| **Security** | Werkzeug (Password Hashing), Session RBAC |
| **Timezone** | `pytz` (Precision IST scaling) |
| **Styling** | Vanilla CSS3 (Custom Design System) |

---

## ⚙️ Configuration

The platform's core behavior is managed through `config.py`. Key variables include:

| Variable | Description | Default |
| :--- | :--- | :--- |
| `WITHDRAWAL_DATES` | Days of the month when payout windows open. | `[5, 15, 25]` |
| `PLATFORM_FEE_PERCENTAGE` | Dynamic platform commission rate. | `15` |
| `CLOUDINARY_URL` | Cloudinary connection string for media uploads. | *Required* |
| `MONGO_URI` | MongoDB Atlas cluster connection string. | *Required* |

---

## 📦 Installation & Quick Start

### 1. Prerequisite
Ensure you have **Python 3.10+** and a **MongoDB Atlas** account.

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Sanchit-Darandale/CrewHub.git
cd CrewHub

# Set up virtual environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the root directory:
```env
SECRET_KEY=your_secret_key
MONGO_URI=your_mongodb_uri
CLOUDINARY_URL=your_cloudinary_url
```

### 4. Launch
```bash
python app.py
```
Access the platform at `http://localhost:5000`.

---

## 📂 Architecture Overview

*   `app.py`: The Controller layer, managing routing and business logic.
*   `models.py`: The data layer, encapsulating MongoDB operations for all entities.
*   `utils.py`: Utility functions including SMTP mailers and precision helpers.
*   `static/`: Contains the optimized CSS design system and frontend assets.
*   `templates/`: Jinja2 templates following a modular inheritance pattern.

---

## 📜 Development & Support

Developed as a modern service ecosystem demonstration.

**Main Developer**: [Sanchit Darandale](https://github.com/Sanchit-Darandale)  
**Agentic AI Support**: Antigravity AI  

---
*Created for the Technology Commercialization & Startup Development Project.*