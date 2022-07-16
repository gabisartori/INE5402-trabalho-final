import time

class Post:
    
    post_options = '''==============================
[0] Sair
[1] Curtir
[2] Comentar
[3] Mostrar respostas
'''
    
    def __init__(self, owner):
        self.likes = 0
        self.owner = owner
        self.replies = []
        self.liked_by = []
        self.private = self.owner.private
        self.created_at = time.time()

    def add_like(self, user_email):
        self.likes += 1
        self.liked_by.append(user_email)

    def add_reply(self, reply):
        self.replies.insert(0, reply)