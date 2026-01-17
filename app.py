from datetime import datetime

def greet(name):
    current_time = datetime.now().strftime("%H:%M")
    return f"Hello, {name}! Current time is {current_time}"

if __name__ == "__main__":
    user = "World"
    print(greet(user))
