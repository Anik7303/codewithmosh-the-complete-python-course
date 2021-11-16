from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open.')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed.')
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print('Reading from a file stream.')


class NetworkStream(Stream):
    def read(self):
        print('Reading from a network stream.')


stream1 = FileStream()
stream1.read()
stream2 = NetworkStream()
stream2.read()
