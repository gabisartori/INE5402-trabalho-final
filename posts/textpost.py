from posts.post import Post

class TextPost(Post):
    def __init__(self, owner, title, content):
        super().__init__(owner)
        self.title = title
        self.content = content

    def show_post(self,):
        print('='*30)
        if self.title:
            print(self.owner.name + ": " + self.title)
            print(self.content)
            print("Likes: " + str(self.likes))
            self.show_post_replies(self)
        
    def show_post_replies(self, post):
        pass

    