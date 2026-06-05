from dataclasses import dataclass

# 1. Это аналог struct в Rust. Мы жестко задаем типы полей.
@dataclass
class User:
    user_id: int
    name: str
    email: str
    is_active: bool = True  # Поле со значением по умолчанию

# 2. Строгая функция. Мы говорим: "принимает ТОЛЬКО User, возвращает ТОЛЬКО str"
def greet_user(user: User) -> str:
    if not user.is_active:
        return f"Пользователь {user.name} заблокирован."
    
    return f"Привет, {user.name} ({user.email})!"

# 3. Точка входа
# if __name__ == "__main__":
   