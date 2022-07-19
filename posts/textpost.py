from posts.post import Post

class TextPost(Post):
    def __init__(self, owner, title, content):
        super().__init__(owner)
        self.title = title
        self.content = content

    def show_post(self):
        '''Mostra a publicação na tela de forma organizada'''
        print('='*30)
        if self.get_title():
            print(self.get_owner().get_name() + ": " + self.get_title())
        else:
            print(self.get_owner().get_name() + " respondeu:")
        print(self.get_content())
        print("Likes: " + str(self.get_likes()))

    def comment_menu(self, user):
        '''Adiciona um TextPost como comentário na lista de respostas do post'''
        comment = input('Digite o comentário: ')
        reply = TextPost(user, '', comment)
        self.add_reply(reply)
    
    def set_title(self, title):
        '''Define o título da publicação'''
        self.title = title
    
    def set_content(self, content):
        '''Define o conteúdo da publicação'''
        self.content = content
    
    def get_title(self):
        '''Retorna o título da publicação'''
        return self.title
    
    def get_content(self):
        '''Retorna o conteúdo da publicação'''
        return self.content
    