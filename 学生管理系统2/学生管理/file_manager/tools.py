import hashlib


def Password(password):  # 加密
    ha = hashlib.sha256()
    ha.update(password.encode('utf8'))
    return ha.hexdigest()


if __name__ == "__main__":
    a = Password('123456')
    print(a)
