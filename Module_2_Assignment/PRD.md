# Product Requirements Document (PRD)

**Project Title:** AI-Enhanced Perishable Food Supply Platform  
**Course:** CIDM 6325/70 – Electronic Commerce and Web Development  
**Student:** Mafruha Chowdhury  
**Date:** 09/20/2025  

---

## 1. Introduction

### Context & Vision
Perishable food logistics often suffer from static routing, delayed dispatching, and high spoilage rates.  
This project introduces an **AI-enhanced logistics platform** built on Django, HTMX, and Bootstrap to streamline scheduling, routing, and real-time coordination.  

### Problem Statement
Many mid-tier logistics operators still depend on outdated, rule-based scheduling. The lack of adaptable, AI-driven decision support causes waste, inefficiency, and customer dissatisfaction.  

### Goals
- Reduce spoilage through predictive routing.  
- Enhance transparency with real-time tracking.  
- Improve stakeholder coordination across warehouses, airlines, and retailers.  
- Deliver a scalable, ethical, and accessible platform.  

### Traceability Note
This PRD builds directly on the **Module 1 Pitch and MVP** (see `Module_1_Assignment/DOC/Module1_Assignment_PDF.pdf`) by refining its scope into implementation-ready requirements.

---

## 2. Objectives & Success Metrics

- ≥ 20% reduction in spoilage within 6 months.  
- ≥ 30% improvement in on-time deliveries.  
- ≥ 50% reduction in manual dispatcher interventions.  
- Net Promoter Score (NPS) ≥ 8/10 within 3 months.  

---

## 3. Scope

### In Scope
- Regional distribution from warehouses to endpoints.  
- AI-assisted routing and ETA predictions.  
- CRUD-based order and inventory management.  
- HTMX-enabled real-time dashboard updates.  

### Out of Scope
- Global supply chain optimization.  
- AI-driven demand forecasting.  
- Farm-to-warehouse procurement logic.  

---

## 4. User Stories & Use Cases

- **As a warehouse operator**, I want to input shipments so that routes are optimized automatically.  
- **As a driver**, I want dynamic ETAs so I can adapt to traffic or delays.  
- **As a catering manager**, I want real-time delivery updates so I can adjust meal prep schedules.  
- **As a compliance auditor**, I want decision logs so I can validate fairness and traceability.  

### Edge Cases & Constraints
- Reroutes due to weather or traffic.  
- Handling expired or rejected inventory.  
- Fail-safe routing when AI confidence is low.  

---

## 5. Functional Requirements

- **Must Have**  
  - User login/logout (Django authentication).  
  - CRUD for shipments, orders, and deliveries.  
  - AI-based route generation with fallback logic.  
  - Real-time ETA dashboard updates.  

- **Should Have**  
  - Role-based permissions (admin, dispatcher, driver).  
  - Inline edits and live search (HTMX).  

- **Could Have**  
  - CI/CD demo pipeline.  
  - Public-facing dashboard.  

---

## 6. Non-Functional Requirements

- **Performance:** Routes generated in <2 seconds for 100 orders.  
- **Accessibility:** WCAG 2.2 compliance, ARIA roles, screen reader support.  
- **Security:** RBAC, encryption in transit and at rest, ISO 27001-K alignment.  
- **Compliance:** NIST AI RMF and IEEE P7003 fairness guidelines.  
- **Scalability:** Handle 10,000+ deliveries/day with minimal reconfiguration.  

---

## 7. Dependencies & Risks

### Dependencies
- Django, HTMX, Bootstrap, SQLite (initial phase).  
- Potential APIs for mapping/traffic data.  

### Risks & Mitigation
- **AI Reliability:** Outdated data → Validate + fallback rules.  
- **Bias in Routing:** Favoring large clients → Apply fairness rules + audits.  
- **Data Privacy:** Metadata leaks → Encrypt + RBAC.  
- **Over-automation:** Dispatcher bypass → Keep human-in-the-loop.  
- **Vendor Lock-in:** Proprietary APIs → Use modular abstraction layers.  

---

## 8. Acceptance Criteria (Expanded)

- [ ] User can log in and log out successfully (tested with Django auth).  
- [ ] Warehouse operator can create, edit, and delete shipments in CRUD interface.  
- [ ] Driver ETAs display and update dynamically via HTMX.  
## 8. Acceptance Criteria (Expanded)

- [ ] User can log in and log out successfully (Django auth).  
- [ ] Warehouse operator can create, edit, and delete shipments in CRUD interface.  
- [ ] Driver ETAs display and update dynamically via HTMX.  
- [ ] Orders can be **created, updated, and deleted** in both web UI and Admin portal.  
- [ ] Accessibility confirmed with screen reader and keyboard navigation.  
- [ ] AI decision logs are generated for each ETA prediction and stored securely.  
- [ ] Role-based permissions prevent unauthorized CRUD operations.  
- [ ] Repo contains `AI_LOG.md` and `ETHICS.md` with transparent documentation.  


---

## 9. References

- McKinsey Report on AI in Food Logistics (2024).  
- NIST AI Risk Management Framework (AI RMF 1.0, 2023).  
- IEEE P7003 – Algorithmic Bias Considerations.  
- ISO/IEC 27001-K – Security Controls.  
- WCAG 2.2 – Accessibility Guidelines.  

---
