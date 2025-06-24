class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


class Logger(Singleton):
    def __init__(self):
        self.logs = []

    def log(self, message: str):
        self.logs.append(message)

    def get_logs(self):
        return self.logs


logger1 = Logger()
logger2 = Logger()

logger1.log('message1')
logger2.log('message2')

assert logger1 is logger2, 'this is not a singleton'
assert logger1.get_logs() == ['message1', 'message2']



