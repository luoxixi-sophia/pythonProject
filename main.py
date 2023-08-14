import hashlib
import time
import requests
import base64
from Crypto.Cipher import AES
from Crypto.Hash import MD5


class Youdao():
    def __init__(self):
        self.url = 'https://dict.youdao.com/webtranslate'

    def get_enmes(self, input_data):
        mysticTime = str(int(time.time() * 1000))
        data = "client=fanyideskweb&mysticTime={}&product=webfanyi&key=fsdsogkndfokasodnaso".format(mysticTime)
        sign = hashlib.md5(data.encode(encoding='utf-8')).hexdigest()  # python中的MD5 加密
        data = {
            'i': input_data,
            'from': 'auto',
            'to': '',
            'dictResult': 'true',
            'keyid': 'webfanyi',
            'sign': sign,
            'client': 'fanyideskweb',
            'product': 'webfanyi',
            'appVersion': '1.0.0',
            'vendor': 'web',
            'pointParam': 'client,mysticTime,product',
            'mysticTime': mysticTime,
            'keyfrom': 'fanyi.web'
        }
        headers = {
            'Referer': "https://fanyi.youdao.com",
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/113.0.0.0 Safari/537.36",
        }
        cookies = {
            "OUTFOX_SEARCH_USER_ID": "-390346570@10.110.96.160",
            "OUTFOX_SEARCH_USER_ID_NCOO": "1229562063.3960004"
        }
        response = requests.post(self.url, headers=headers, data=data, cookies=cookies).text
        decode_mes = self.decrypt_data(response)
        print(decode_mes)

    def decrypt_data(self, encrypted_data):
        key = b"ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
        iv = b"ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"
        cryptor = AES.new(
            MD5.new(key).digest()[:16], AES.MODE_CBC, MD5.new(iv).digest()[:16]
        )
        decode_mes = cryptor.decrypt(base64.urlsafe_b64decode(encrypted_data)).decode("utf-8")
        return decode_mes


def start():
    input_data = input('请输入要翻译内容：')
    op.get_enmes(input_data)


if __name__ == '__main__':
    op = Youdao()
    start()