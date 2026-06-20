<img width="1599" height="801" alt="dashboard" src="https://github.com/user-attachments/assets/b0cec636-8506-4a67-9fb8-0ce3def7719d" /># 🚀 CRM Automation System

> A full-stack CRM (Customer Relationship Management) system built with **Django + n8n + Gmail** — featuring automated lead notifications, pipeline tracking, and a modern dashboard.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-4.x-green?style=flat-square&logo=django)
![n8n](https://img.shields.io/badge/n8n-Automation-orange?style=flat-square)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat-square&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

- 📋 **Lead Management** — Create, edit, delete, and track leads
- 🔄 **Pipeline Tracking** — New → Contacted → In Progress → Converted
- 📧 **Automated Email Alerts** — Gmail notification on every new lead via n8n
- 🔍 **Search & Filter** — Find leads by name, email, or company
- 📊 **Stats Dashboard** — Live count of leads at every stage
- 📁 **Export CSV** — Download all leads with one click
- 🌙 **Dark / Light Mode** — Persistent theme toggle
- 🔐 **Login Protected** — All pages require authentication
- 📱 **Fully Responsive** — Works on mobile and desktop

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap 5, Bootstrap Icons |
| Database | SQLite (dev) |
| Automation | n8n (self-hosted) |
| Email | Gmail via n8n webhook |
| Auth | Django built-in authentication |

---

## 📁 Project Structure

```
CRM_Automation_System/
│
├── crm_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── leads/
│   ├── models.py          # Lead model
│   ├── views.py           # All business logic
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin panel config
│   └── templates/leads/
│       ├── dashboard.html # Main CRM dashboard
│       ├── contact.html   # Add new lead form
│       └── edit_lead.html # Edit existing lead
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/Bismashoukat/CRM-Automation-System.git
cd CRM-Automation-System
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create admin user
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

Visit: `http://localhost:8000`

---

## 🔄 n8n Automation Setup

1. Install and run n8n locally:
```bash
npx n8n
```

2. Create a new workflow with:
   - **Node 1:** Webhook (POST) → path: `new-lead`
   - **Node 2:** Gmail → Send email notification

3. Webhook URL used in this project:
```
http://localhost:5678/webhook-test/new-lead
```

4. Email template includes: Name, Email, Phone, Company, Message in an HTML table format.

---

## 📸 Screenshots

### Dashboard
![Dashboard](<img width="1599" height="801" alt="dashboard" src="https://github.com/user-attachments/assets/3d980946-6b48-45c3-a0fe-8dc60e8239ea" />
)

### Contact Form
![Contact Form](<img width="1590" height="857" alt="contact form" src="https://github.com/user-attachments/assets/340b436d-1047-450f-9ea6-32e8efe24446" />
)

### Edit Lead
![Edit Lead](<img width="1595" height="851" alt="edit lead form" src="https://github.com/user-attachments/assets/2deff0c9-5e4e-4b18-8912-068616836388" />
)

---

## 🔐 Default Login

After running `createsuperuser`, use those credentials at:
```
http://localhost:8000/admin
```

---

## 📦 Requirements

```
Django>=4.0
requests>=2.28
```

---

## 🌟 What I Learned

- Building a full Django CRUD application from scratch
- Connecting Django backend to n8n automation webhooks
- Designing a professional responsive UI with Bootstrap 5
- Implementing search, filter, and pagination in Django
- Creating automated email workflows with n8n + Gmail
- Login-protected views with Django authentication

---

## 👩‍💻 Developer

**Bisma Shoukat** — AI Automation Developer & Full Stack Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/bisma-shoukat-50ab88378)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/Bismashoukat)
[![Fiverr](https://img.shields.io/badge/Fiverr-Hire_Me-green?style=flat-square)](https://fiverr.com/bismacoder)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
