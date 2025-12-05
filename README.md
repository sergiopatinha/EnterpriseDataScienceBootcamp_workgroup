# Customer Churn Prediction — Enterprise Data Science Bootcamp

## Project Identification
Group project for the course **Big Data Bootcamp - Postgraduate Program in Enterprise Data Science & Analytics**.
Group: EDSB25_20

Members:

Diana Gomes — Student ID: 20240829

Sara Góis — Student ID: 20242129

Sérgio Patinha — Student ID: 20241149

Tiago Franco — Student ID: 20242038

## Project Overview
Customer churn represents a significant risk to recurring revenue businesses. In this project, we build an end-to-end **machine learning system to predict customer churn**, identify its key drivers, and translate predictions into **data-driven retention strategies**.

The core business question is:
> *Can we reliably predict churn early enough to intervene, and how should the business act on it?*

---

## Business Objectives
- Predict which customers are most likely to churn  
- Understand the main behavioral and contractual drivers of churn  
- Suggest targeted, cost-effective retention actions 

---

## Dataset Description

- **Number of customers:** 7,043  
- **Initial features:** 56  
- **Final predictive features:** 31  
- **Target variable:** `st_churn_label` (Yes / No)  
- **Duplicate customers:** None  

---

## Feature Domains
- **Demographics:** gender, age, marital status, dependents  
- **Location:** ZIP code clusters  
- **Services & Subscriptions:** phone, internet, security, streaming, contract type  
- **Billing & Usage:** monthly charges, payment method, data usage  
- **Customer Engagement:** referrals 


## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook

---

## Analytical Workflow
### Data Preparation
- Merging datasets from multiple business domains
- Strict leakage control (all post-churn variables removed)
- Target definition and dataset validation

### Exploratory Data Analysis (EDA)
Key insights discovered:
- Contract type is the strongest churn driver (month-to-month is highest risk)
- Early tenure customers are significantly more likely to churn
- Protection services & referrals reduce churn risk
- High monthly charges & flexible billing increase churn probability

### Feature Engineering
- Binary encoding of service indicators
- Binning of referrals and data usage
- One-hot encoding of contract, payment, and internet type
- Merging streaming services into a single feature
- Geo-clustering using latitude/longitude
- Removal of redundant and multicollinear variables

### Modeling & Evaluation
Models tested:
- Logistic Regression
- Random Forest
- XGBoost (Final selected model)

**Evaluation strategy:**
- 80/20 Train–Test split
- 5-Fold Stratified Cross-Validation
- Primary metric: F1-Score

**Final performance interpretation:**
~70% of true churners detected in advance
Some false positives accepted as business trade-off

### Business Strategy & Impact
Customers are segmented into three action groups:

   🔴 High Risk
   Month-to-month contracts
   High monthly charges
   Short tenure
   Fiber + Unlimited data
   
   Actions:
   Short-term loyalty bonuses
   Contract optimization
   Targeted bundle discounts

   🟠 Medium Risk
   Moderate price
   Some add-ons
   Mid-tenure
   
   Actions:
   Vouchers
   Add-on bundles

   🟢 Low Risk
   Long tenure
   Multiple services
   Referrers
   
   Actions:
   Loyalty programs
   Upselling
   Refer-a-friend incentives
   
   **This turns churn prediction into a direct revenue protection system.**

## Key Takeaways
- Churn is not random — it is strongly driven by business design
- Flexible contracts and early lifecycle stages carry the highest risk
- A predictive system allows proactive, targeted intervention
