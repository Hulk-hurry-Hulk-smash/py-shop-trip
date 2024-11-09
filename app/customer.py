from typing import Dict, Tuple
from app.car import Car
from app.shop import Shop
from app.config import config
from datetime import datetime  # Імпортуємо тільки datetime

class Customer:
    def __init__(
        self,
        name: str,
        location: Tuple[int, int],
        money: float,
        product_cart: Dict[str, int],
        car: Car
    ) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car = car

    def calculate_distance(self, shop_location: Tuple[int, int]) -> float:
        return (
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2
        ) ** 0.5

    def calculate_fuel_cost(self, distance: float) -> float:
        return (distance / 100) * self.car.fuel_consumption * \
            config["FUEL_PRICE"]

    def make_purchase(self, shop: Shop) -> None:
        # Використання datetime.now() після заміни через monkeypatch
        print(f"\nDate: {datetime.now():%d/%m/%Y %H:%M:%S}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in self.product_cart.items():
            product_price = shop.products.get(product, 0)
            cost = product_price * quantity
            print(f"{quantity} {product} for {cost} dollars")
            total_cost += cost

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        self.money -= total_cost

    def return_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars\n")
