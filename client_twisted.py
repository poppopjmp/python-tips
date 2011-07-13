#! /usr/bin/python
#coding=utf8

from twisted.internet import epollreactor
epollreactor.install()

from twisted.internet import protocol, reactor
from twisted.protocols import basic

class Data_Center(basic.LineReceiver):

    def connectionMade(self):
        print "connected to ", self.transport.getPeer()

    def dataReceived(self, data):
        print data 
        back_data = raw_input("---> ")
        if back_data  =="quit" or not back_data:
            print "client quit ..."
            self.transport.write(back_data)
            self.transport.loseConnection()
        else:
            self.transport.write(back_data)

class Client_Factory(protocol.ClientFactory):
    protocol = Data_Center

    def clientConnectionFailed(self, transport, reason):
        print "client connection failed"
        reactor.stop()

    def clientConnectionLost(self, transport, reason):
        print "client connection lost"
        reactor.stop()

if __name__ == "__main__":
    host = "localhost"
    port = 50000
    reactor.connectTCP(host, port, Client_Factory(), timeout=10)
    reactor.run()
