#  BuildConnect – Contractor & Homeowner Platform

BuildConnect is a Django-based web application that connects homeowners with professional contractors for renovation and construction projects.

Homeowners can post jobs, and contractors can apply with price offers and personal messages.

---

##  Project Purpose

The main goal of this project is to provide a simple and user-friendly platform where:

- Homeowners can easily publish renovation and construction jobs.
- Contractors can browse available jobs and apply for them.
- Applications can be reviewed, accepted, or rejected.

This project is developed as part of the Django Basics course at SoftUni.

---

##  Technologies Used

- Python [3.9.13]
- Django [4.2.27]
- PostgreSQL
- Bootstrap 5
- HTML5 / CSS3

---

##  Project Structure

The project consists of the following Django apps:

- **jobs** – Manages job listings, categories, and cities.
- **contractors** – Handles contractor profiles and skills.
- **applications** – Manages job applications.
- **common** – Contains shared models and utilities.

---

##  Database Models

Main models used in the project:

- Job
- Contractor
- Application
- City
- Category
- Skill

### Relationships

- One-to-Many: City → Job, Category → Job
- Many-to-Many: Contractor ↔ Skill
- One-to-Many: Job → Application
- One-to-Many: Contractor → Application

---

##  Main Features

- Full CRUD operations for Jobs and Contractors
- Job search and filtering
- Contractor skill management
- Application system with validation
- Accept / Reject application functionality
- Custom template filters
- Custom 404 error page
- Responsive UI with Bootstrap
- Pagination

---

##  Forms & Validation

The project includes multiple customized forms with:

- Field validation
- Custom error messages
- Placeholders and help texts
- Disabled fields for delete confirmation
- Duplicate application prevention
- Budget and experience validation

---

## 📸 Screenshots

### Home Page
![Home](screenshots/home_page.bmp)

### Job Listings
![Jobs](screenshots/job_list.bmp)

### Job Detail
![Job Detail](screenshots/job_detail.bmp)

### Contractors
![Contractors](screenshots/contractor_list.bmp)

### Contractor Profile
![Contractor Detail](screenshots/contractor_detail.bmp)

### Create Job
![Create Job](screenshots/job_create.bmp)

### Apply for Job
![Apply](screenshots/job_apply.bmp)


## 🚀 Installation & Setup

Follow these steps to run the project locally:

---

### 1. Clone the Repository

```bash
git clone https://github.com/feik123/buildconnect-platform.git
cd buildconnect-platform
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
``` 
Activate the virtual environment:
- On Windows:
```bash 
venv\Scripts\activate
```
- On macOS/Linux:
```bash 
source venv/bin/activate
``` 
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root based on `.env.template`.

Example `.env` for local testing:

SECRET_KEY=django-insecure-buildconnect-local-key  
DEBUG=True  
ALLOWED_HOSTS=127.0.0.1,localhost  

# PostgreSQL (optional)
DB_NAME=buildconnect_db  
DB_USER=postgres  
DB_PASSWORD=postgres  
DB_HOST=localhost  
DB_PORT=5432  

If PostgreSQL credentials are not provided,
the application can use SQLite.