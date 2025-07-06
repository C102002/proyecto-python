
class UserUpdateRequestDto:

    def __init__(self, id: str, email: str | None = None, name: str | None = None, password: str | None = None):
        self.id = id
        self.email = email
        self.name = name
        self.password = password