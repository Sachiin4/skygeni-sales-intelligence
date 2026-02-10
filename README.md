#Sales Intelligence Decision Engine for identifying win drivers, pipeline risk, and revenue insights.

## Objective

The goal of this project is to investigate why win rates are declining despite a healthy pipeline and to design a lightweight decision intelligence system that helps sales leaders identify risks and improve revenue outcomes.

---

## Business Problem

Although the sales pipeline volume appears healthy, the CRO lacks visibility into:

- Where deals are being lost
- Which segments are underperforming
- What actions can improve conversion

This project focuses on identifying **win rate drivers, risk signals, and revenue intelligence insights**.

---

## Approach

The solution is designed as a simple but practical Sales Intelligence Engine.

### Steps

1. Exploratory Data Analysis (EDA) to understand pipeline behavior  
2. Win Rate Driver Analysis using Logistic Regression  
3. Deal-level win probability scoring  
4. Risk deal detection  
5. Pipeline health measurement using probability-weighted revenue  
6. Automated CRO insight generation

---

## Key Insights

- Overall win rate is ~45%, indicating moderate conversion performance  
- The largest leakage occurs at the **Qualified stage**, suggesting weak early deal qualification  
- Several deals show <40% win probability and require early intervention  
- Revenue is highly concentrated, with ~58% coming from the top 20% of deals  
- Probability-weighted pipeline health is ~0.47, meaning less than half the pipeline is realistically convertible

---

## Decision Engine

A simple interpretable Logistic Regression model is used to:

- Identify win and loss drivers  
- Score each deal with win probability  
- Detect high-risk opportunities  
- Support revenue forecasting using expected revenue

Outputs generated:

- Deal win probabilities
- High-risk deal list
- Pipeline health score
- Segment-level performance insights

---

## Mini System Design

### Architecture

CRM → Data Warehouse → Python Scoring Engine → Insights → Dashboard / Alerts

### How It Works

- Daily pipeline scoring
- Weekly executive review metrics
- Automated identification of risk deals
- Segment-level performance monitoring

---

## If I Were the CRO Tomorrow Morning

1. Tighten qualification criteria since most leakage occurs at the Qualified stage  
2. Review deals with <40% win probability weekly  
3. Focus more on referral and late-stage opportunities  
4. Monitor top 20% high-value deals due to revenue concentration risk  
5. Track probability-weighted pipeline health instead of relying only on raw pipeline size

---

## How to Run the Project

```bash
pip install -r requirements.txt
python src/win_driver_model.py
python src/insight_generator.py
python src/pipeline_health.py
