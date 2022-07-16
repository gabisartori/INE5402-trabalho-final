from posts.post import Post
from posts.textpost import TextPost

class ImagePost(Post):
    def __init__(self, owner, title, image_link):
        super().__init__(owner)
        self.title = title
        self.image_link = image_link
    
    def show_post(self):
        print('='*30)
        print(self.owner.name + ": " + self.title)
        file = open(f'ascii_arts/{self.image_link}.txt', 'r')
        for line in file:
            print(line, end='')
        print()
        
        print("Likes: " + str(self.likes))

    def comment_menu(self, user):
        comment = input('Digite o comentário: ')
        reply = TextPost(user, '', comment)
        self.add_reply(reply)
    