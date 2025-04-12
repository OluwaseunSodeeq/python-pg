# Advance Python Decorators Functions
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated(func):
    def wrapper(*args, **kwargs):
        new_user = args[0]
        if new_user.is_logged_in == True:
            return func()
    return wrapper()

@is_authenticated
def create_blog_post(user, blog_post):
    if user.is_logged_in:
        print(f"Blog post '{blog_post}' created by {user.name}.")
    else:
        print(f"{user.name} is not logged in. Cannot create blog post.")





new_user = User("Tobi")
new_user.is_logged_in = True
create_blog_post(new_user, "My First Blog Post")
#     app.run(debug=True, port=5000)

# NOTE
# **kwargs — Keyword (named) arguments
# both allow you to pass a variable number of keyword arguments to a function.
# The **kwargs syntax allows you to pass a dictionary of key-value pairs to the function, 
# where the keys are the names of the arguments and the values are their corresponding values.
# The difference is that *args is used for positional arguments, while **kwargs is used for keyword arguments.

# *args examples:
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

greet("Seun", "Oluwatobiloba", "Rafael")

# **kwargs examples:
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

profile(name="Seun", age=23, location="Lagos")
