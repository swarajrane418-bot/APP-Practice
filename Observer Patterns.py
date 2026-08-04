class Observer:
    def update(self, message):
        print(f"Observer received message: {message}")


class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

youtuber = Subject()
observer1 = Observer()

youtuber.subscribe(observer1)

youtuber.notify("New video uploaded!")