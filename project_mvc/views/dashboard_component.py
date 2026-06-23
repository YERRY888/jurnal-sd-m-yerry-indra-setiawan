def fetch_data_from_api(api_function):

    print("[System] Mencoba menghubungkan ke API...")

    try:
        response = api_function()

        if response["status"] == "success":
            print("[System] Data berhasil diterima")
            return response["data"]

        else:
            print(
                f"[Error API] {response['message']}"
            )
            return None


    except Exception as e:

        print(
            f"[System Error] Gagal mengambil data: {e}"
        )

        return None



def render_dashboard(data_list, is_loading=False):

    print("--- DASHBOARD APLIKASI ---")

    if is_loading:
        print("Mohon Tunggu...")

    elif not data_list:
        print("[!] Tidak ada data tersedia")

    else:
        for item in data_list:
            print(
                f"- Item ID: {item['id']} | Nama: {item['name']}"
            )
