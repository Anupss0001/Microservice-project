# 🚀 Microservices Platform with CI/CD & Kubernetes

---

## 📌 Overview

This project is a **cloud-native microservices system** built using **FastAPI, Docker, Kubernetes, and AWS services**.

It demonstrates real-world DevOps practices including:
- Containerization
- Microservices architecture
- Kubernetes orchestration
- CI/CD pipeline design (planned)
- Environment configuration management

---

## 🏗️ Architecture

User
↓
API Gateway / NodePort Services
↓
| Auth Service (FastAPI) |
| API Service (FastAPI) |

↓
Docker Containers
↓
Kubernetes Cluster (Minikube / AWS-ready)
↓
Database (AWS RDS PostgreSQL)


---

## ⚙️ Tech Stack

- **Backend:** FastAPI (Python)
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)
- **CI/CD:** GitHub Actions (planned)
- **Cloud:** AWS EC2, RDS, S3 (architecture-ready)
- **Database:** PostgreSQL
- **Version Control:** Git & GitHub

---

## 📦 Microservices

### 1️⃣ Auth Service
- User authentication endpoint
- JWT token generation (mock version)
- Environment-based DB configuration

### 2️⃣ API Service
- REST API endpoints
- Health check endpoint

---

## 🐳 Docker Setup

### Build Image
```bash
docker build -t anpya/auth-service .
Run Container
docker run -p 8000:8000 anpya/auth-service
☸️ Kubernetes Deployment
Apply manifests
kubectl apply -f k8s/
Check resources
kubectl get pods
kubectl get svc
Access services
minikube service auth-service
minikube service api-service
🌐 Environment Variables
DB_HOST=your-rds-endpoint
DB_USER=admin
DB_PASS=******
DB_NAME=postgres
DB_PORT=5432
🔁 CI/CD Pipeline (Planned)
Build Docker image
Push to DockerHub
Deploy automatically to Kubernetes using GitHub Actions
☁️ AWS Deployment (Architecture Ready)
EC2 → Kubernetes worker node
RDS → PostgreSQL database
S3 → Logs / file storage (optional)
🧪 API Endpoints
Auth Service
POST /login
GET /
GET /env
API Service
GET /
🧠 Key Learnings
Docker image creation & deployment
Kubernetes deployments & services
NodePort networking in Minikube
Debugging pods and services
Git & GitHub workflow
Environment variable management in microservices
🚧 Challenges Solved
Kubernetes service not accessible → fixed using NodePort + Minikube IP
Docker build context errors → fixed project structure
GitHub authentication issues → resolved using PAT
FastAPI dependency issues → fixed using Docker build
Environment variables injection in Kubernetes
📸 Project Status

✔ Microservices running
✔ Docker containers working
✔ Kubernetes cluster active
⏳ CI/CD pipeline pending
⏳ AWS deployment pending

👨‍💻 Author

Anupss0001
DevOps & Backend Engineer (Learning Path)

⭐ Future Improvements
Add API Gateway (Ingress Controller)
Implement real JWT authentication
Add monitoring (Prometheus + Grafana)
Fully automate CI/CD pipeline
Deploy production-grade AWS EKS cluster
