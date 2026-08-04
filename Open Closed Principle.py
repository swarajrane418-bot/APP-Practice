from abc import ABC, abstractmethod

# Abstract Base Class
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Existing payment methods
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


# New payment method added without modifying existing code
class BitcoinPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Bitcoin")


# Usage
payments = [
    CreditCardPayment(),
    UPIPayment(),
    PayPalPayment(),
    BitcoinPayment()
]

for payment in payments:
    payment.pay(1000)