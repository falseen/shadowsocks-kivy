# -*- coding: utf-8 -*-

import time,sys,os
sys.path.append('..')
from shadowsocks import local

def main():
    commod = ["-s", "sss.run", "-p", "10000", "-k", "sss.run"]
    sys.argv +=commod
    local.main()


if __name__ == '__main__':
    main()