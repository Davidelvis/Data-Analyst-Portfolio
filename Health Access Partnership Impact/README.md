# 📊 Health Access Partnership Impact — End-to-End Data Analytics Workflow

This project simulates a real-world analytics workflow for a **global health partnership program**, focused on improving access to screening, training, and healthcare delivery in underserved regions.

It demonstrates the full journey from **raw impact reporting (CSV/Google Sheets)** to **automated, visual insights** using **BigQuery**, **dbt**, and **Looker Studio**, with automation powered by **Google Apps Script** and **Cloud Scheduler**.

---

## 🎯 The Goal

Transform **unstructured and semi-structured health impact data** into clear, visual insights — tracking key program metrics such as:

- 👩‍⚕️ Number of women screened  
- 🧑🏽‍🏫 Health workers trained & competency demonstrated  
- 📦 Delivery milestones & timelines  
- 🗣️ Qualitative narratives on community impact  

---

## 🛠️ Tech Stack

`Google Sheets` · `BigQuery` · `dbt` · `Looker Studio` · `Python` · `Google Apps Script` · `Cloud Scheduler`

---

## ⚙️ How It Works

This project follows a full-stack analytics pipeline — from ingestion to transformation and reporting.

---

### 1. 📥 Ingest & Standardise Data

Impact data is collected from local partners and logged in **Google Sheets**, including:

- Text-based milestone updates  
- Planned vs actual delivery timelines  
- Quantitative metrics and qualitative feedback  

**Google Apps Script** is used to automatically clean, standardise, and push this data into **BigQuery** staging tables.

🔧 Key processing steps:
- Data reshaping & pivoting  
- Text cleaning (e.g. NLP keyword extraction)  
- Timestamping & change tracking  

---

### 2. 🗃️ Load & Structure Data in BigQuery

Structured staging tables are created in **BigQuery**, providing a scalable foundation for transformation.

Tables include:
- `partnership_info`  
- `impact_metrics`  
- `qualitative_feedback`  
- `milestone_tracker`  

---

### 3. 🧱 Transform with dbt

All modeling is handled using **dbt**, applying a modular and layered approach:

- `dim_partnership`: Partner, country, and thematic area  
- `fact_impact`: Number of women screened, trained, deliveries  
- `dim_date`: Reporting periods  
- `fact_feedback`: Partner feedback, sentiment, keyword tagging  

📁 dbt architecture:

Sources → Models → Data Marts

Includes tests, documentation, and auto-generated dbt docs.

---

### 4. ⏱️ Automated Pipeline Refresh

- **Google Apps Script** with triggers: Daily data sync from Google Sheets to BigQuery  
- **dbt Cloud Job**: Scheduled post-load transformations  
- **Cloud Scheduler** *(optional)*: Coordination of cloud workflows  

---

### 5. 📊 Insights & Dashboards (Looker Studio)

Dashboards built in **Looker Studio**, directly connected to **BigQuery**, provide actionable insight.

#### 🧭 Topline Impact View
- Women screened  
- Health workers trained  
- Delivery status (planned vs actual)  
- Country- and partner-level comparisons  

#### 💬 Qualitative Analysis
- Keyword cloud from free-text  
- Theme clustering (e.g. trust, access, community mobilisation)  

#### 🧑‍⚕️ Partner Detail Pages
- Partnership-specific dashboards  
- Milestone completion tracking  
- Upload history and performance summary  

➡️ All dashboards auto-refresh with the latest data.

---

## 📁 Folder Structure

📦 health-impact-analytics
┣ 📁 apps_script/
┃ ┗ ingest.gs
┣ 📁 dbt_project/
┃ ┣ models/
┃ ┗ dbt_project.yml
┣ 📁 google_sheets/
┃ ┗ example_template.xlsx
┣ 📁 dashboards/
┃ ┗ impact_summary.report
┗ README.md


---

## ✅ Notes

This project uses **anonymised and synthetic data** to simulate real-world health access programs. The architecture mirrors actual workflows I’ve built under NDA, demonstrating how I approach:

- Data modeling  
- Workflow automation  
- Dashboard design  
- Insight generation at scale  

---

## 💬 Contact

- **LinkedIn**: [Your LinkedIn]  
- **Portfolio Site**: [Your Portfolio Site]  
- **Email**: [Your Email]  

---

> Thank you for reviewing this showcase!
