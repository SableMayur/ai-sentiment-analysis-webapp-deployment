🚀 Production-Ready AI Sentiment Analysis: Hugging Face, FastAPI, Docker & Kubernetes
A complete, beginner-friendly DevOps guide and project template demonstrating how to take a Hugging Face machine learning model (distilbert-base-uncased-finetuned-sst-2-english), wrap it in a lightweight interactive web application using FastAPI, containerize it with Docker, and deploy it onto a Kubernetes cluster.

📂 Project Architecture
ai-sentiment-analysis/
│
├── main.py              # FastAPI web server and Hugging Face pipeline logic
├── requirements.txt     # Python dependencies (including CPU-optimized PyTorch)
├── Dockerfile           # Instructions to build the Docker container image
└── deployment.yaml      # Kubernetes Deployment and Service manifests

🛠️ Step 1: Local Setup & Testing (Without Docker)
Before using containers, let's verify everything works locally in a Python virtual environment.
1. Clone the Repository & Setup Virtual Environment
Open your terminal and run:
# Clone your repository and enter the folder
cd ai-sentiment-analysis

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS / Linux:
source venv/bin/activate
# On Windows (PowerShell):
venv\Scripts\Activate.ps1
2. Configure requirements.txt
Make sure your requirements.txt includes the required packages and uses the CPU-optimized PyTorch wheel (ideal for standard servers and testing sandboxes like Killercoda):
fastapi
uvicorn
python-multipart
pydantic
transformers
torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu
3. Install Dependencies
pip install -r requirements.txt
4. Run the Local Server
uvicorn main:app --reload --host 127.0.0.1 --port 8000
Open your browser and visit http://127.0.0.1:8000. Test typing a sentence to verify the sentiment analyzer works seamlessly! Press Ctrl + C in your terminal to stop the server when done.

🐳 Step 2: Containerize with Docker
Now that our code is verified, let's package it into a Docker container image.
1. Create a Dockerfile
Create a file named Dockerfile (no file extension) in your root folder and paste the following configuration:
```dockerfile
FROM python:3.10-slim


WORKDIR /app


# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


# Copy requirements and install python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of your application code into the container
COPY . .


EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. Build Your Docker Container Image
Run the build command in your terminal:
docker build -t sentiment-app:latest .
3. Run the Container Locally
Test your built container to make sure the app launches properly inside it:
docker run -p 8000:8000 sentiment-app:latest
Visit http://localhost:8000 in your browser. You are now running your app inside an isolated Docker container! Press Ctrl + C to exit.
4. Push to Container Registry (e.g., Docker Hub)
For Kubernetes to deploy your container, it needs to pull your image from a container registry.
# Log in to Docker Hub
docker login

# Tag your image (replace 'your-dockerhub-username' with your actual account name)
docker tag sentiment-app:latest your-dockerhub-username/sentiment-app:latest

# Push to Docker Hub
docker push your-dockerhub-username/sentiment-app:latest

☸️ Step 3: Deploy to Kubernetes
Deploy your application container to a Kubernetes cluster (works with Minikube, kind, Killercoda, or cloud providers like EKS, GKE, AKS).
1. Create deployment.yaml
Create a file named deployment.yaml in your project root:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sentiment-app-deployment
spec:
  replicas: 2 # Creates 2 pod replicas for high availability/load balancing
  selector:
    matchLabels:
      app: sentiment-app
  template:
    metadata:
      labels:
        app: sentiment-app
    spec:
      containers:
      - name: sentiment-app
        image: your-dockerhub-username/sentiment-app:latest # Make sure to match your Docker Hub image tag
        ports:
        - containerPort: 8000
        resources:
          limits:
            cpu: "1"
            memory: "1Gi"
          requests:
            cpu: "500m"
            memory: "512Mi"
---
apiVersion: v1
kind: Service
metadata:
  name: sentiment-app-service
spec:
  type: LoadBalancer # Exposes service externally (or NodePort depending on your cluster environment)
  selector:
    app: sentiment-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
```

2. Apply the Configuration
Run the following kubectl command in your terminal:
kubectl apply -f deployment.yaml
3. Verify Deployment
Check if your pods and service are running successfully:
kubectl get pods
kubectl get services
Once active, access your service via the cluster's external IP or port, type any sentence, and see your Hugging Face model compute live sentiment analysis inside a scalable Kubernetes cloud architecture!

📝 License
This project is open-source and available under the MIT License.
