import os

from project_mvc.controllers.api_handler import get_users
from project_mvc.views.dashboard_component import (
    fetch_data_from_api,
    render_dashboard
)

# Membaca variabel environment
user_name = os.getenv("APP_USER", "Guest")
app_env = os.getenv("APP_ENV", "development")

# Simulasi State
app_state = {
    "items": [],
    "is_loading": True
}


def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False


if __name__ == "__main__":

    print(f"Halo {user_name}! Aplikasi ini berjalan di dalam kontainer Docker.")
    print(f"Environment: {app_env}")

    # kondisi loading
    render_dashboard(
        app_state["items"],
        app_state["is_loading"]
    )

    # Integrasi Frontend - Backend
    data = fetch_data_from_api(get_users)

    if data:
        update_state(data)

    # kondisi data tampil
    render_dashboard(
        app_state["items"],
        app_state["is_loading"]
    )
