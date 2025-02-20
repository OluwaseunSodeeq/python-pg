class User:
    def __init__(self,username,complexion):
        # default Attributes below
        self.complexion = complexion
        self.username = username
        print("the constructor or the init function and it runs every time this class create an object.")

# first Object
user_1= User("Oluwaseun","Chocolate")
user_1.id = "212"
user_1.lastname = "Sodeeq"
print(f"My name is {user_1.username} {user_1.lastname} and my id num is {user_1.id}")

# Second Object
user_friend = User("Malik","Dark")
user_friend.id = "304"
user_friend.lastname = "Muhammed"
print(f"My name is {user_friend.username} {user_friend.lastname} and my id num is {user_friend.id}")

