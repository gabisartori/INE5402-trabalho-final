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
            print(self.content)
            print("Likes: " + str(self.likes))
            self.show_post_replies(self)
        
    def show_post_replies(self):
        pass

    def post_menu(self, viewer):
        self.show_post()
        while True:
            print(self.post_options)
            option = input('Digite a opção desejada: ')
            if option == '1':
                # Adiciona uma curtida à publicação
                self.add_like(viewer.email)
                print('Curtida adicionada com sucesso!')
            elif option == '2':
                # Incia o menu de comentar
                self.comment_menu()
            elif option == '3':
                pass
            elif option == '0':
                # Encerra o menu de publicação
                break

    def comment_menu(self, user):
        comment = input('Digite o comentário: ')
        reply = TextPost(user, '', comment)
        self.add_reply(reply)
    