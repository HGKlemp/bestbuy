import products
from store import Store


def start(best_buy):

    while True:
        print("\n========== Best Buy ==========")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("\nPlease choose a number: ")

        if choice == "1":
            print("\n------ Product List ------")

            product_list = best_buy.get_all_products()

            for index, product in enumerate(product_list, start=1):
                print(f"{index}. ", end="")
                product.show()

        elif choice == "2":
            print(f"\nTotal amount in store: {best_buy.get_total_quantity()}")

        elif choice == "3":

            shopping_list = []
            product_list = best_buy.get_all_products()

            while True:

                print("\n------ Product List ------")

                for index, product in enumerate(product_list, start=1):
                    print(f"{index}. ", end="")
                    product.show()

                product_number = input(
                    "\nEnter product number (or press ENTER to finish): "
                )

                if product_number == "":
                    break

                try:
                    product_number = int(product_number)

                    if product_number < 1 or product_number > len(product_list):
                        print("Invalid product number.")
                        continue

                    quantity = int(input("Enter quantity: "))

                    shopping_list.append(
                        (product_list[product_number - 1], quantity)
                    )

                except ValueError:
                    print("Please enter valid numbers.")

            if len(shopping_list) == 0:
                print("No products selected.")

            else:
                try:
                    total_price = best_buy.order(shopping_list)
                    print(f"\nOrder completed!")
                    print(f"Total price: ${total_price}")

                except ValueError as error:
                    print(error)

        elif choice == "4":
            print("\nGoodbye!")
            break

        else:
            print("Invalid choice.")


def main():

    product_list = [
        products.Product(
            "MacBook Air M2",
            price=1450,
            quantity=100
        ),
        products.Product(
            "Bose QuietComfort Earbuds",
            price=250,
            quantity=500
        ),
        products.Product(
            "Google Pixel 7",
            price=500,
            quantity=250
        )
    ]

    best_buy = Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()