# 🏕️ [ApexSky](https://apexsky.onrender.com) - Project Management Platform

> *Build, Manage, and Showcase your finest work.*

**ApexSky** is a comprehensive platform designed for developers and creators to manage their personal and team projects. It serves as a dynamic portfolio where users can showcase their work, organize projects into categories, and share them with the world—all without needing to edit raw HTML or CSS.

Whether you are a solo developer or a team lead, ApexSky provides the tools to document your journey, share your repositories, and track your project's lifecycle.

---

## 📸 Demo

![Site Demo](https://res.cloudinary.com/content-storage/image/upload/v1752216151/apexsky-projects-management-demo.jpg)

---

## 🚀 Key Features

- **📂 comprehensive Project Management:** Create detailed project cards with descriptions, tech stacks, and status updates.
- **🏷️ Smart Categorization:** Organize projects using **Catalogs** (e.g., App Development, Analysis) and **Labels** (e.g., Hackathon, Hobby).
- **👤 Professional Profiles:** Customizable user profiles with avatars, bios, and social links.
- **❤️ Engagement:** Discover and "Like" projects from other community members.
- **🔍 Explore & Search:** Easily find projects and developers through a dedicated explore page.
- **☁️ Cloudinary Integration:** Seamless and optimized image hosting for project thumbnails and profile pictures.
- **🔐 Secure Authentication:** Robust user account management and security.

---

## 🛠️ Tech Stack

**Backend**

- **Framework:** Python, Django
- **Database:** PostgreSQL (Production) / SQLite (Development)
- **API:** Django REST Framework (Foundation laid)

**Frontend**

- **Core:** HTML5, CSS3, JavaScript
- **Styling:** Bootstrap
- **Templating:** Django Template Language (DTL)

**Services & Tools**

- **Media Storage:** Cloudinary
- **Static Files:** WhiteNoise
- **Deployment:** Render

---

## ⚙️ Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/saidulalimallick04/apexsky-projects-management.git
cd apexsky-projects-management
```

### 2. Install Dependencies

Ensure you have Python installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory and populate it with your credentials:

```env
# Database Configuration
DATABASE_URL=Your_PostgreSQL_URL_Here

# Email Configuration
EMAIL_HOST_USER=Your_Email_Address
EMAIL_HOST_PASSWORD=Your_Email_App_Password

# Cloudinary Configuration (For Images)
CLOUDINARY_CLOUD_NAME=Your_Cloud_Name
CLOUDINARY_CLOUD_API_KEY=Your_API_Key
CLOUDINARY_CLOUD_API_SECRET=Your_API_Secret

# Security
SECRET_KEY=Your_Django_Secret_Key
```

### 4. Run Migrations

apkply the database migrations:

```bash
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📁 Project Structure

```text
apexsky-projects-management/
├── ProjectRoot/       # Core project settings and configuration
├── Home/              # Landing page and general views
├── Users/             # User authentication and profile management
├── Projects/          # Project creation, listing, and details logic
├── Blogs/             # Blog functionality (Under Development)
├── API/               # API endpoints (Foundation)
├── templates/         # HTML Templates
├── static/            # Static assets (CSS, JS, Images)
└── manage.py          # Django management script
```

---

## 👨‍💻 Author

| Profile | Developer Name | Role | GitHub | LinkedIn | X |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [![Sami](https://github.com/saidulalimallick04.png?size=75)](https://github.com/saidulalimallick04) | Saidul Ali Mallick (Sami) | Backend Developer & AIML Engineer | [@saidulalimallick04](https://github.com/saidulalimallick04) | [@saidulalimallick04](https://linkedin.com/in/saidulalimallick04) | [@saidulmallick04](https://x.com/saidulmallick04) |

> ❤️ I believe in building impact, not just writing code.
> *💚 Backend Sage signing off..*
---
