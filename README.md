# flask-mongo-api

Backend in Flask 

## Prerequisites
Ensure you have the following installed:
 - [Python 3.x](https://www.python.org/downloads/)
 - [MongoDB](https://www.mongodb.com/docs/manual/installation/)
 - A mongo database called flask-mongo-api & order collection

## Run Locally

Clone the project

```bash
  git clone git@github.com:manoelbalam/flask-mongo-api.git
```

Go to the project directory

```bash
  cd flask-mongo-api
```

Create a Virtual Environment

```bash
  python -m venv venv
```

Activate the Environment

```bash
  source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

Install Dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```
## API Reference

#### Get all orders

```http
  curl -i -X 'GET' 'http://127.0.0.1:5000/api/orders/' -H 'Content-Type: applicaion/json'
```

#### Create Order

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `customer_name`      | `string` | **Required**. Name of the customer |

```http
  curl -i -X 'POST' 'http://127.0.0.1:5000/api/orders/' -H 'Content-Type: application/json' -d '{"customer_name":"customer_name_0"}'
```