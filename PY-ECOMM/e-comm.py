# Dummy product data (id, name, category, price)
products = [
    {'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 1000},
    {'id': 2, 'name': 'Smartphone', 'category': 'Electronics', 'price': 700},
    {'id': 3, 'name': 'Shoes', 'category': 'Fashion', 'price': 50},
    {'id': 4, 'name': 'T-shirt', 'category': 'Fashion', 'price': 20},
    {'id': 5, 'name': 'Headphones', 'category': 'Electronics', 'price': 150},
    {'id': 6, 'name': 'Jacket', 'category': 'Fashion', 'price': 100},
]

def search_product(name):
    result = [product for product in products if name.lower() in product['name'].lower()]
    return result

def filter_by_category(category):
    result = [product for product in products if category.lower() in product['category'].lower()]
    return result

def sort_products_by_price(order='asc'):
    if order == 'asc':
        return sorted(products, key=lambda x: x['price'])
    elif order == 'desc':
        return sorted(products, key=lambda x: x['price'], reverse=True)
    else:
        return products

def ecommerce_system():
    while True:
        print("\nE-commerce System:")
        print("1. Search Products")
        print("2. Filter Products by Category")
        print("3. Sort Products by Price")
        print("4. View All Products")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            search_term = input("Enter product name to search: ")
            results = search_product(search_term)
            if results:
                print("\nSearch Results:")
                for product in results:
                    print(f"{product['id']}. {product['name']} - {product['category']} - ${product['price']}")
            else:
                print("No products found.")

        elif choice == '2':
            category = input("Enter category to filter by: ")
            results = filter_by_category(category)
            if results:
                print("\nFiltered Results:")
                for product in results:
                    print(f"{product['id']}. {product['name']} - {product['category']} - ${product['price']}")
            else:
                print("No products found in that category.")

        elif choice == '3':
            order = input("Enter 'asc' for ascending or 'desc' for descending: ")
            sorted_products = sort_products_by_price(order)
            print("\nSorted Products by Price:")
            for product in sorted_products:
                print(f"{product['id']}. {product['name']} - {product['category']} - ${product['price']}")

        elif choice == '4':
            print("\nAll Products:")
            for product in products:
                print(f"{product['id']}. {product['name']} - {product['category']} - ${product['price']}")

        elif choice == '5':
            print("Exiting the e-commerce system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ecommerce_system()
