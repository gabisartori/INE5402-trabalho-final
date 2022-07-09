from user import *
from posts.Post import *
from posts.TextPost import *
from functions import *

def main():
    user_list = []
    register_user(user_list)
    me = user_list[0]
    me.add_post(TextPost(me, "Hello World!", "This is my first post!"))
    me.comment(me.posts[0], "This is a comment!")
    show_timeline(me, me.posts)

if __name__ == '__main__': main()
