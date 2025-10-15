
# flask-mongo-api

Backend in Flask 



## Requirements

- Python env
- Installed and running mongoDB


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