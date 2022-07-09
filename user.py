from posts.TextPost import TextPost
import hashlib

def sha256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


class User:
    def __init__(self, name, id, private, password_hash) -> None:
        self.name = name
        self.id = id,
        self.posts = []
        self.private = private
        self.password = password_hash

    def add_post(self, post) -> None:
        self.posts.append(post)
    
    def build_feed(self, all_posts) -> None:
        for post in all_posts:
            if not post.owner.private: print(post.content) 
    
    def build_my_feed(self):
        for post in self.posts:
            print(post)
    
    def comment(self, post, comment):
        post.add_reply(TextPost(self, '', comment))
