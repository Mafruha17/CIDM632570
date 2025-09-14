
##  Mafruha Chowdhury 
 CIDM 6325-70\
West Texas A&M University

---
# AI-Powered Delivery Order Management System (Django + HTMX)


## Overview

This project is a lightweight web-based **Supply Chain Order Management System** tailored for **perishable food logistics**. It leverages **Django**, **HTMX**, and **Bootstrap** to enable users to create, view, update, and delete delivery orders with real-time ETA predictions.

While the current ETA calculation uses a mock function, the architecture is designed to support integration with real machine learning models or external APIs.

---
## Features

* 📦 **Create new delivery orders** with key metadata
* 📋 **View all existing orders** in a tabular format
* ✏️ **Edit orders inline** using HTMX partial updates
* ❌ **Delete orders** with confirmation modal
* 🤖 **Mock AI ETA logic** to simulate delivery time estimation
* 🎨 Clean Bootstrap-styled forms and tables
* ⚡ Fully **asynchronous updates** with HTMX (no page reloads)
-  **HTMX-enhanced dynamic** order form with real-time ETA mock logic.
- Bootstrap-styled UI for **responsive form input and table views**.
- CRUD interface for order management with AJAX **interactivity.**
- Django Admin panel enabled for backend data storage and model manag
---
## Tech Stack

| Layer         | Technology             |
| ------------- | ---------------------- |
| Backend       | Django (v4.2)          |
| Frontend      | Bootstrap 5            |
| Interactivity | HTMX                   |
| AI Logic      | Mock function (Python) |
| DB            | SQLite (default)       |

---

## 📑 Table of Contents

* [🌱 Overview: Perishable Food Logistics Use Case](#-overview-perishable-food-logistics-use-case)
* [🔧 Features Implemented](#-features-implemented)
* [🧠 AI Integration (Planned)](#-ai-integration-planned)
* [✅ Completed Functionality](#-completed-functionality-as-of-module-2-submission)
* [🤖 ETA Mock Logic](#-eta-mock-logic)
* [🚫 Controlled Fields](#-controlled-fields)
* [📂 Routes Implemented](#-routes-implemented)
* [📁 Directory Structure](#-directory-structure)
* [🚀 Usage](#-usage)
* [✅ Manual Testing Checklist](#-Manual-Testing-Checklist)
* [ Sample Screenshots](#-Sample-Screenshots)
* [💡 Notes for Review](#-notes-for-review)
* [📌 Next Steps (Optional Enhancements)](#-next-steps-optional-enhancements)

---
## 🌱 Overview: Perishable Food Logistics Use Case

This application simulates an internal logistics tracking system for a company that delivers **perishable goods** such as:

* Fresh produce (fruits, vegetables)
* Dairy and refrigerated items
* Pre-packaged meal kits or temperature-sensitive products

The tool enables:

* Time-sensitive order placement and routing
* Mock AI-generated ETA predictions for dynamic scheduling
* Lightweight CRUD operations with live updates
* Audit-compliant tracking with immutable fields like `order_id`

Designed for **logistics managers** and **supply coordinators**, this MVP platform provides agility, speed, and future AI-readiness.

---

## 🔧 Features Implemented

### ✅ Core Functionality

* **Order Creation Form**

  * Users can create new orders via a Bootstrap-styled form.
  * ETA is dynamically generated using a placeholder AI function `calculate_eta_mock()`.

* **HTMX-Enhanced Order List View**

  * Displays all submitted orders in a dynamic HTML table.
  * Includes real-time Edit/Delete actions via HTMX without full-page reloads.

* **Edit Order**

  * Orders can be updated using a pre-filled form.
  * `Order ID` field is **read-only** during updates to preserve audit integrity.

* **Delete Order**

  * Orders can be removed via HTMX-enabled confirmation and refresh.

* **ETA Field**

  * Each order includes an `ETA` field generated at creation time.
  * This value is produced by a mock AI function (`calculate_eta_mock`) and will be replaced with actual AI logic in a later sprint.

---


## 🧠 AI Integration (Planned)

* Current ETA logic uses `calculate_eta_mock(order)` from [`ai_engine.py`](logistics_project/logistics_app/ai_engine.py).
* This mock function simulates ETA prediction and is used as a placeholder.
* Future iterations will integrate **real AI/ML logic or an external API** to calculate delivery ETA based on input parameters (e.g., location, client type).

---

## ✅ Completed Functionality (as of Module 2 Submission)

| Feature        | Status     | Notes                                                             |
| -------------- | ---------- | ----------------------------------------------------------------- |
| Order Creation | ✅ Complete | Uses Bootstrap-styled form and HTMX for dynamic entry             |
| Order Listing  | ✅ Complete | Table view with Edit/Delete buttons per entry                     |
| Order Edit     | ✅ Complete | HTMX-powered form, retains `order_id` as read-only                |
| Order Delete   | ✅ Complete | Confirmation prompt before deletion; seamless UI removal via HTMX |
| ETA Prediction | ✅ Complete | Uses `calculate_eta_mock()` as placeholder for AI logic           |

---

## 🤖 ETA Mock Logic

For the MVA (minimum viable artifact), the project uses a mocked AI engine:
ETA is currently simulated using a function in `ai_engine.py`:

```python
# logistics_app/ai_engine.py
from datetime import timedelta, date

def calculate_eta_mock(order):
    return date.today() + timedelta(days=3)
```

This placeholder can later be replaced by:

* A trained ML regression model
* External logistics APIs (e.g., Google Maps ETA, Route Optimization tools)
* Real-time traffic/weather integration

---

## 🚫 Controlled Fields

* `order_id` is read-only during updates to preserve audit integrity.
* Form logic dynamically sets `readonly=True` during edit operations via `OrderForm(read_only=True)`.

---

## 📂 Routes Implemented

| URL Path              | View           | Description                    |
| --------------------- | -------------- | ------------------------------ |
| `/`                   | `index`        | Landing page with initial form |
| `/predict/`           | `predict_eta`  | Returns mocked ETA text        |
| `/order/create/`      | `order_create` | Form to create new orders      |
| `/orders/`            | `order_list`   | Table view of existing orders  |
| `/order/update/<pk>/` | `order_update` | Edit form for an order (HTMX)  |
| `/order/delete/<pk>/` | `order_delete` | Confirmation and deletion flow |

---

## 📁 Directory Structure

## Project Structure (with clickable links)

- [manage.py](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/manage.py)
- logistics_project/
  - logistics_app/
    - [forms.py](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/logistics_app/forms.py)
    - [models.py](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/logistics_app/models.py)
    - [views.py](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/logistics_app/views.py)
    - [urls.py](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/logistics_app/urls.py)
    - [ai_engine.py](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/logistics_app/ai_engine.py) ← ETA logic (mock placeholder)
    - templates/logistics_app/
      - [order_form.html](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/logistics_app/templates/logistics_app/order_form.html)
      - [order_list.html](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/logistics_app/templates/logistics_app/order_list.html)
      - [order_confirm_delete.html](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/logistics_app/templates/logistics_app/order_confirm_delete.html)


---

## 🚀 Usage

1. **Start server:**

```bash
python manage.py runserver
```

2. **Access application:**

* Home page with form: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Orders list: [http://127.0.0.1:8000/orders/](http://127.0.0.1:8000/orders/)
* Create new order: [http://127.0.0.1:8000/order/create/](http://127.0.0.1:8000/order/create/)

3. **Admin panel (optional):**

```bash
python manage.py createsuperuser
```

---

## 💡 Notes for Review

* HTMX is used for **seamless form interaction** and table row updates.
* Form styling is handled via **Bootstrap 5**.
* **Order ID is immutable once created**.
* All views and URLs follow Django's clean separation of concerns.
* **Code and logic were committed to the `Module2Assignment` branch**, and are fully functional as of `Sept 13, 2025`.

---
## ✅ Manual Testing Checklist
---
| Test Case ID | Feature Area         | Test Description                                                        | Expected Result                                                | Status |
| ------------ | -------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------- | ------ |
| TC-001       | Home Page            | Access `/` URL                                                          | Form loads with all input fields                               | ✅      |
| TC-002       | Create Order (Valid) | Fill in all required fields and submit                                  | Order is saved and redirected to `/orders/`                    | ✅      |
| TC-003       | Create Order (Empty) | Submit form with no input                                               | Validation errors are displayed                                | ✅      |
| TC-004       | Order List Display   | Visit `/orders/`                                                        | Orders are listed in descending order with Edit/Delete buttons | ✅      |
| TC-005       | ETA Display          | Create order and view in list                                           | Mock ETA is shown for each order                               | ✅      |
| TC-006       | Edit Order           | Click "Edit", change delivery location, submit                          | Order updates, remains in list with new values                 | ✅      |
| TC-007       | Edit Order ID        | Attempt to change `Order ID` during edit                                | `Order ID` field is read-only and uneditable                   | ✅      |
| TC-008       | Delete Order         | Click "Delete", confirm deletion                                        | Order is removed from list                                     | ✅      |
| TC-009       | Invalid Order URL    | Access `/orders/999/edit/` for non-existent order                       | 404 error or friendly error shown                              | ✅      |
| TC-010       | Form Styling         | Verify all fields use Bootstrap styling (`form-control`, spacing, etc.) | Clean and responsive layout                                    | ✅      |
| TC-011       | Admin Panel          | Login to `/admin/` and view/edit orders                                 | Admin interface works and displays same data                   | ✅      |
| TC-012       | Git Sync             | Check remote GitHub repository after push                               | All latest code and files are committed and visible on GitHub  | ✅      |


---

## Sample Screenshots

> ![Create new order](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/doc/adding_order)
> ![Orders](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/doc/Orders.png)
> ![Edit Order](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/doc/EditOrders.png)
> ![Delete Order](https://github.com/Mafruha17/CIDM632570/blob/Module2Assignment/Module2Assignment/doc/DeleteOrder.png)
> 
---
## Future Work

* Replace mock ETA with actual AI/ML logic
* Add user authentication
* Add order filtering by date, client, location
* Export orders to Excel or PDF
* Improve accessibility and mobile responsiveness


## 📌 Next Steps (Optional Enhancements)

* Replace `calculate_eta_mock()` with:

  * A trained ML model
  * Or a REST API call to an external prediction service
* Add filtering/search to the order table
* Implement pagination
* Add audit logging for update/delete events


## License
This project is for academic purposes and internal demo only. No commercial use permitted.
