from posts.post import Post
from posts.textpost import TextPost

class ImagePost(Post):
    def __init__(self, owner, title, image_link):
        super().__init__(owner)
        self.title = title
        self.image_link = image_link
    
    def show_post(self):
        print('='*30)
        print(self.get_owner().get_name() + ": " + self.get_title())
        file = open(f'ascii_arts/{self.get_image_link()}.txt', 'r')
        for line in file:
            print(line, end='')
        print()
        
        print("Likes: " + str(self.get_likes()))

    def comment_menu(self, user):
        comment = input('Digite o comentário: ')
        reply = TextPost(user, '', comment)
        self.add_reply(reply)
    
    def set_title(self, title):
        '''Define o título da publicação'''
        self.title = title
    
    def set_image_link(self, image_link):
        '''Define o link da imagem'''
        self.image_link = image_link
    
    def get_title(self):
        '''Retorna o título da publicação'''
        return self.title
    
    def get_image_link(self):
        '''Retorna o link da imagem'''
        return self.image_link
