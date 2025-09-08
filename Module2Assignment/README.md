# CIDM 6325/70 – Electronic Commerce and Web Development

## 🧪 MiniLab – MVP Logistics Platform: AI-Enhanced Perishable Food Delivery

This README outlines the scope, design, setup, and delivery goals for the Minimum Viable Artifact (MVA) of the AI-enhanced perishable food logistics platform. This MVP is structured to be delivered and deployed within a 1–2 week window and will serve as the first tangible deliverable for the CIDM 6325/70 course project.

---

## 📚 Table of Contents
1. [Objective](#objective)  
2. [Technology Stack](#technology-stack)  
3. [Feature Scope (MVP)](#feature-scope-mvp)  
4. [Actors](#actors)  
5. [Core Data Models](#core-data-models)  
6. [Setup Instructions](#setup-instructions)  
7. [Estimated Effort](#estimated-effort)  
8. [Goal](#goal)  
9. [Development Scaffold](#development-scaffold)  
10. [Mock AI Logic](#mock-ai-logic)  
11. [Test Routes](#test-routes)

---

## 🎯 Objective
To demonstrate a prototype of an AI-assisted logistics system that:
- Accepts perishable shipment orders
- Uses a simulated AI engine to generate delivery routes and ETAs
- Visualizes real-time updates for dispatchers and client endpoints

---

## ⚙️ Technology Stack
| Layer        | Tech Used               |
|--------------|-------------------------|
| Front-End    | Bootstrap 5 + HTMX      |
| Back-End     | Django (views, models)  |
| AI Logic     | Python module (mock logic or simple sklearn rule) |
| Database     | SQLite (mock delivery & order data) |
| Deployment   | Localhost (dev server) / Optional: Heroku |

---

## 🔧 Feature Scope (MVP)
| Feature                     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Order Entry UI**          | Form to enter destination, product type, delivery urgency                   |
| **Mock AI Route Planner**   | Simulates best route based on origin/destination matrix                     |
| **ETA Simulation**          | Simulates countdown / updates to user-facing dashboard                      |
| **Warehouse Dashboard**     | Tracks pending shipments, routes, status updates                            |
| **Client Notifications**    | Endpoint-facing view of expected delivery time                              |
| **Audit Log (Optional)**    | Displays how AI made decisions (transparency for MVA phase)                 |

---

## 👥 Actors
- **Warehouse Staff** – Places order, sees routes
- **AI System (Mocked)** – Assigns best-fit route and ETA
- **Driver (Simulated)** – Progress visible through dashboard
- **Client** – Checks delivery status via read-only interface

---

## 🧱 Core Data Models
| Model       | Fields                                                             |
|-------------|---------------------------------------------------------------------|
| `Order`     | `id`, `product_type`, `destination`, `timestamp`, `urgency`       |
| `Route`     | `id`, `origin`, `destination`, `eta_minutes`                      |
| `Delivery`  | `order_id`, `driver_name`, `status`, `ai_rationale`              |

---

## 🛠️ Setup Instructions

1. **Clone the Repo**
```bash
git clone https://github.com/Mafruha17/CIDM632570.git
cd CIDM632570/Module1Assignment
```

2. **Create and Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install Requirements**
```bash
pip install -r requirements.txt
```

4. **Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run Development Server**
```bash
python manage.py runserver
```

6. **Access the App**  
Open your browser to: `http://127.0.0.1:8000/`

---

## ⏱️ Estimated Effort
| Task                          | Hours        |
|-------------------------------|--------------|
| Django project scaffolding     | 2–3 hrs      |
| Model creation + migrations    | 2 hrs        |
| HTMX forms + UI integration    | 3–4 hrs      |
| AI logic simulation            | 2–3 hrs      |
| Frontend layout (Bootstrap)    | 2 hrs        |
| Testing and polish             | 2 hrs        |

**Total Estimate:** 15–17 hours

---

## ✅ Goal
Deliver a working Django app that showcases:
- AI-integrated delivery logic
- Real-time operational transparency
- Strong foundation for further iterations (Part D, Part H)

---

## 🏗️ Development Scaffold

```bash
├── manage.py
├── requirements.txt
├── logistics_app/           # Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
├── logistics_project/       # Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── README.md
```

---

## 🤖 Mock AI Logic
Simple Python module: `ai_engine.py`
```python
def estimate_eta(destination: str, urgency: str) -> int:
    base_eta = 60 if urgency == "normal" else 30
    if "remote" in destination.lower():
        base_eta += 20
    return base_eta

def assign_route(order_id: int) -> str:
    return f"Route-{order_id % 5}"  # Dummy route assignment
```

---

## 🧪 Test Routes

| URL Path             | View Function         | Description                            |
|----------------------|------------------------|----------------------------------------|
| `/orders/new/`       | `create_order_view`    | Form to create new shipment order      |
| `/dashboard/`        | `warehouse_dashboard`  | Displays current orders + statuses     |
| `/client/status/`    | `client_status_view`   | Client-facing status ETA tracker       |
| `/ai/preview/`       | `simulate_ai_decision` | View to show AI decision-making logic  |

These are mapped via `logistics_app/urls.py` and included in `logistics_project/urls.py`

---
