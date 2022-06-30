class Post:
    def __init__(self, owner) -> None:
        self.likes = 0
        self.owner = owner
        self.replies = []
        self.liked_by = []
        self.private = self.owner.private

    def like(self, user_id) -> None:
        self.likes += 1
        self.liked_by.append(user_id)

    def add_reply(self, reply) -> None:
        self.replies.append(reply)
    
