from user import *
from posts.Post import *
from posts.TextPost import *
import hashlib



# Todo otimizar isso aí
def register_user(user_list):
    name = input("Insira seu nome de usuário: ")
    private = input("Essa conta será privada? (s/n): ").strip()[0].lower() == 's'
    password = input("Insira sua senha: ")
    if password == input('Confira sua senha: '):
        user = User(name, len(user_list), private, password)
        user_list.append(user)
        print("User registered successfully!")
    else:
        print('Senhas não conferem! Tente novamente.')
        register_user(user_list)
    

def queryPost(id, post_list):
    for post in post_list:
        if post.id == id:
            return post

# :?:??????
def set_post_list(user_list):
    temp = []
    for user in user_list:
        for post in user.posts:
            temp.append(post)

    return temp

def show_post_replies(post):
    pass

def show_post(post: Post):
    print('='*30)
    if post.title:
        print(post.owner.name + ": " + post.title)
    print(post.content)
    print("Likes: " + str(post.likes))
    show_post_replies(post)
    
def show_timeline(user, posts):
    for post in posts:
        if not post.private or post.owner == user:
            show_post(post)
