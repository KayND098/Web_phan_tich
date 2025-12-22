import csv
import os

users = {}
current_user = None
DB_PATH = os.path.join("database", "acc.csv")

def load_users():
    global users
    if os.path.exists(DB_PATH):
        with open(DB_PATH, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)   
            for row in reader:
                username = row["username"]
                users[username] = {
                    "email": row["email"],
                    "phone": row["phone"],
                    "is_paid": row["is_paid"] == "Yes",
                    "password": row["password"],
                    "logged_in": False
                }

def save_to_csv(email, username, phone, is_paid, password):
    os.makedirs("database", exist_ok=True)
    file_exists = os.path.exists(DB_PATH)

    with open(DB_PATH, mode="a", newline="", encoding="utf-8") as f:
        fieldnames = ["email", "username", "phone", "is_paid", "password"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Nếu file chưa tồn tại thì ghi header trước
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "email": email,
            "username": username,
            "phone": phone,
            "is_paid": "Yes" if is_paid else "No",
            "password": password
        })

def register(email, phone, is_paid=False, password="", username=""):
    global users
    if username in users:
        return " Tên đăng nhập đã tồn tại!"
    users[username] = {
        "email": email,
        "phone": phone,
        "is_paid": is_paid,
        "password": password,
        "logged_in": False
    }
    save_to_csv(email, username, phone, is_paid, password)
    return f" Đăng ký thành công cho {username}, trả phí: {is_paid}"

def login(username, password):
    global users, current_user
    if username not in users:
        return " Tên đăng nhập chưa được đăng ký!"
    if users[username]["password"] != password:
        return " Mật khẩu không chính xác!"
    users[username]["logged_in"] = True
    current_user = username
    return f" {username} đã đăng nhập thành công!"

def logout():
    global users, current_user
    if current_user is None:
        return " Không có ai đang đăng nhập!"
    users[current_user]["logged_in"] = False
    msg = f" {current_user} đã đăng xuất!"
    current_user = None
    return msg

load_users()