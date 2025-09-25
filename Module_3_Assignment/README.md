
##  Mafruha Chowdhury 
 CIDM 6325-70\
West Texas A&M University

---
# 📦 Module 3 Assignment – CIDM 6325 (Fall 2025)

## 🔍 Overview
This module builds upon the logistics delivery order system implemented in Module 2. It focuses on:

- 🧠 AI-assisted form and model design
- 🧾 Custom form validation
- 🆔 Auto-generated Order IDs
- 🔁 Multi-model relationships (in progress)
- 🎯 Accessibility and ethical reflection

---

## ✅ Completed Features – Part A: Forms & Validation

### 🔧 Auto-Generated Order ID
- Format: `ORD-XXXXXX` (alphanumeric, UUID-based)
- Assigned automatically in `Order` model via `save()` override
- Not editable by user

### 🧪 Validation Logic
Implemented in `forms.py`:
- `clean_order_date`: Prevents past-dated orders
- `clean()`: Ensures `client_type` isn’t embedded in `delivery_location`

### 💡 HTMX Form Handling
- Live form submission with error feedback
- Success alert displays `order_id` and `eta`

### ♿ Accessibility Notes
- ARIA roles (`aria-live`)
- Label linking via `id_for_label`
- Bootstrap classes for clarity and spacing

---

## 📌 In Progress – Part B: Multi-Model Design
- Adding `Customer` model (One-to-Many)
- Optional: `Tag` model (Many-to-Many with Orders)
- Schema diagram + migration documentation
- Use-case assumptions for business/analytics

---

## 📁 Key Files

```text
├── logistics_project/
│   └── settings.py, urls.py
├── logistics_app/
│   ├── models.py           # Auto-ID + ETA logic
│   ├── forms.py            # Custom validation
│   ├── views.py            # HTMX-aware form handling
│   ├── templates/
│   │   └── logistics_app/
│   │       ├── order_form.html  # Bootstrap + accessibility
│   │       └── order_list.html
│   └── ai_engine.py        # calculate_eta_mock()
├── db.sqlite3              # Dev DB (can be reset)
├── manage.py
└── README.md (this file)
