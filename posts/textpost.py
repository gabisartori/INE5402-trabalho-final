from posts.post import Post

class TextPost(Post):
    def __init__(self, owner, title, content):
        super().__init__(owner)
        self.title = title
        self.content = content

    def show_post(self):
        print('='*30)
        if self.title:
            print(self.owner.name + ": " + self.title)
        else:
            print(self.owner.name + " respondeu:")
        print(self.content)
        print("Likes: " + str(self.likes))

    def comment_menu(self, user):
        comment = input('Digite o comentário: ')
        reply = TextPost(user, '', comment)
        self.add_reply(reply)
    