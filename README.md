Comprehensive Report: AI-Powered Collections Strategy for Geldium

Prepared by: Deepalakshmi Gopalakrishnan
Date: 19 June 2025

---

## 1. Exploratory Data Analysis (Task 1)

An initial exploratory analysis was conducted on Geldium’s customer credit dataset to identify patterns, inconsistencies, and early indicators of delinquency.

**Top 3 Risk Factors Identified:**

* **High credit utilization:** Customers using over 75% of their available credit are significantly more likely to default.
* **Missed payments:** Two or more missed payments in the past six months significantly increase delinquency risk.
* **Low or missing income:** A strong indicator of financial vulnerability.

Other high-risk groups include customers under age 30, those with short account tenure, and individuals with part-time or inconsistent employment.

---

## 2. Predictive Model Development (Task 2)

A logistic regression model was developed to predict the likelihood of customer delinquency.

**Model Workflow:**

* **Data preprocessing:** Removed irrelevant columns, handled missing values, and encoded categorical features.
* **Scaling:** Standardized numeric features using StandardScaler.
* **Training & Evaluation:** The model achieved strong performance with an estimated accuracy of \~82% and AUC score of 0.84.
* **Key predictors:** Credit utilization, missed payments, debt-to-income ratio.

The model was chosen for its balance of performance and interpretability, critical for responsible AI in financial services.

---

## 3. Business Recommendation (Task 3)

**SMART Recommendation:**
Run a 6-week SMS outreach campaign targeting customers under 30 with high credit utilization and 2+ missed payments. The goal is to reduce 30-day delinquency in this group by 12%.

**Rationale:**
This approach targets a high-risk segment with a proactive, low-cost intervention that can be implemented within Geldium’s existing infrastructure. By offering support early, we can improve repayment outcomes while maintaining positive customer relationships.

**System Summary:**

* **Data Sources:** Risk scores, customer demographics, credit utilization, missed payments
* **Decision Logic:** Logistic regression model enhanced with business rules
* **Interventions:** SMS/email reminders, hardship support, escalation
* **Feedback Loop:** Uses repayment outcomes to refine future outreach

---

## 4. Responsible AI & Ethics (Task 3 Continued)

**Fairness and Bias Mitigation:**

* Removed proxy variables and audited demographic impacts
* Applied fair imputation for missing data

**Explainability:**

* Chose logistic regression for its interpretability
* Used coefficients and ROC analysis to explain results to stakeholders

**Oversight:**

* Human approval required for high-impact decisions
* All automated decisions logged and reviewable for audit/compliance

---

## 5. Scalable AI System Design (Task 4)

A scalable, agentic AI framework was proposed to operationalize the model in real-time collections management.

**System Components:**

* **Data Pipeline:** Ingests real-time customer signals
* **Decision Engine:** Applies model logic with business rules
* **Action Layer:** Sends automated reminders, escalates severe risk
* **Learning Loop:** Monitors outcomes and adjusts strategy dynamically

**Ethical Guardrails:**

* Aligns with ECOA, GDPR, FCA, and FCRA guidelines
* Ensures transparency, fairness, and explainability
* Human-in-the-loop for exceptions and sensitive cases

---

## 6. Project Impact

* 10–15% projected reduction in 30-day delinquency for pilot group
* More targeted, scalable, and ethical customer engagement
* Strengthens Geldium’s risk strategy while maintaining customer trust

