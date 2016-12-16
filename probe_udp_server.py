# -*- coding: utf-8 -*-
"""探针收数服务器"""
import socket
import time

__author__ = "liushen"

dic = set()


class Socket(object):
    def __init__(self, addr):
        self.s = None
        self.addr = addr

    def __enter__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(self.addr)
        return self.s

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s.close()


class xxxx(object):
    def __init__(self):
        self.fp = None
        self.count = 0

    def __enter__(self):
        self.open()
        return self

    def open(self):
        self.fp = open("Mac" + time.strftime(" %m-%d %H:%M:%S"), 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

    def writeline(self, txt):
        if self.count >= 50:
            self.fp.close()
            self.open()
            self.count = 0
        self.fp.write(txt + "\n")
        self.count += 1


def main():
    # UDP
    addr = ('0.0.0.0', 6665)

    with Socket(addr)as s:
        print ("UDP Server started:", addr)

        with xxxx() as fp:
            while True:
                data, addr = s.recvfrom(2048)
                # if not data:
                #     print "client has exist"
                #     break
                # print "received:", data, "from", addr
                print ("data: ", data)
                for i in data.split():
                    mac = str(i).split("|")[1]
                    if mac in dic:
                        continue
                    fp.writeline(mac)
                    dic.add(mac)


if __name__ == "__main__":
    main()
