import requests


def quake_resource_search(key, mode):
    headers = {
        "X-QuakeToken": key
    }
    try:
        resp = requests.get(url="https://quake.360.cn/api/v3/user/info", headers=headers, timeout=5)
        if resp.status_code == 401:
            return '[!] Error: API-KEY error.\n'
        data = resp.json()['data']
    except Exception as e:
        print(e)
        return f"{str(e)}\n"
    else:
        if mode == "complete":
            string = f"======== 360Quake ========\n[+] Username: {data['user']['username']}\n[+] Id: {data['id']}\n[+] E-mail: {data['user']['email']}\n[+] Credit: {data['credit']}\n[+] Persistent_credit: {data['persistent_credit']}\n[+] Mobile_phone: {data['mobile_phone']}\n[+] Role: {data['role'][0]['fullname']}\n[+] Ban_status: {data['ban_status']}\n==========================\n"
        elif mode == "easy":
            string = f"[!] Remaining free query quota is {data['credit']}.\n"
        return f"{str(string)}\n"
