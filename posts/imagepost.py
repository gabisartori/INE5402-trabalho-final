if __name__ == '__main__':
    from posts.post import Post
else: from posts.post import Post

class ImagePost(Post):
    def __init__(self, owner, title, image_link):
        super().__init__(owner)
        self.title = title
        self.image_link = image_link