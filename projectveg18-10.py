print('*' * 5, 'WELCOME TO VEGETABLE MARKET', '*' * 5)

# Initializing data or variables
vegetables = ['brinjal', 'tomato', 'drumstick', 'onion']
quantity = [10, 35, 10, 50]
cost_price = [30, 15, 30, 20]
selling_price = [40, 20, 50, 30]
cart_customer = []
quantity_customer = []
owner_username = 'sai@1234'
owner_password = '1234'
cus_cnt=0

while True:
    print("1. OWNER")
    print("2. CUSTOMER")
    ch = int(input("Enter 1 for OWNER or 2 for CUSTOMER: "))

    if ch == 1:
        # Owner section
        user_name = input("Enter your username: ")
        password = input("Enter your password: ")

        if user_name == owner_username and password == owner_password:
            while True:
                print("Owner Menu:")
                print("1. Add vegetables")
                print("2. Remove vegetables")
                print("3. Display stock")
                print("4. Modify stock quantities")
                print("5. Profit report")
                print("6.Customers count")
                print("7. Close shop")
                owner_choice = int(input("Enter your choice: "))

                # Add vegetables
                if owner_choice == 1:
                    while True:
                        veg_add = input("Enter the vegetable you want to add: ")
                        if veg_add in vegetables:
                            print(veg_add, "is already available.")
                        else:
                            vegetables.append(veg_add)
                            kgs = float(input(f"Enter number of kgs for {veg_add}: "))
                            quantity.append(kgs)
                            price=int(input("enter cost price of new vegitable"))
                            cost_price.append(price)
                            sell_price=int(input('enter the selling price of new vegitable'))
                            selling_price.append(sell_price)
                        again_add = input("Do you want to add more vegetables? (yes/no): ")
                        if again_add.lower() == 'no':
                            break

                # Remove vegetables
                elif owner_choice == 2:
                    while True:
                        veg_remove = input("Enter the vegetable you want to remove: ")
                        if veg_remove in vegetables:
                            idx = vegetables.index(veg_remove)
                            vegetables.pop(idx)
                            quantity.pop(idx)
                            print(veg_remove, "removed from stock.")
                        else:
                            print(veg_remove, "is not available.")
                        again_remove = input("Do you want to remove more vegetables? (yes/no): ")
                        if again_remove.lower() == 'no':
                            break

                # Display stock
                elif owner_choice == 3:
                    print("*" * 10, 'VEGETABLES AVAILABLE', "*" * 10)
                    for v, q, p in zip(vegetables, quantity, selling_price):
                        print(v, q, 'kgs @ Rs.', p, 'per kg')

                # Modify stock quantities
                elif owner_choice == 4:
                    veg_modify = input("Enter the vegetable whose quantity you want to modify: ")
                    if veg_modify in vegetables:
                        idx = vegetables.index(veg_modify)
                        new_qty = float(input("Enter new quantity: "))
                        quantity[idx] = new_qty
                        print(f"Quantity of {veg_modify} updated to {new_qty} kgs.")
                    else:
                        print(veg_modify, "is not available.")

                # Profit report
                elif owner_choice == 5:
                    total_profit = 0
                    print("*" * 10, 'PROFIT REPORT', "*" * 10)
                    for veg, qty, cus_qty in zip(vegetables, quantity, quantity_customer):
                        veg_index = vegetables.index(veg)
                        profit_per_kg = selling_price[veg_index] - cost_price[veg_index]
                        item_profit = profit_per_kg * cus_qty
                        total_profit += item_profit
                        print(f"{veg}: {cus_qty} kgs sold, Profit: Rs. {item_profit}")
                    print("Total Profit: Rs.", total_profit)
                #customers count
                elif owner_choice==6:
                    
                    print("total customers count is ", cus_cnt)

                # Close shop
                elif owner_choice == 7:
                    passward=input("enter your passward")
                
                    if passward == owner_password:
                        
                        print("The shop is now closed for the day.")
                        break
                    else:
                        print("enter correct password")
        

                else:
                    print("Invalid choice! Please try again.")
        else:
            print("Invalid username or password.")
        break

    elif ch == 2:
        # Customer section
        customer_name = input("Enter your name: ")
        customer_mobile = input("Enter your mobile number: ")
        cus_cnt=0

        if len(customer_mobile) == 10 and customer_mobile.isdigit():
            cus_cnt=cus_cnt+1
            while True:
                print("Customer Menu:")
                print("1. Display available vegetables")
                print("2. Add vegetables to your cart")
                print("3. Remove vegetables from your cart")
                print("4. Modify quantities in your cart")
                print("5. Display your cart")
                print("6. Display customer name and mobile number")
                print("7. Bill and Checkout")
                print("8. Exit")
                
                customer_choice = int(input("Enter your choice: "))

                # Display available vegetables
                if customer_choice == 1:
                    print("*" * 10, 'VEGETABLES AVAILABLE', "*" * 10)
                    for v, q, p in zip(vegetables, quantity, selling_price):
                        print(v, q, 'kgs @ Rs.', p, 'per kg')

                # Add vegetables to the cart
                elif customer_choice == 2:
                    while True:
                        print("*" * 10, 'VEGETABLES AVAILABLE', "*" * 10)
                        for v, q, p in zip(vegetables, quantity, selling_price):
                            print(v, q, 'kgs @ Rs.', p, 'per kg')
                        veg_add_cus = input("Enter the vegetable you want to add: ")
                        if veg_add_cus in vegetables:
                            veg_index = vegetables.index(veg_add_cus)
                            qty_cus_veg = float(input(f"Enter how many kgs of {veg_add_cus} you want to add: "))
                            if qty_cus_veg <= quantity[veg_index]:
                                cart_customer.append(veg_add_cus)
                                quantity_customer.append(qty_cus_veg)
                                quantity[veg_index] -= qty_cus_veg
                            else:
                                print("Sorry, we don't have that much quantity. Available:", quantity[veg_index])
                        else:
                            print(veg_add_cus, "is not available.")
                        again_add = input("Do you want to add more vegetables? (yes/no): ")
                        if again_add.lower() == 'no':
                            break

                # Remove vegetables from the cart
                elif customer_choice == 3:
                    while True:
                        veg_remove_cus = input("Enter the vegetable you want to remove: ")
                        if veg_remove_cus in cart_customer:
                            idx = cart_customer.index(veg_remove_cus)
                            cart_customer.pop(idx)
                            quantity_customer.pop(idx)
                            print(veg_remove_cus, "removed from your cart.")
                        else:
                            print(veg_remove_cus, "is not in your cart.")
                        again_remove = input("Do you want to remove more vegetables? (yes/no): ")
                        if again_remove.lower() == 'no':
                            break

                # Modify quantities in the cart
                elif customer_choice == 4:
                    veg_modify_cus = input("Enter the vegetable whose quantity you want to modify: ")
                    if veg_modify_cus in cart_customer:
                        idx = cart_customer.index(veg_modify_cus)
                        new_qty = float(input("Enter new quantity: "))
                        quantity_customer[idx] = new_qty
                        print(f"Quantity of {veg_modify_cus} updated to {new_qty} kgs.")
                    else:
                        print(veg_modify_cus, "is not in your cart.")

                # Display customer cart
                elif customer_choice == 5:
                    print("*" * 10, 'CUSTOMER CART', "*" * 10)
                    for v, q in zip(cart_customer, quantity_customer):
                        print(v, q, 'kgs')

                # Display customer name and mobile number
                elif customer_choice == 6:
                    print("Customer Name:", customer_name)
                    print("Mobile Number:", customer_mobile)

                # Bill and Checkout
                elif customer_choice == 7:
                    total_amount = 0
                    print("*" * 10, 'BILL', "*" * 10)
                    for veg, qty in zip(cart_customer, quantity_customer):
                        veg_index = vegetables.index(veg)
                        price_per_kg = selling_price[veg_index]
                        amount = qty * price_per_kg
                        total_amount += amount
                        print(veg,':',qty,' kgs @ Rs. ',price_per_kg,' per kg = Rs. ',amount)
                    print("Total Bill Amount: Rs.", total_amount)
                    break

                # Exit
                elif customer_choice == 8:
                    break

                else:
                    print("Invalid choice! Please try again.")
        else:
            print("Invalid mobile number. Please try again.")
