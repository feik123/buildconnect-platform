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
- Django [6.0.2]
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

##  Installation & Setup

Follow these steps to run the project locally:

### 1 Clone the repository

```bash
git clone https://github.com/[your-username]/[your-repo-name].git
cd [your-repo-name]