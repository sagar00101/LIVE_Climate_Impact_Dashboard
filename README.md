# LIVE_Climate_Impact_Dashboard
# 🌍 Maharashtra Live Climate & Air Quality Impact Tracker

An automated end-to-end data pipeline and real-time analytics dashboard monitoring climate and air quality metrics across key agro-climatic zones in Maharashtra, India.

---

## 🔗 Live Demo
👉 **[View the Live Interactive Dashboard Here](https://liveclimateimpactdashboard-w7amztv6dgujbh9jezywbj.streamlit.app/)** 

---

## 📌 Project Overview
Static climate reports often miss localized anomalies. This project provides:
- **Continuous Live Data Ingestion:** Automated fetching of telemetry using Open-Meteo REST APIs.
- **Multi-Zone Tracking:** Real-time data from 5 major regions:
  - **Mumbai** (Coastal)
  - **Pune** (Western Plateau)
  - **Nagpur** (Vidarbha)
  - **Nashik** (North Maharashtra)
  - **Chhatrapati Sambhajinagar** (Marathwada)
- **Zero-Maintenance Automation:** Hourly cloud cron jobs that collect, transform, and persist records.

---

## 🛠️ Architecture & Tech Stack

```text
[Open-Meteo API] 
       │
       ▼ (Hourly REST API Call)
[GitHub Actions (CRON)] ──> [fetch_data.py] ──> [maharashtra_climate_live_data.csv]
                                                               │
                                                               ▼
                                                    [Streamlit Cloud Dashboard]
