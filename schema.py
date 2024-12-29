# schema.py
from typing import Optional, List
import strawberry
from datetime import datetime
from models import db, ShoppingCart

@strawberry.type
class CartType:
    id: int
    name: str
    price: float
    quantity: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_model(cls, model: ShoppingCart):
        return cls(
            id=model.id,
            name=model.name,
            price=model.price,
            quantity=model.quantity,
            created_at=model.created_at,
            updated_at=model.updated_at
        )

@strawberry.input
class CartInput:
    name: str
    price: float
    quantity: int

@strawberry.type
class Query:
    @strawberry.field
    def cart(self, cart_id: int) -> Optional[CartType]:
        cart = ShoppingCart.query.get(cart_id)
        return CartType.from_model(cart) if cart else None

    @strawberry.field
    def carts(self) -> List[CartType]:
        carts = ShoppingCart.query.all()
        return [CartType.from_model(cart) for cart in carts]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_cart(self, cart_data: CartInput) -> CartType:
        cart = ShoppingCart(
            name=cart_data.name,
            price=cart_data.price,
            quantity=cart_data.quantity
        )
        db.session.add(cart)
        db.session.commit()
        return CartType.from_model(cart)

    @strawberry.mutation
    def update_cart(self, cart_id: int, cart_data: CartInput) -> Optional[CartType]:
        cart = ShoppingCart.query.get(cart_id)
        if cart:
            cart.name = cart_data.name
            cart.price = cart_data.price
            cart.quantity = cart_data.quantity
            db.session.commit()
            return CartType.from_model(cart)
        return None

    @strawberry.mutation
    def delete_cart(self, cart_id: int) -> bool:
        cart = ShoppingCart.query.get(cart_id)
        if cart:
            db.session.delete(cart)
            db.session.commit()
            return True
        return False