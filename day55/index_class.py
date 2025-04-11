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