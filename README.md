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
7. [Development](#-Development)

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

> NOTE: mongo daemon must be running in the OS.

> NOTE: mandatory a database named ``flask-mongo-api`` and a collection named ``order``

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
- **GET** `/api/orders/`
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
- **POST** `/api/orders/`
  - Create a new order
  - Body Parameters:
    - `String:customer_name`: Name of the customer

  Example:

  ```http
  curl -i -X 'POST' 'http://127.0.0.1:5000/api/orders/' -H 'Content-Type: application/json' -d '{"customer_name":"customer_name"}'
  ```
  Response:
  ```http
  HTTP/1.1 201 CREATED
  Server: Werkzeug/3.1.3 Python/3.11.2
  Date: Fri, 17 Oct 2025 00:26:25 GMT
  Content-Type: application/json
  Content-Length: 83
  Connection: close

  {
    "Message": "Order created successfully!",
    "id": "68f18d313446633c95bed359"
  }
  ```

- **DELETE** `/api/orders/<string:order_id>`

  - Delete an order by order_id
   - Query Parameters:
    - `ObjectId:order_id`: It must be a 12-byte input or a 24-character hex string 

  Example:

  ```http
  curl -i -X 'DELETE' 'http://127.0.0.1:5000/api/orders/68f18d313446633c95bed359' -H 'Content-Type: applicaion/json'
  ```
  Response:
  ```http
  HTTP/1.1 200 OK
  Server: Werkzeug/3.1.3 Python/3.11.2
  Date: Fri, 17 Oct 2025 00:37:05 GMT
  Content-Type: application/json
  Content-Length: 46
  Connection: close

  {
    "Message": "Order deleted successfully"
  }
  ```

- **GET** `/api/orders/<string:order_id>`

  - Retrieve an order by order_id
  - Query Parameters:
    - `ObjectId:order_id`: It must be a 12-byte input or a 24-character hex string

  Example:

  ```http
  curl -i -X 'GET' 'http://127.0.0.1:5000/api/orders/68f18d313446633c95bed359' -H 'Content-Type: applicaion/json'
  ```
  Response:
  ```http
  HTTP/1.1 200 OK
  Server: Werkzeug/3.1.3 Python/3.11.2
  Date: Fri, 17 Oct 2025 00:31:10 GMT
  Content-Type: application/json
  Content-Length: 102
  Connection: close

  {
    "_id": "68f18d313446633c95bed359",
    "customer_name": "customer_name",
    "status": "inProgress"
  }
  ```

- **PATCH** `/api/orders/<string:order_id>`

  - Update an order by order_id
  - Query Parameters:
    - `ObjectId:order_id`: It must be a 12-byte input or a 24-character hex string 
  - Body Parameters:
    - `String:customer_name`: Name of the customer
    - `String:status`: Status of the order could be ["inProgress", "Done", "Delivered"]

  Example:

  ```http
  curl -i -X 'PATCH' 'http://127.0.0.1:5000/api/orders/68f18d313446633c95bed359' -H 'Content-Type: application/json' -d '{"customer_name":"customer_name_updated", "status":"Done"}'
  ```
  Response:
  ```http
  HTTP/1.1 200 OK
  Server: Werkzeug/3.1.3 Python/3.11.2
  Date: Fri, 17 Oct 2025 00:33:24 GMT
  Content-Type: application/json
  Content-Length: 104
  Connection: close

  {
    "_id": "68f18d313446633c95bed359",
    "customer_name": "customer_name_updated",
    "status": "Done"
  }
  ```

---
## ⚙️ Testing the API

You can test the API using the following methods:

1. **Unit Testing (Open API)**:  **_Flasgger UI_** will run on: `http://localhost:5000/apidocs/`
   
2. **Postman / cURL**: Use these tools to manually send HTTP requests to the Flask API and verify the responses.

---
## 🛠️ Development

### Database Schema

The **order** model includes:
- `_id`: ObjectId (Primary Key)
- `customer_name`: String (Required)
- `status`: String (Required)