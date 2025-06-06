import requests

BASE_URL = "http://127.0.0.1:8000/api"
TOKEN = None  # access token сохранится сюда после логина


def login(username: str, password: str):
    global TOKEN
    url = f"{BASE_URL}/token/"
    response = requests.post(url, json={"username": username, "password": password})
    response.raise_for_status()
    data = response.json()
    TOKEN = data["access"]
    print("Logged in successfully. Token saved.")


def get_headers():
    if not TOKEN:
        raise ValueError("Сначала вызови функцию login() для получения токена.")
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }


def create_expense(amount: float, category_id: int, description: str, date: str):
    url = f"{BASE_URL}/expenses/create/"
    payload = {
        "amount": amount,
        "category": category_id,
        "description": description,
        "date": date
    }
    response = requests.post(url, json=payload, headers=get_headers())
    response.raise_for_status()
    return response.json()


def create_income(amount: float, source: str, description: str, date: str):
    url = f"{BASE_URL}/incomes/create/"
    payload = {
        "amount": amount,
        "source": source,
        "description": description,
        "date": date
    }
    response = requests.post(url, json=payload, headers=get_headers())
    response.raise_for_status()
    return response.json()


def get_summary(date_after=None, date_before=None):
    url = f"{BASE_URL}/summary/"
    params = {}
    if date_after:
        params["date_after"] = date_after
    if date_before:
        params["date_before"] = date_before

    response = requests.get(url, headers=get_headers(), params=params)
    response.raise_for_status()
    return response.json()


# Пример использования
if __name__ == "__main__":
    # Введи реальные username/password
    login("admin", "admin")

    # Примеры вызова функций
    print(create_expense(1000, category_id=1, description="Кофе и обед", date="2025-06-06"))
    print(create_income(5000, source="Фриланс", description="Проект", date="2025-06-05"))
    print(get_summary(date_after="2025-06-01", date_before="2025-06-30"))
