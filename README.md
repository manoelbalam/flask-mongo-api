# flask-mongo-api - Orders Backend

Backend in Flask written in Debian BookWorm

---
## Table of Contents

1. [Project Components](#-project-components)
2. [Design Pattern](#-design-pattern)
    - [Layered Pattern](#layered-pattern)
3. [Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
4. [Project Structure](#-project-structure)
5. [API Endpoints](#-api-endpoints)
    - [Orders](#orders)
6. [Testing the API](#-testing-the-api)

---
## 🔗 Project Components

- **Backend**:
  - RESTful API
  - Database management
  - Log activity
---
## ⛁ Design Pattern

### Layered Pattern

![App](https://i.postimg.cc/zXpGBTpX/app.png)

The application is contains 3 main layers and 1 parallel layer each with its own responsibility.

- **Presentation Layer:**
  - Controllers
    
- **Business Layer:**
  - Business Logic
  - Validations

- **Persistence Layer:**
  - Mongo database Access

- **Loggin Layer:**
  - Log business layer
  - Log persistence layer 
---
## 🚀 Getting Started

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/docs/manual/installation/)
- Virtual environment (recommended)
- [Postman (optional)](http://postman.com/)

### Installation

1: Clone repository:
```bash
  git clone git@github.com:manoelbalam/flask-mongo-api.git
```
2: Go to the project directory

```bash
  cd flask-mongo-api
```

3: Create a Virtual Environment

```bash
  python -m venv venv
```

4: Activate the Environment

```bash
  source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

5: Install Dependencies

```bash
  pip install -r requirements.txt
```

6: Start the server

```bash
  python3 app.py
```

**Flask API** will run on: `http://127.0.0.1:5000`

__WARNING__ :
* mongodb daemon must be running in the OS.
* mandatory a database named ``flask-mongo-api``
* mandatory a collection named ``order``
---
## 📁 Project Structure

```
flask-mongo-api/                 # Backend code written in Flask
├── app.py                       # Main Flask application file
├── controllers/
|   └── orderController.py       # Contains the API endpoints
├── dbaccess/
|   └── orderDBA.py              # Persist data into DB
├── logic/
|   └── orderLogic.py            # Data fields validationd and logic
├── requirements.txt             # Project dependencies
└── README.md                    # Project README file (this file)
```
---
## 🔌 API Endpoints

### Orders
- `GET /api/orders`
  - Get all orders

  Example:

  ```http
  curl -i -X 'GET' 'http://127.0.0.1:5000/api/orders/' -H 'Content-Type: applicaion/json'
  ```
  Response:
  ```http
  Date: Thu, 16 Oct 2025 23:20:10 GMT
  Content-Type: application/json
  Content-Length: 94
  Connection: close

  [
    {
      "_id": "68f077cbe2684838baa87acd",
      "customer_name": "customer_name",
      "status": "inProgress"
    }
  ]
  ```
---
## ⚙️ Testing the API

You can test the API using the following methods:

1. **Unit Testing (Open API)**:
  **Flasgger UI** will run on: `http://127.0.0.1:5000`
   
2. **Postman / cURL**: Use these tools to manually send HTTP requests to the Flask API and verify the responses.

---