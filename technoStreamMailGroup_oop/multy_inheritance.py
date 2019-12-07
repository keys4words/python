class Stream:
    def get_name(self):
        return 1

class InputStream(Stream):
    def read(self):
        return 'text'

    def get_name(self):
        return 2

class OutputStream:
    def write(self, text):
        return True

class InputOutputStream(InputStream, OutputStream):
    pass

stream = InputOutputStream()
print(stream.write(123))
print(stream.get_name())
print(InputOutputStream.__mro__)
print(type(stream) == OutputStream)
print(isinstance(stream, OutputStream))
print(isinstance(stream, object))
print(stream.__class__)
print(type(stream).__bases__)
print(stream.__dict__)