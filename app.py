from project_mvc.controllers.api_handler import get_users
from project_mvc.views.dashboard_component import (
    fetch_data_from_api,
    render_dashboard
)

# Simulasi State
app_state = {
    "items": [],
    "is_loading": True
}


def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False


if __name__ == "__main__":

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
