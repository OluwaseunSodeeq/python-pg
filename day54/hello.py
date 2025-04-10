from flask import Flask
import time
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# if __name __ == "__hello__":
#     app.run()


# First class object: passing a function as a value
def add(n1,n2):
    return n1 + n2

def operations(n1,n2,func):
    return func(n1,n2)

operations(2,3,add)

# Function can be returned from another function
def outer_function():
    def inner_function():
        return print("Hello, I'm inside the outer function")
    print("Hello, I'm outside the outer function")
    # inner_function()
    return inner_function

result = outer_function()
print(result)


# PYTHON DECORATORS
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

def delay_decorator(func):
    def wrapper_function():
        time.sleep(2)
        return func()
    return wrapper_function

@delay_decorator # this will run after 2 seconds of being called.
def say_hello():
    return "Hello!"

@delay_decorator
def say_bye():
    return "Bye!"

def say_hello_bye():
    return "Hello and Bye!"