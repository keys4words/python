import abc

class AbstractServer(abc.ABC):
    def __init__(self, version):
        self.version = version
    def get_version(self):
        return self.version
    @abc.abstractmethod
    def connect(self):
        pass

class IServer(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        pass
    @abc.abstractmethod
    def disconnect(self):
        pass
    @abc.abstractmethod
    def request(self):
        pass
    @abc.abstractmethod
    def response(self):
        pass

class ServerApache(AbstractServer):
    def connect(self):
        pass

class ServerIIS(AbstractServer):
    pass

class Client:
    def connect_to(self, server):
        if isinstance(server, AbstractServer):
            server.connect()

serverApache = ServerApache(2)

