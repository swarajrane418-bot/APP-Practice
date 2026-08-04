from abc import ABC, abstractmethod

# Abstraction
class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Low-level module
class EmailService(MessageService):
    def send(self, message):
        print(f"Email: {message}")


# Another low-level module
class SMSService(MessageService):
    def send(self, message):
        print(f"SMS: {message}")


# High-level module
class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send(message)


# Usage
email = EmailService()
notification = Notification(email)
notification.notify("Order placed successfully!")

sms = SMSService()
notification = Notification(sms)
notification.notify("Payment received!")