Main machine learning model for Loantap:- 
# LoanTap Credit-Risk Pipeline 💳

An end-to-end proof-of-concept for predicting loan defaults using **Logistic Regression, SMOTE, and class-weighting**.

---

## 🚀 Project Overview
- Built a binary classifier to flag **“Charged Off”** loans vs **“Fully Paid.”**
- 370K+ cleaned records, 22 engineered features (borrower profile, credit history, loan terms).
- Tackled severe class imbalance (80:20) with **SMOTE & custom weights**.
- Tuned for **F1-score on defaulters (minority class)** rather than raw accuracy.

---

## 🛠️ Tech Stack
- Python  
- pandas  
- scikit-learn  
- imbalanced-learn  
- category_encoders  
- statsmodels  
- seaborn  
- matplotlib  

---

## 📊 Key Steps
### Cleaning & Imputation
- Mode-fill and binarize `mort_acc`  
- Drop high-cardinality/text columns (`emp_title`, `address`, etc.)

### Feature Engineering
- Label & target encoding (`term`, `grade`, `purpose`)  
- Extract `issue_month`, `issue_year`, `credit_age_years`

### Collinearity Control
- VIF analysis → removed `loan_amnt` (collinear with `installment`)

### Modeling & Tuning
- Baseline logistic regression → **F1(defaulter)=0.13**  
- +Class weights & SMOTE → **F1=0.42**  
- Threshold sweep & PR-AUC evaluation

### Evaluation
- Precision-recall curves  
- Confusion matrices  
- Test-set validation  

---

## 📈 Results
- **Defaulter F1:** 0.13 → 0.42 (+223%)  
- **Recall:** 0.08 → 0.64 (majority of defaulters caught)  
- **Precision:** 0.53 → 0.31 (trade-off for higher recall)  
- **PR-AUC:** ~0.36 before & after balancing (reflects minority performance)  

---

## 🔍 Business Insights & Conclusions
- **High-risk segments:** 60-month terms, grades E–G, high DTI, high interest  
- Higher open-account counts correlate with default  
- **Strongest predictor:** Loan grade  
- **Metric choice:** F1-score & recall matter most for NPA control  
- AUROC alone is misleading under imbalance  

---

## 🎯 Actionable Recommendations
- Refine underwriting rules:
  - Stricter approval or higher rates for 60-month loans  
  - Tighter DTI and loan-amount caps on E–G grades  
- Monitor key flags:
  - Any public record → automatic manual review  
  - Small-business purpose → require extra collateral  
- Operationalize model:
  - Deploy with a 0.5 threshold for balanced F1  
  - Regularly retrain as economic conditions shift  
- Enhance data sources:
  - Add transaction histories, geo-demographics, alternative credit data  
- Cost-benefit analysis:
  - Quantify cost of false positives vs false negatives to set business threshold  

---

# End-to-End ML Model Deployment on AWS 🚀

This project demonstrates how to deploy a Machine Learning model using AWS services, starting from building a **Web API** to full **CI/CD automation with GitHub Actions and ECS**.

---

## 1️⃣ Web API (Flask)
- Built a **Flask API** to expose the ML model as endpoints.
- Defined routes (`/ping`, `/predict`) to handle GET/POST requests.
- Returned predictions in **JSON format** for easy integration.
- Tested locally and via **Postman** to validate API responses.

---

## 2️⃣ Containerization & Docker
- Packaged the Flask app into a **Docker container** for portability.
- Created a `Dockerfile`:
  - `FROM python:3.8-slim-buster`
  - Installed dependencies from `requirements.txt`
  - Copied source code into container
  - Exposed app with `CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]`
- Built and ran the image locally to confirm functionality.

---

## 3️⃣ Deploy Docker to ECS
- **Amazon ECR**: Created a private repository to store Docker images.
- **Push Image**:
  - Logged in to ECR via AWS CLI
  - Tagged and pushed Docker image to ECR
- **Amazon ECS (Fargate)**:
  - Created ECS cluster
  - Defined ECS Task using the ECR image
  - Set up ECS Service to run the container
  - Configured networking/security groups to expose the API
- Result: Model accessible via ECS endpoint.

---

## 4️⃣ CI/CD with GitHub Actions → ECS
- Implemented **GitHub Actions workflow** in `.github/workflows/deploy.yml`.
- Workflow steps:
  1. **Checkout** repo
  2. **Configure AWS credentials** from GitHub Secrets
  3. **Login to ECR**
  4. **Build, tag, and push Docker image** to ECR
  5. **Update ECS Task Definition** with new image
  6. **Deploy ECS Service**
- Added **unit tests with Pytest** to validate code before deployment.
- Automated pipeline ensures every commit → build → test → deploy.

---

## 📊 Key Takeaways
- End-to-end ML deployment pipeline: **Flask API → Docker → ECS → CI/CD**  
- Hands-on with AWS services: **ECR, ECS, Fargate, GitHub Actions**  
- Production-ready workflow with **automated builds, tests, and deployments**  

---
