

# RamenAI
RamenAI is a chatbot focused on ramen enthusiasts. The chat generates recommendations and different recipes according to your tastes and based on each user's past conversation history.


## Docker Deployment Guide

### Prerequisites

- Docker
- MongoDB uri

Step 1: Clone the repository
```
git clone https://github.com/pamelasann/RamenAI.git
```
Step 2: Create the .env file
```
OPENAI_API_KEY = "your_api_key"
MONGO_URI = "your_mongodb_uri"
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
```
Step 3: Deploy the Architecture with Docker Compose
```
docker-compose up --build
```

# RamenAI
<img src="./previewImages/login.png" alt="Main Menu" width=750 height=400>
<img src="./previewImages/chat.png" alt="Main Menu" width=750 height=400>
