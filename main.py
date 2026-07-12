import products
from store import Store


def main():
    product_list = [
        products.Product(
            "MacBook Air M2",
            price=1450,
            quantity=100,
            active=True
        ),
        products.Product(
            "Bose QuietComfort Earbuds",
            price=250,
            quantity=500,
            active=True
        ),
        products.Product(
            "Google Pixel 7",
            price=500,
            quantity=250,
            active=True
        ),
    ]

    best_buy = Store(product_list)

    active_products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())

    total_price = best_buy.order([
        (active_products[0], 1),
        (active_products[1], 2)
    ])

    print(total_price)


if __name__ == "__main__":
    main()