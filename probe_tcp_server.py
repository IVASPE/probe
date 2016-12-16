# -*- coding: utf-8 -*-
"""探针收数服务器"""
import socket

__author__ = "liushen"


def main():
    # TCP
    addr = ('0.0.0.0', 6664)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义socket类型，网络通信，TCP
    s.bind(addr)  # 套接字绑定的IP与端口
    s.listen(1)  # 开始TCP监听
    print "TCP server started:", addr
    while True:
        conn, addr = s.accept()  # 接受TCP连接，并返回新的套接字与IP地址
        print 'Connected by', addr  # 输出客户端的IP地址

        while True:
            print conn.sendall("ok")
            data = conn.recv(1024)  # 把接收的数据实例化
            print data
        conn.close()


if __name__ == "__main__":
    main()
    print "done"
