🚀 Microservices Platform with CI/CD & Kubernetes
📌 Overview

This project is a cloud-native microservices system built using FastAPI, Docker, Kubernetes, and AWS services. It demonstrates real-world DevOps practices including containerization, orchestration, CI/CD pipeline design, and environment configuration management.

🏗️ Architecture
User
  ↓
API Gateway / NodePort Services
  ↓
────────────────────────────
| Auth Service (FastAPI)   |
| API Service (FastAPI)    |
────────────────────────────
  ↓
Docker Containers
  ↓
Kubernetes Cluster (Minikube / AWS EKS-ready)
  ↓
Database (AWS RDS PostgreSQL)
⚙️ Tech Stack
Backend: FastAPI (Python)
Containerization: Docker
Orchestration: Kubernetes (Minikube)
CI/CD: GitHub Actions (planned/extendable)
Cloud Services: AWS EC2, RDS, S3 (architecture-ready)
Database: PostgreSQL (RDS)
Version Control: Git & GitHub
📦 Microservices
1️⃣ Auth Service
User authentication endpoint
JWT token generation (mock/demo version)
Environment-based DB configuration
2️⃣ API Service
Main application service
REST API endpoints
Health check endpoint
🐳 Docker Setup
Build image:
docker build -t anpya/auth-service .
Run container:
docker run -p 8000:8000 anpya/auth-service
☸️ Kubernetes Deployment
Apply manifests:
kubectl apply -f k8s/
Check pods:
kubectl get pods
Check services:
kubectl get svc
Access services (Minikube):
minikube service auth-service
minikube service api-service
🌐 Environment Variables

Configured via Kubernetes Secrets / .env:

DB_HOST=your-rds-endpoint
DB_USER=admin
DB_PASS=******
DB_NAME=postgres
DB_PORT=5432
🔁 CI/CD Pipeline (Planned)

Future enhancement using GitHub Actions:

Build Docker image
Push to DockerHub
Deploy to Kubernetes cluster automatically
☁️ AWS Deployment (Architecture Ready)
EC2 → Kubernetes Node
RDS → PostgreSQL Database
S3 → File/log storage (optional)
🧪 API Endpoints
Auth Service
POST /login
GET  /
GET  /env
API Service
GET /
🧠 Key Learnings
Docker image creation & optimization
Kubernetes deployments & services (NodePort)
Debugging pod/service issues
Minikube networking (NodePort & tunneling)
Git & GitHub workflow handling
Environment variable management in microservices
🚧 Challenges Solved
Kubernetes service not accessible → fixed using NodePort + Minikube IP
Docker build context errors → fixed project structure
GitHub authentication issues → resolved with PAT/CLI
FastAPI dependency errors → fixed via Docker build
Environment variable injection in Kubernetes
📸 Project Status
✔ Microservices running
✔ Docker containers working
✔ Kubernetes cluster active
✔ GitHub repository updated
⏳ CI/CD pipeline pending
⏳ AWS deployment final step pending
👨‍💻 Author

Anupss0001
DevOps & Backend Engineer (Learning Path)

⭐ Future Improvements
Add API Gateway (Ingress Controller)
Implement real JWT authentication
Add monitoring (Prometheus + Grafana)
Fully automate CI/CD pipeline
Deploy production-grade AWS EKS cluster
🚀 Done
