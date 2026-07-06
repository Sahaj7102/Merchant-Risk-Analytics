# Merchant Risk Analytics

An end-to-end FinTech analytics project that transforms over **6.3 million payment transactions** into merchant-level risk intelligence using PostgreSQL, SQL, Python, and Power BI.

---

## 📌 Project Overview

Financial institutions process millions of transactions every day, making it difficult to identify merchants with abnormal transaction behaviour or elevated fraud exposure.

This project builds a merchant-centric analytics pipeline that aggregates raw transaction data into actionable business metrics, enabling fraud monitoring, operational reporting, and executive decision-making.

---

## 🎯 Objectives

- Build a scalable PostgreSQL analytics pipeline.
- Engineer merchant-level features from raw transactions.
- Identify high-risk merchants using fraud metrics.
- Develop executive dashboards for fraud monitoring.
- Create a production-quality analytics portfolio project.

---

## Dataset

- **Dataset:** PaySim Mobile Money Transactions
- **Records:** 6,362,620+
- **Domain:** FinTech / Digital Payments
- **Source:** Kaggle

---

## Tech Stack

- PostgreSQL
- SQL
- Python
- Power BI
- Git & GitHub

---

## Project Roadmap

- ✅ Phase 1 – Database Profiling & Environment Setup
- ✅ Phase 2 – Schema Verification & Data Mapping
- 🚧 Phase 3 – Feature Engineering & Aggregation
- ⏳ Phase 4 – Risk Tiering & Metric Layering
- ⏳ Phase 5 – Dashboard Visualization & Guardrail Analytics

---

## Repository Structure

```
Merchant-Risk-Analytics
│
├── sql/
├── docs/
├── python/
├── powerbi/
├── data/
└── README.md
```

---

##  Current Status

### Completed
- ✅ Phase 1 – Database Profiling & Environment Setup
- ✅ Phase 2 – Schema Verification & Data Mapping

### In Progress
- Phase 3 – Feature Engineering & Aggregation

### Key Findings

- Verified the source and destination schemas.
- Confirmed that merchant destinations (`nameDest`) are represented by IDs prefixed with `M`.
- Discovered that merchant entities in the PaySim dataset are highly sparse, with most merchants appearing only once.
- Identified a potential limitation in using PaySim for merchant-level behavioral analytics, which will be evaluated before proceeding with feature engineering.

> **Note:** Data validation is an essential part of analytics. Understanding dataset limitations before building models ensures the final solution reflects real-world behavior rather than assumptions.