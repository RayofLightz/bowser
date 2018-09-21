import hashlib

def check_sum(ftc):
    a = hashlib.md5()
    a.update(ftc.encode())
    return a.hexdigest()

