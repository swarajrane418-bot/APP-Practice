class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UpiPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class CashPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")

class ShoppingCart:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def checkout(self, amount):
        self.payment_method.pay(amount)

cart = ShoppingCart(UpiPayment())
cart.checkout(1500)

cart = ShoppingCart(CreditCardPayment())
cart.checkout(2000)

cart = ShoppingCart(CashPayment())
cart.checkout(500)