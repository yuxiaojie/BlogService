import base64
import hashlib
from Crypto.Cipher import DES3


MATCH = 1
NOT_FIND = -1
TIME_OUT = -2
MISMATCH = -3

BS = DES3.block_size


def b64decode(content):
    return base64.b64decode(content).decode()


def b64encode(content):
    return base64.b64encode(content.encode()).decode()


def md5(src, upper=False):

    """
        md5加密
    :param src: 原始内容
    :param upper: 结果大小写
    :return:
    """

    md5_tool = hashlib.md5()
    md5_tool.update(src.encode(encoding='utf_8'))

    if upper:
        return md5_tool.hexdigest().upper()
    else:
        return md5_tool.hexdigest()


def sha1(src, upper=False):
    tool = hashlib.sha1()
    tool.update(src.encode('utf-8'))

    if upper:
        return tool.hexdigest().upper()
    else:
        return tool.hexdigest()


def sha256(src, upper=False):
    tool = hashlib.sha256()
    tool.update(src.encode('utf-8'))
    if upper:
        return tool.hexdigest().upper()
    else:
        return tool.hexdigest()


def pad(s):
    return s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()


def unpad(s):
    return s[0:-ord(s[-1])]


class Prpcrypt(object):
    def __init__(self, key, iv):
        self.key = key
        self.mode = DES3.MODE_CBC
        self.iv = iv.encode()

    def encrypt(self, text):
        text = pad(text.encode())
        cryptor = DES3.new(self.key, self.mode, self.iv)
        x = len(text) % 8
        if x != 0:
            text = text + '\0' * (8 - x)
        # print(text)
        self.ciphertext = cryptor.encrypt(text)
        return base64.standard_b64encode(self.ciphertext).decode("utf-8")

    def decrypt(self, text):
        cryptor = DES3.new(self.key, self.mode, self.iv)
        de_text = base64.standard_b64decode(text.encode())
        plain_text = cryptor.decrypt(de_text)
        st = str(plain_text.decode('utf-8', 'ignore')).rstrip('\0')
        out = unpad(st)
        return out


def hash_code(data):
    print('md5: ', md5(data))
    print('sha1: ', sha1(data))
    print('sha256: ', sha256(data))
