
# 📦 Module 3 – CIDM 6325: Form Validation + Multi-Model Design

**Author:** Mafruha Chowdhury  
**Course:** CIDM 6325 – Electronic Commerce (Fall 2025)  
**Focus:** AI-assisted form validation, multi-model design, and accessibility

---

## 🔍 Overview

This module extends the logistics delivery app built in Module 2 by implementing:

- `OrderForm` with custom validation
- Auto-generated `order_id` (e.g., `ORD-1A2B3C`)
- ETA estimation (mock AI logic)
- A new `Customer` model (One-to-Many with Orders)
- Accessible, Bootstrap-styled form
- HTMX compatibility
- Admin interface for both models

---

## ✅ Completed Features – Part A

### 🧪 Validation & UX

- `clean_order_date`: prevents past-dated orders
- `clean()`: blocks client type from appearing in delivery location
- Auto-generates `order_id` inside `Order.save()`
- Custom error messages with ARIA + Bootstrap
- WCAG 2.2–compliant form display

---

## 🧩 Multi-Model Design – Part B

- `Customer` model added
- One customer → many orders
- Foreign key relationship tested
- Visual schema diagram embedded below

---

## 🧪 CRUD Verification

- ✅ Create Order (Form + Admin)
- ✅ Read Orders List
- ✅ Update via Admin
- ✅ Delete via Admin
- ✅ Validations enforced in form

---

## 📁 Key Files

- `models.py`: `Order`, `Customer`
- `forms.py`: `OrderForm` with validation
- `views.py`: Full CRUD
- `order_form.html`: Accessible, HTMX-compatible
- `AI_LOG.md`: Prompt log + decisions
- `README.md`: This file

---

## 🤖 AI Used For

- Auto-ID and ETA logic
- Form validation and error UX
- Bootstrap layout and accessibility best practices
- Debugging and logic cleanup


---

## 🧠 Ethical & Accessibility Note


---

This module emphasized not just technical function, but also ethical and accessible design. Field validation and error visibility were tested using both Bootstrap alerts and screen reader-compatible markup.All code was reviewed for ethical implications (e.g., no exposed fields, respectful errors), and all forms include ARIA attributes and field-label associations for assistive technologies.

 Decisions like removing editable order IDs helped reduce user input errors. Prompts were crafted to reflect on what AI should generate vs. what the developer must verify manually.

---

## 📐 Visual Schema Diagram

![Schema Diagram – Customer to Order](image-1.png)

---

## 📦 requirements.txt

```txt
Django>=4.2,<5.0
django-htmx>=1.15.0
````

> Run `pip install -r requirements.txt` to set up the project.

---

## 🚀 How to Run This App

```bash
# Setup
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt

# Run server
python manage.py migrate
python manage.py runserver
```

---
| Scenario                             | Result        |
| ------------------------------------ | ------------- |
| Create Order via Form                | ✅ Works       |
| View Orders List                     | ✅ Works       |
| Update Order via Admin               | ✅ Works       |
| Delete Order via Admin               | ✅ Works       |
| Validation for Past Date             | ✅ Error shown |
| Validation for Duplicate Client Type | ✅ Error shown |
| Required Field: Customer             | ✅ Error shown |
