if __name__ == '__main__':
    from Post import Post
else: from posts.Post import Post

class TextPost(Post):
    def __init__(self, owner, title, content):
        super().__init__(owner)
        self.title = title
        self.content = content
