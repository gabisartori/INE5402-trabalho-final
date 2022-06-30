from User import *
from posts.Post import *
from posts.TextPost import *

def register_user(user_list):
    name = input("Enter your name: ")
    private = input("Is your profile private? (y/n): ").strip()[0].lower() == 'y'
    user = User(name, private)
    user_list.append(user)
    print("User registered successfully!")


def main():
    user_list = []
    post_list = []
    register_user(user_list)

    eu = user_list[0]

    post = TextPost(eu, "Hello World!", "This is my first post!")
    eu.add_post(post)

    for post in eu.posts:
        print(post.private)

if __name__ == '__main__': main()