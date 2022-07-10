if __name__ == '__main__':
    from posts.post import Post
else: from posts.post import Post

class TextPost(Post):
    def __init__(self, owner, title, content):
        super().__init__(owner)
        self.title = title
        self.content = content
