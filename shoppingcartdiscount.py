#This code calculates and apply given discount to a customer purchase

def discount_rate(rate_discounted: int):

    def total_cost():
        cart_list = input("Enter the price of each item bought, seperated by a comma and space\n")
        anew_cart = cart_list.split(", ")
        a_list_item = []
        for i in anew_cart:
            new_cart = int(i)
            a_list_item.append(new_cart)
        sum_item_price = 0
        for price in a_list_item:
            sum_item_price += price
        return sum_item_price
    total = total_cost()
    discounted_price = (total * rate_discounted) / 100
    final_cost = total - discounted_price
    print(f"You have received a discount of {discounted_price:.2f} and your total payment due is {final_cost:.2f}")
discount_rate(10)