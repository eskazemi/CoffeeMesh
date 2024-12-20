from datetime import datetime
from enum import Enum
from typing import (
    List,
    Optional,
)
from uuid import UUID

from pydantic import (
    BaseModel,
    conint,
    field_validator,
    conlist,
    Extra,
)


class Size(Enum):
    small = "small"
    medium = "medium"
    big = "big"


class StatusEnum(Enum):
    created = "created"
    paid = "paid"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"


class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Optional[conint(ge=1, strict=True)] = 1  # should integer

    class Config:
        extra = Extra.forbid
        # We use Config to ban
        # properties that haven’t been
        # defined in the schema.

    @field_validator('quantity')
    @classmethod
    def quantity_non_nullable(cls, value: int):
        assert value is not None, "quantity may not be None"
        return value


class CreateOrderSchema(BaseModel):
    order: conlist(OrderItemSchema, min_length=1)

    class Config:
        extra = Extra.forbid


class GetOrderSchema(CreateOrderSchema):
    id: UUID
    created: datetime
    status: StatusEnum


class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]

    class Config:
        extra = Extra.forbid