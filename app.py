from views.dashboard_component import render_dashboard

# Simulasi State
app_state = {
    "items": [],
    "is_loading": True
}

def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False

if __name__ == "__main__":
    print("Loading data...")

    data = [
        {"id": 1, "name": "Admin"},
        {"id": 2, "name": "User"}
    ]

    update_state(data)

    render_dashboard(app_state["items"])
