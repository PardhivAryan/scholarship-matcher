
# 🎓 **Smart Scholarship Matcher – FastAPI + PostgreSQL + Docker**

A production-grade backend system that matches students to scholarships based on eligibility criteria using a custom scoring engine.
Built with **FastAPI**, **PostgreSQL**, **JWT Authentication**, **Docker Compose**, and a clean, modular architecture.

---

# 🚀 **Features**

* 🔐 **JWT Authentication** (Signup, Login, Protected Routes)
* 👨‍🎓 **Student Profile Management**
* 🎓 **Create & Manage Scholarships** (Eligibility rules: CGPA, Income, Category, State)
* 🤖 **Matching Engine** that scores scholarships for each student (0–100)
* 🧠 **Search Engine** (Elasticsearch Ready)
* 🐳 **Fully Dockerized** (FastAPI + PostgreSQL + Elasticsearch)
* 📁 Clean structure with **Models, Schemas, Routers, Services**
* 🧪 **Interactive API Docs** via Swagger ([http://localhost:8000/docs](http://localhost:8000/docs))

---

# 🏗 **Project Architecture**

```
scholarship-matcher/
│── app/
│   ├── routers/          # API endpoints
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Matching & search logic
│   ├── utils/            # JWT + Hasher
│   ├── database.py       # DB engine & session
│   ├── main.py           # FastAPI app entry
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── README.md
```

---

# 📦 **Tech Stack**

### **Backend**

* FastAPI
* Python 3.10
* SQLAlchemy
* PostgreSQL
* JWT (PyJWT)
* Passlib (bcrypt hashing)

### **DevOps / Infra**

* Docker
* Docker Compose
* Elasticsearch (optional module)
* Redis (optional for caching)

---

# 🐳 **Run With Docker (recommended)**

Make sure Docker Desktop is running, then:

```bash
docker-compose up --build
```

This will start:

* FastAPI backend → [http://localhost:8000](http://localhost:8000)
* PostgreSQL → port 5432
* Elasticsearch → port 9200

All auto-connected through a Docker network.

---

# ⚙️ **Run Without Docker (local venv)**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Go to:

👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

# 🔐 **Authentication Endpoints**

### **Signup**

```
POST /auth/signup
```

### **Login**

```
POST /auth/login
```

Returns:

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

Use this token in all protected endpoints.

---

# 👨‍🎓 **Student Endpoints**

### **Update Profile**

```
PUT /students/update
```

JSON Example:

```json
{
  "token": "<JWT>",
  "age": 20,
  "gender": "M",
  "income": 150000,
  "cgpa": 8.5,
  "category": "OBC",
  "state": "Andhra Pradesh"
}
```

### **View Profile**

```
GET /students/me?token=<JWT>
```

---

# 🎓 **Scholarship Endpoints**

### **Create Scholarship**

```
POST /scholarships/create
```

JSON Example:

```json
{
  "token": "<JWT>",
  "name": "AP Merit Scholarship",
  "provider": "Govt of AP",
  "description": "Award for top students",
  "min_income": 0,
  "max_income": 200000,
  "min_cgpa": 7,
  "categories": ["OBC", "SC", "General"],
  "states": ["Andhra Pradesh", "Telangana"]
}
```

---

# 🤖 **Matching Engine**

```
GET /scholarships/match?token=<JWT>
```

The backend generates a score out of **100**:

| Criteria       | Points |
| -------------- | ------ |
| CGPA match     | +30    |
| Income match   | +40    |
| Category match | +20    |
| State match    | +10    |

Example Response:

```json
[
  {
    "scholarship": {
      "id": 1,
      "name": "AP Merit Scholarship"
    },
    "score": 100
  }
]
```

---

# 🔍 **Full-Text Search**

```
GET /scholarships/search?query=merit
```

(Uses Elasticsearch if enabled)

---

# 🧪 **Swagger API Docs**

Once the server is running:

👉 [http://localhost:8000/docs](http://localhost:8000/docs)
👉 [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

# 🏁 **License**
Free for learning & personal projects.
