from src.auth.application.dtos.request.user_register_request_dto import UserRegisterRequestDto

class UserRegisterRequestMockDto(UserRegisterRequestDto):
    
    def __init__(self, email: str, name: str, password: str, role: str):
        super().__init__(email, name, password)
        self.role = role