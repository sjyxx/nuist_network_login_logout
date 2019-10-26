import requests


def logout():
    url = 'http://a.nuist.edu.cn/index.php/index/logout'
    try:
        r = requests.post(url, timeout=30)
        r.raise_for_status()

        return r.json()['info']
    except:
        print('error')


# def main():
print(logout())
