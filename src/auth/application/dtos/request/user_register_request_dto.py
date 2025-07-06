class UserRegisterRequestDto:

    def __init__(self, email: str, name: str, password: str):
        self.email = email
        self.name = name
        self.password = password