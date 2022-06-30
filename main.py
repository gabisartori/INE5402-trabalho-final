from User import *
from posts.Post import *
from posts.TextPost import *

def register_user(user_list):
    name = input("Enter your name: ")
    private = input("Is your profile private? (y/n): ").strip()[0].lower() == 'y'
    user = User(name, len(user_list), private)
    user_list.append(user)
    print("User registered successfully!")

# :?:??????
def set_post_list(user_list):
    temp = []
    for user in user_list:
        for post in user.posts:
            temp.append(post)

    return temp

def main():
    user_list = []
    register_user(user_list)
    post_list = set_post_list(user_list)
    eu = user_list[0]

    post = TextPost(eu, "Hello World!", "This is my first post!")
    eu.add_post(post)

    for post in eu.posts:
        print(post.private)

if __name__ == '__main__': main()