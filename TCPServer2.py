#http://brownbears.tistory.com/207
import socketserver
import sys

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('client Connection: {0} '.format(self.client.client_address[0]))
        sock = self.request

        rbuff = sock.recv(1024) #데이터를 수신하고 그결과를 rbuff에 저장
        received = str(rbuff, encoding='utf-8')
        print('received : {0} '.format(received))

        #Received Data Return
        sock.send(rbuff)
        print('transfer : {0} '.format(received))
        sock.close()

if __name__ == '__main__':
    if len(sys.argv) <2:
       print('{0} < Bind IP >'.format(sys.argv[0]))
       sys.exit()

    bindIP = sys.argv[1]
    bindPort = 5425

    server = socketserver.TCPServer((bindIP, bindPort), MyTCPHandler)

    print('Server Start...')

    server.server_forever()
