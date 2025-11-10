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

## ▶️ Future Improvements
- Add **Docker Compose** for multi-container setups  
- Integrate **monitoring/logging** (CloudWatch)  
- Extend CI/CD with **blue/green deployments**  


