**🚀 Support Nexus – Frontend**

Frontend interface for Support Nexus, an AI-powered multi-agent customer support system.
Built using Streamlit, this application provides a conversational UI for querying the AI backend and uploading documents for vector-based ingestion.

**📌 Overview**

Support Nexus Frontend enables users to:

    💬 Interact with the AI support system via natural language

    📄 Upload PDF documents for ingestion into a Vector Database

    ⚡ Experience faster responses using session-based caching

**Note:** This repository contains only the UI and API integration layer.
The AI orchestration and RAG pipeline live in the backend repository.

**✨ Features**

**💬 Conversational Query Interface**

      Chat-style UI

      Maintains session message history

      Integrates with FastAPI backend

      Displays structured AI responses

      Caches repeated queries within session

**📄 Document Upload**

      Accepts PDF files

      Sends multipart/form-data to backend

      Backend processes ingestion asynchronously

      Displays upload status feedback

**⚡ Session-Based Cache**

      Reduces repeated API calls

      Improves perceived response speed

      Tracks query frequency

**⚙️ Installation**

**1️⃣ Clone Repository**

      git clone https://github.com/Amit-9889/support-nexus-frontend.git
      cd support-nexus-frontend

**2️⃣ Create Virtual Environment**

      python -m venv venv
      venv\Scripts\activate      # Windows
      source venv/bin/activate   # Mac/Linux

**3️⃣ Install Dependencies**

      pip install -r requirements.txt

**🔗 Backend Repository**

This frontend integrates with the Support Nexus Backend, which contains:

      Multi-agent orchestration

      Intent detection and routing

      RAG-based document retrieval

      Background ingestion pipeline

      FastAPI API layer

**👉 Backend Repository:**

      https://github.com/Amit-9889/support-nexus-backend.git
      Make sure the backend server is running before starting the frontend.

**🔌 API Contract**
**Query Endpoint**

      POST /api/v1/query

      Request

      {
        "question": "What is refund policy?",
        "user_id": "Amit_123"
      }


      Response

      {
        "status": "success",
        "messages": {
          "question": "...",
          "intent": "POLICY",
          "answer": "...",
          "user_id": "...",
          "order_id_required": false
        }
      }

**Upload Endpoint**

      POST /api/v1/upload/upload

      Content-Type: multipart/form-data

      Field name: file

      Only PDF supported

**▶️ Run Application**

      streamlit run app.py


**Application runs at:**

      http://localhost:8501


**Ensure backend is running at:**

      http://127.0.0.1:8000
