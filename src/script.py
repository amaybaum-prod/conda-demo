from twisted.internet import protocol, reactor, endpoints
from twisted.web import http, client


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write()


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
http_client = http.HTTPClient
redirect_agent = client.RedirectAgent
