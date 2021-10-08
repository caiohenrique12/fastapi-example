from fastapi import APIRouter
from pydantic import BaseModel

from app.models import Customer

router = APIRouter()


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


@router.get("/customers/", tags="customers")
async def index():
    return await Customer.objects.all()


@router.get("customers/{customer_name}", tags="customers")
async def customer(customer_name: str):
    return {"hello": "world"}


@router.post("/customers/", tags="customers")
async def create(customer: BaseCustomer):
    new_customer = Customer.create(customer)

    if new_customer:
        return 201
    else:
        return 404
