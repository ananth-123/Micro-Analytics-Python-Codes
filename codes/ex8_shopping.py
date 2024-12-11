from collections import defaultdict

def show_menu():
    print("\nShopping List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Clear list")
    print("5. Exit")

def main():
    cart = defaultdict(int)
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            item = input("Enter item to add: ").lower()
            cart[item] += 1
            print(f"Added: {item} (Quantity: {cart[item]})")
            
        elif choice == '2':
            if not cart:
                print("Cart is empty!")
                continue
            item = input("Enter item to remove: ").lower()
            if item in cart:
                cart.pop(item)
                print(f"Removed: {item}")
            else:
                print("Item not found!")
                
        elif choice == '3':
            if not cart:
                print("Cart is empty!")
            else:
                print("\nYour Shopping Cart:")
                for item, qty in cart.items():
                    print(f"{item}: {qty}")
                    
        elif choice == '4':
            cart.clear()
            print("Cart cleared!")
            
        elif choice == '5':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
