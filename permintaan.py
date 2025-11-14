import requests

def mendapatkan(url):
    try:
        respon = requests.get(url)
        respon.raise_for_status()
        return respon
    except Exception as e:
        print("Gagal mengambil data:", e)
        return None
