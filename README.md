# flask-mongo-api - Orders Backend

Backend in Flask written in Debian BookWorm

## 🔗 Project Components

- **Backend** (This Repository):
  - RESTful API
  - Database management
  - Log activity

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

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Mongo Database
- Virtual environment (recommended)
- Postman (optional)

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

__WARNING__ :
* mongodb daemon must be running in the OS.
* mandatory a database named ``flask-mongo-api``
* mandatory a collection named ``order``

You can explore the api by running : [http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)

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

## 🔌 API Endpoints
