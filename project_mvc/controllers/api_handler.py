import random

# Simulasi data dari database
users = [
    {"id": 1, "name": "Admin"},
    {"id": 2, "name": "User"}
]


def get_users():

    # simulasi server sibuk
    error_chance = random.randint(1, 3)

    if error_chance == 1:
        return {
            "status": "error",
            "message": "Server sedang sibuk, coba lagi nanti"
        }

    return {
        "status": "success",
        "data": users
    }
