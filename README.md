# 🚀 AI Sentiment Analysis Web Application Deployment
### Hugging Face | Python | FastAPI | Docker | Docker Hub

A hands-on project demonstrating how to integrate a pretrained AI model from Hugging Face into a web application and deploy it using Docker containers.

This project uses a pretrained DistilBERT model for sentiment classification. Users can enter text through a web interface, and the application predicts whether the sentiment is Positive or Negative.

The main objective is to understand the complete process of using an AI model, developing a Python web application, containerizing it, and deploying it using Docker.

---

## 📌 Project Overview

In this project, we will:

- Explore pretrained models available on Hugging Face.
- Integrate a pretrained DistilBERT model into Python.
- Develop a sentiment analysis web application using FastAPI.
- Set up a Python virtual environment.
- Install the required application dependencies.
- Create a Dockerfile to containerize the application.
- Build and manage Docker images.
- Run the application inside Docker containers.
- Publish Docker images to Docker Hub.
- Pull and run the application image on another machine.

Application Screenshots

1. Sentiment Analyzer – Input Page

Enter your text into the input field and click Analyze Sentiment to analyze its emotional tone.

2. Sentiment Analysis – Result Page

The application displays the predicted sentiment along with its confidence score.

Example Output:

Input: i am happy

Sentiment: POSITIVE

Confidence Score: 0.9999


## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Application development |
| Hugging Face | Pretrained AI models |
| DistilBERT | Sentiment classification |
| Transformers | Model integration |
| PyTorch (CPU) | Model inference |
| FastAPI | Web application |
| Uvicorn | Application server |
| Docker | Application containerization |
| Docker Hub | Docker image registry |
| Git & GitHub | Version control |

---

## 🏗️ Project Architecture

```text
             USER
               |
               v
       Sentiment Analysis UI
               |
               v
          FastAPI Server
               |
               v
      Hugging Face Transformers
               |
               v
       Pretrained DistilBERT
               |
               v
       Sentiment Prediction
               |
               v
        Positive / Negative
               |
               v
          Docker Image
               |
               v
           Docker Hub
               |
               v
        Docker Container
               |
               v
       Running Application
```

---

## 📂 Project Structure

```text
ai-sentiment-analysis-webapp-deployment/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
└── README.md
```

---

# 🧪 PRACTICAL IMPLEMENTATION

## Step 1: Clone the GitHub Repository

Clone the project:

```bash
git clone https://github.com/SableMayur/ai-sentiment-analysis-webapp-deployment.git
```

Navigate to the project directory:

```bash
cd ai-sentiment-analysis-webapp-deployment
```

Verify the files:

```bash
ls
```

For Windows PowerShell:

```powershell
dir
```

## Step 2: Understand the Hugging Face Model

[Hugging Face](https://huggingface.co/) is a platform that provides pretrained machine learning models, datasets, and tools for AI development.

Instead of training a sentiment analysis model from scratch, we use an existing pretrained model.

**Model used:**

`distilbert-base-uncased-finetuned-sst-2-english`

Model link:

https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english

This model is fine-tuned for binary sentiment classification.

It predicts two classes:

- POSITIVE
- NEGATIVE

### How to use the Hugging Face model

Install the required libraries:

```bash
pip install transformers torch
```

Import the pipeline:

```python
from transformers import pipeline
```

Load the pretrained model:

```python
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
```

Pass text to the model:

```python
result = classifier("I love learning Docker and Kubernetes!")

print(result)
```

Example output:

```python
[
    {
        'label': 'POSITIVE',
        'score': 0.9998
    }
]
```

The model returns a sentiment label and a confidence score.

**Note:** The first model load downloads the pretrained model from Hugging Face. An internet connection is required unless the model is already cached locally.

## Step 3: Set Up the Python Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

**Linux:**

```bash
source venv/bin/activate
```

### Install dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

For CPU-only PyTorch installation, use:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

If using this separate CPU installation, ensure `torch` is not also installed through `requirements.txt`.

### Run the application locally

Start the FastAPI application:

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Open your browser:

http://127.0.0.1:8000

Enter text into the application and click the Analyze Sentiment button.

The application will display the predicted sentiment and confidence score.

Stop the server using:

```text
CTRL + C
```

---

# 🐳 STEP 4: Containerize the Application Using Docker

Now that the application works locally, let's package it using Docker.

### 4.1 Understanding the Dockerfile

Create a file named `Dockerfile` in the project root.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install CPU-only PyTorch
RUN pip install --no-cache-dir torch \
    --index-url https://download.pytorch.org/whl/cpu

# Install remaining dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Dockerfile explanation

| Instruction | Purpose |
|---|---|
| FROM | Selects the Python base image |
| WORKDIR | Sets the working directory |
| RUN | Executes commands during image building |
| COPY | Copies application files |
| EXPOSE | Documents the application port |
| CMD | Defines the container startup command |

### 4.2 Create .dockerignore

Create a `.dockerignore` file:

```text
venv/
.venv/
__pycache__/
*.pyc
.git/
.gitignore
.env
.vscode/
.idea/
*.log
```

This prevents unnecessary files from being included in the Docker build context.

### 4.3 Build the Docker Image

Run:

```bash
docker build -t sentiment-analysis:v1 .
```

Check the image:

```bash
docker images
```

### 4.4 Run the Docker Container

Start the application inside a Docker container:

```powershell
docker run -d -p 8000:8000 --name sentiment-app sentiment-analysis:v1
```

Explanation:

- `-d`: Runs the container in detached mode.
- `-p 8000:8000`: Maps host port 8000 to container port 8000.
- `--name`: Assigns a name to the container.
- `sentiment-analysis:v1`: Specifies the Docker image.

### 4.5 Verify the Container

Check running containers:

```bash
docker ps
```

View application logs:

```bash
docker logs sentiment-app
```

Access the application:

http://localhost:8000

### 4.6 Access the Container

Enter the running container:

```bash
docker exec -it sentiment-app bash
```

Check application files:

```bash
ls
```

Check installed packages:

```bash
pip list
```

Exit the container:

```bash
exit
```

### Useful Docker Commands

| Command | Description |
|---|---|
| `docker images` | List available images |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker logs sentiment-app` | View container logs |
| `docker inspect sentiment-app` | Inspect container configuration |
| `docker exec -it sentiment-app bash` | Access container shell |
| `docker stop sentiment-app` | Stop container |
| `docker start sentiment-app` | Start stopped container |
| `docker rm -f sentiment-app` | Remove container |

---

# ☁️ STEP 5: Push Docker Image to Docker Hub

Docker Hub is a cloud-based container registry where developers can store and distribute Docker images.

### 5.1 Create a Docker Hub Repository

1. Visit https://hub.docker.com/
2. Sign in to your Docker Hub account.
3. Click on Create Repository.
4. Enter repository name: `sentiment-analysis`.
5. Select Public visibility.
6. Create the repository.

### 5.2 Login to Docker Hub

Run:

```bash
docker login
```

Authenticate using your Docker Hub credentials or access token.

### 5.3 Tag the Docker Image

Tag the local image with your Docker Hub username:

```bash
docker tag sentiment-analysis:v1 sablemayur17/sentiment-analysis:v1
```

### 5.4 Push the Image

Upload the Docker image:

```bash
docker push sablemayur17/sentiment-analysis:v1
```

Docker uploads the image layers to Docker Hub.

### 5.5 Verify the Image

Visit your Docker Hub repository:

https://hub.docker.com/r/sablemayur17/sentiment-analysis

You should see the uploaded `v1` image tag.

### 5.6 Pull the Image

To download the image on another machine:

```bash
docker pull sablemayur17/sentiment-analysis:v1
```

### 5.7 Run the Pulled Image

```bash
docker run -d -p 8000:8000 \
  --name sentiment-app \
  sablemayur17/sentiment-analysis:v1
```

The application can now run on another machine without manually installing Python and its dependencies.

---

# 🔄 Complete Project Workflow

```text
        GitHub Repository
                |
                v
          Clone Project
                |
                v
       Setup Python Environment
                |
                v
        Install Dependencies
                |
                v
       Load Hugging Face Model
                |
                v
        Run FastAPI Application
                |
                v
          Create Dockerfile
                |
                v
         Build Docker Image
                |
                v
        Run Docker Container
                |
                v
        Push Image to Docker Hub
                |
                v
       Pull Image on Another Machine
                |
                v
        Run Container Successfully
```

---

# 🛠️ Troubleshooting Guide

### 1. No space left on device

**Error:**

```text
OSError: [Errno 28] No space left on device
```

**Solution:**

Use CPU-only PyTorch and check Docker disk usage:

```bash
docker system df
```

Remove unused build cache:

```bash
docker builder prune -af
```

### 2. Docker permission denied

On Linux, add your user to the Docker group:

```bash
sudo usermod -aG docker $USER
```

Log out and log back in.

### 3. Container exits immediately

Check container logs:

```bash
docker logs sentiment-app
```

Check container status:

```bash
docker ps -a
```

### 4. Application is not accessible

Verify port mapping:

```bash
docker port sentiment-app
```

Ensure Uvicorn listens on:

```text
0.0.0.0:8000
```

### 5. Hugging Face model download fails

Check your internet connectivity and Hugging Face availability. The first model download requires internet access unless the model is already cached.

---

# 📚 Learning Outcomes

After completing this project, you should understand:

1. How pretrained Hugging Face models work.
2. How to integrate AI models into Python applications.
3. How FastAPI serves a web application.
4. How to create and manage Python virtual environments.
5. How Docker images and containers work.
6. How to write Dockerfiles.
7. How to build and run Docker images.
8. How to publish Docker images to Docker Hub.
9. How to pull images and deploy containers on another machine.
10. How to troubleshoot common containerization issues.

---

## 👨‍💻 Author

**Mayur Sable**

Aspiring Cloud & DevOps Engineer

- GitHub: [SableMayur](https://github.com/SableMayur)
- LinkedIn: [Mayur Sable](https://www.linkedin.com/in/sablemayur/)
- Project Repository: [AI Sentiment Analysis Web Application Deployment](https://github.com/SableMayur/ai-sentiment-analysis-webapp-deployment)

---

⭐ If this project helps you learn AI application deployment and Docker fundamentals, consider giving the repository a star!

**Happy Learning & Happy Deploying! 🚀**
