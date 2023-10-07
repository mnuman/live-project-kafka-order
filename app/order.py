from typing import List
from pydantic import BaseModel


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
