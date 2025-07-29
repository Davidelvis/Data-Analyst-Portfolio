import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()
random.seed(42)

# Setup
NUM_PARTNERSHIPS = 20
OUTPUT_DIR = "/home/david/Projects/Portfolio/Data-Analyst-Portfolio"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Constants
COUNTRIES = ["Kenya", "Uganda", "Nigeria", "India", "Bangladesh", "Philippines"]
PARTNER_TYPES = ["NGO", "Gov Health Dept", "Clinic Network", "University", "Startup"]
THEMES = ["trust", "awareness", "community mobilisation", "access", "acceptance"]
SKILLS = ["BP measurement", "HPV screening", "Visual inspection", "Counselling", "Data entry"]

# 1. Partnerships Table
partnerships = []
for i in range(1, NUM_PARTNERSHIPS + 1):
    partnerships.append({
        "partnership_id": f"P{i:03}",
        "partner_name": fake.company(),
        "country": random.choice(COUNTRIES),
        "partner_type": random.choice(PARTNER_TYPES),
        "start_date": fake.date_between(start_date="-2y", end_date="-1y"),
        "lead_contact": fake.name(),
    })
df_partners = pd.DataFrame(partnerships)
df_partners.to_csv(f"{OUTPUT_DIR}/partnerships.csv", index=False)

# 2. Impact Metrics Table
impact_metrics = []
for p in df_partners["partnership_id"]:
    for month in pd.date_range("2023-01-01", "2024-12-01", freq="MS"):
        impact_metrics.append({
            "partnership_id": p,
            "report_month": month.strftime("%Y-%m"),
            "women_screened": random.randint(50, 800),
            "health_workers_trained": random.randint(2, 25),
            "skills_demonstrated": random.sample(SKILLS, k=random.randint(1, 3))
        })
df_impact = pd.DataFrame(impact_metrics)
df_impact["skills_demonstrated"] = df_impact["skills_demonstrated"].apply(lambda x: ", ".join(x))
df_impact.to_csv(f"{OUTPUT_DIR}/impact_metrics.csv", index=False)

# 3. Delivery Milestones Table
deliveries = []
for p in df_partners["partnership_id"]:
    for m in range(1, 5):
        planned = fake.date_between(start_date="-1y", end_date="today")
        actual = planned + timedelta(days=random.randint(-5, 20))
        deliveries.append({
            "partnership_id": p,
            "milestone": f"Milestone {m}",
            "planned_date": planned,
            "actual_date": actual,
            "status": "On Track" if abs((actual - planned).days) <= 7 else "Delayed"
        })
df_deliveries = pd.DataFrame(deliveries)
df_deliveries.to_csv(f"{OUTPUT_DIR}/deliveries.csv", index=False)

# 4. Qualitative Feedback Table
feedback = []
for p in df_partners["partnership_id"]:
    for _ in range(3):
        theme = random.sample(THEMES, k=2)
        feedback.append({
            "partnership_id": p,
            "submission_date": fake.date_between(start_date="-6M", end_date="today"),
            "feedback_text": fake.paragraph(nb_sentences=4),
            "themes": ", ".join(theme)
        })
df_feedback = pd.DataFrame(feedback)
df_feedback.to_csv(f"{OUTPUT_DIR}/feedback.csv", index=False)

print(f"✅ Sample data generated in: {OUTPUT_DIR}")
