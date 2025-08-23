import time

class SimpleLogger:
    def __init__(self, name: str = "App"):
        self.name = name

    def start(self, method_name: str):
        print(f"[{self.name}] | {method_name} | START | {time.strftime('%Y-%m-%d %H:%M:%S')}")

    def message(self, method_name: str, msg: str):
        print(f"[{self.name}] | {method_name} | MESSAGE | {msg}")

    def end(self, method_name: str):
        print(f"[{self.name}] | {method_name} | END | {time.strftime('%Y-%m-%d %H:%M:%S')}")
