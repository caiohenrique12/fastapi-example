from typing import Optional

from fastapi import Request, FastAPI
from pydantic import BaseModel

from app.db import database, Customer

app = FastAPI(title="FastAPI, Docker, and Traefik")


class BaseCustomer(BaseModel):
    name: str
    age: int
    street: str
    number: str
    neighborhood: str
    complement: str
    city: str
    state: str
    country: str
    active: bool


@app.get("/")
async def read_root():
    return {"hello": "world"}

@app.get("customers/")
async def index():
    return await Customer.objects.all()

@app.post("/customers/")
async def create(customer: BaseCustomer):
    if not database.is_connected:
        await database.connect()

    new_customer = Customer.objects.get_or_create(name=customer.name, age=customer.age,
                                                  street=customer.street, number=customer.number,
                                                  city=customer.city, state=customer.state,
                                                  neighborhood=customer.neighborhood,
                                                  complement=customer.complement,
                                                  active=customer.active)
    if new_customer:
        return 201
    else:
        return 404
