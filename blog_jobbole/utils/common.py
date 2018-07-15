# -*- coding: utf-8 -*-

import hashlib

def get_md5(url):
    m = hashlib.md5()
    m.update(url.encode('utf-8'))
    return m.hexdigest()

#if __name__ == "__main__":
#    print(get_md5("http://jobbole.com".encode('utf-8')))
