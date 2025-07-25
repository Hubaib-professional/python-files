# app.py

def greet(name):
    """
    Returns a greeting message.
    """
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"

def add(a, b):
    """
    Adds two numbers and returns the sum.
    """
    return a + b

if __name__ == "__main__":
    # This block will only run when app.py is executed directly
    print(greet("CI/CD Learner"))
    print(f"2 + 3 = {add(2, 3)}")
```python