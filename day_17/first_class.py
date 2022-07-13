## First Class

class User:
    
    def __init__(self, username, account="Pessoal"):
        print("init called!")
        self.username = username
        self.account = account
        self.followers = 0
        self.followings = 0

    def follow(self, user):
        user.followers += 1
        user.followings += 1

    def add_follower(self, amount=1):
        self.followers += amount

    def print_followers_number(self):
        print(f"Hey {self.username}, you have {self.followers} followers")
# -------- ---------------------------

user_1 = User("Tom")
user_2 = User("Jerry", "Comercial")

print(user_1.username)
print(user_1.account)
print(user_1.followers)
print(user_2.username)
print(user_2.account)
print(user_2.followers)
user_2.add_follower()
user_2.print_followers_number()
user_2.add_follower(9)
user_2.print_followers_number()
user_1.follow(user_2)
user_2.print_followers_number()
