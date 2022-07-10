from user import *
from posts.post import *
from posts.textpost import *
import hashlib
    

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
