from typing import List
from pydantic import BaseModel

"""
  A sample order can be published by invoking the curl script below against
  the exposed endpoint (localhost:8080/order when running locally):

curl -X 'POST' \
  'http://localhost:8080/order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "id":"6e042f29-350b-4d51-8849-5e36456dfa48",
    "products":[
       {
          "productCode":"12345",
          "quantity":2
       }
    ],
    "customer":{
       "firstName":"Tom",
       "lastName":"Hardy",
       "emailAddress":"tom.hardy@email.com",
       "shippingAddress":{
          "line1":"123 Anywhere St",
          "city":"Anytown",
          "state":"AL",
          "postalCode":"12345"
       }
    }
 }'
"""


# Handsomely generated from JSON sample by https://jsontopydantic.com/
class Product(BaseModel):
    productCode: str
    quantity: int


class ShippingAddress(BaseModel):
    line1: str
    city: str
    state: str
    postalCode: str


class Customer(BaseModel):
    firstName: str
    lastName: str
    emailAddress: str
    shippingAddress: ShippingAddress


class Order(BaseModel):
    id: str
    products: List[Product]
    customer: Customer
