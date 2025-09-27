# 📦 Module 3 – CIDM 6325: Form Validation + Multi-Model Design

**Author:** Mafruha Chowdhury  
**Course:** CIDM 6325 – Electronic Commerce (Fall 2025)  
**Focus:** AI-assisted form validation, multi-model design, and accessibility

---

## 🔍 Overview

This module extends the logistics delivery app built in Module 2 by implementing:

- Custom form validation (`OrderForm`)
- Auto-generated `order_id` (e.g., `ORD-1A2B3C`)
- ETA estimation using mock AI logic
- A new `Customer` model (One-to-Many with Orders)
- Bootstrap-styled, accessible forms
- HTMX-compatible form structure
- Admin interface for both models

---

## ✅ Completed Features – Part A: Forms & Validation

### 🧪 Validation Logic

Implemented in `forms.py`:

- `clean_order_date`: Prevents orders dated in the past
- `clean()`: Prevents client type from being embedded in delivery location
- `order_id`: Auto-generated in `Order.save()` method
- User-friendly error messages using Bootstrap + ARIA
- WCAG 2.2–aligned form layout

---

## 🧩 Multi-Model Design – Part B

- `Customer` model added with `One-to-Many` relationship
- Linked via foreign key in the `Order` model
- Fully functional in admin and form
- Tested with real CRUD scenarios

---

## 🧪 CRUD Verification

| Scenario                             | Result        |
| ------------------------------------ | ------------- |
| Create Order via Form                | ✅ Works       |
| View Orders List                     | ✅ Works       |
| Update Order via Admin               | ✅ Works       |
| Delete Order via Admin               | ✅ Works       |
| Validation for Past Date             | ✅ Error shown |
| Validation for Duplicate Client Type | ✅ Error shown |
| Required Field: Customer             | ✅ Error shown |

---

## 📁 Key Files

- `models.py`: Defines `Order`, `Customer`
- `forms.py`: Custom `OrderForm` with validations
- `views.py`: Full CRUD support
- `order_form.html`: Bootstrap + accessible
- `AI_LOG.md`: Prompt log and design decisions
- `README.md`: This documentation

---

## 🤖 AI Use Summary

AI assistance included:

- Auto-ID generation logic (`ORD-XXXXXX`)
- ETA field mock generation
- Validation rule suggestions
- UX guidance for error display and form layout
- Accessibility checks (ARIA roles, WCAG alignment)

---

## 🧠 Ethical & Accessibility Reflection

This module emphasized both technical correctness and responsible design:

- All validation messages were tested for clarity and user dignity.
- ARIA roles and label-input linking were used for screen reader compatibility.
- Auto-generated IDs reduced user input risk.
- Every AI-suggested code block was manually reviewed and adjusted for business fit, usability, and ethical clarity.

---

## 📐 Schema Diagram

![Schema Diagram – Customer to Order](image-1.png)

---

## 📦 `requirements.txt`

```txt
Django>=4.2,<5.0
django-htmx>=1.15.0
