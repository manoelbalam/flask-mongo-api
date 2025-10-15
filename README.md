# flask-mongo-api

Backend in Flask writed in Debian BookWorm

## Prerequisites
Ensure you have the following installed:
 - [Python 3.x](https://www.python.org/downloads/)
 - [MongoDB](https://www.mongodb.com/docs/manual/installation/)
 - A mongo database named flask-mongo-api & order collection

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
  source venv/bin/activate
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

#### Get order by id

```http
  curl -i -X 'GET' 'http://127.0.0.1:5000/api/orders/68efb402513bc61af848ccfdasas' -H 'Content-Type: applicaion/json'
```

#### Create Order

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `customer_name`      | `string` | **Required**. Name of the customer |

```http
  curl -i -X 'POST' 'http://127.0.0.1:5000/api/orders/' -H 'Content-Type: application/json' -d '{"customer_name":"customer_name_0"}'
```

#### Update Order

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `customer_name`      | `string` | **Required**. Name of the customer |

```http
  curl -i -X 'PATCH' 'http://127.0.0.1:5000/api/orders/68f00e0fd92ada1eb3775a32' -H 'Content-Type: application/json' -d '{"customer_name":"customer_name_0", "status":"Done4"}'

```

#### Delete Order

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `order_id`      | `string` | **Required**. Name of the customer |

```http
  curl -i -X 'DELETE' 'http://127.0.0.1:5000/api/orders/68ef1de67664eef7dae6cfb7' -H 'Content-Type: applicaion/json'
```
