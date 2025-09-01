#### CIDM632570
  * Course Number/Section/Name: CIDM6325/70/ Electronic Commerce and Web Development Semester/Year: Fall 2025  Professor: Dr. Jeffry Babb 


# 🧠 Django CRUD MiniLab – Hallucination Checker

This Django mini-app demonstrates a secure Create/Read pattern for managing AI-generated code snippets — with an emphasis on traceability and secure software development workflows.

---

## 📚 Table of Contents

- [📁 Folder Structure](#-folder-structure)
- [📌 Project Overview](#-project-overview)
- [🛠️ Setup & Scaffold](#️-setup--scaffold)
- [🧩 Model](#-model)
- [🌐 Views + URLs](#-views--urls)
- [🔄 Django Principles](#-django-principles)
- [📸 Screenshots](#-screenshots)
- [🧪 Step-by-Step Setup Guide](#-step-by-step-setup-guide)
- [🔗 GitHub Repo Links](#-github-repo-links)
- [💡 Reflection](#-reflection)

---

## 📁 Folder Structure

```

Module1Assignment/
├── hallucination\_checker/       ← Project settings (urls.py, settings.py)
├── hallucination\_app/           ← App logic (views, models, forms, templates)
│   └── templates/
│       └── hallucination\_app/
│           ├── create\_snippet.html
│           └── list\_snippets.html
├── screenshots/
│   ├── create\_entry.png
│   └── view\_entries.png
├── manage.py
└── README.md

````

---

## 📌 Project Overview

This app allows users to submit and view AI-generated code snippets. Its purpose is to simulate traceable AI code submission, such as detecting hallucination risks in secure development workflows.  
While this version supports only Create and Read, it establishes a foundation for future validation, annotation, and risk detection.

---

## 🛠️ Setup & Scaffold

```bash
django-admin startproject hallucination_checker .
python manage.py startapp hallucination_app
````

✅ Registered `hallucination_app` in `INSTALLED_APPS`.

---

## 🧩 Model

```python
from django.db import models

class CodeSnippet(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

## 🌐 Views + URLs

```python
# views.py
from django.shortcuts import render, redirect
from .models import CodeSnippet
from .forms import CodeSnippetForm

def create_snippet(request):
    if request.method == 'POST':
        form = CodeSnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_snippets')
    else:
        form = CodeSnippetForm()
    return render(request, 'hallucination_app/create_snippet.html', {'form': form})

def list_snippets(request):
    snippets = CodeSnippet.objects.all()
    return render(request, 'hallucination_app/list_snippets.html', {'snippets': snippets})
```

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_snippets, name='list_snippets'),
    path('create/', views.create_snippet, name='create_snippet'),
]
```

---

## 🔄 Django Principles

* `models.py` is the **source of truth** for data structure
* Views are **thin controllers**, delegating to forms and templates
* `transaction.atomic()` and `select_for_update()` are reserved for future transactional safety
* Extensible toward validation pipelines and audit trails

---

## 📸 Screenshots

### Create Entry

![Create Entry](screenshots/create_entry.png)

### View Entries

![View Entries](screenshots/view_entries.png)

---

## 🧪 Step-by-Step Setup Guide

### ✅ 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### ✅ 2. Install Django

```bash
pip install django
```

### ✅ 3. Start project and app

```bash
django-admin startproject hallucination_checker .
python manage.py startapp hallucination_app
```

### ✅ 4. Register app

In `hallucination_checker/settings.py`, add:

```python
'hallucination_app',
```

### ✅ 5. Create templates

```bash
mkdir -p hallucination_app/templates/hallucination_app
```

### ✅ 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### ✅ 7. Run the development server

```bash
python manage.py runserver
```

Then visit:

* [http://127.0.0.1:8000/create/](http://127.0.0.1:8000/create/) → Submit snippets
* [http://127.0.0.1:8000/](http://127.0.0.1:8000/) → View all snippets

---

## 🔗 GitHub Repo Links

> *Update these after pushing:*

* [View `models.py`](https://github.com/Mafruha17/CIDM632570/tree/Module1Assignment/hallucination_app/models.py)
* [Full commit history](https://github.com/Mafruha17/CIDM632570/tree/Module1Assignment)

---

## 💡 Reflection

This CRUD MiniLab solidified core Django concepts and reinforced the value of “thin views” and model-driven architecture. While the app is basic, it serves as a scaffold for more complex AI-aware pipelines — such as risk annotation, hallucination detection, and audit trail generation.

It reflects Django-first thinking, modular design, and future readiness.

---


