import codecs
import itertools


class EncryptedFile:
    """
    DO NOT USE ANY OF THESE FOR REAL ENCRYPTION
    """
    _registry = {}  # "rot13" -> Rot13EncryptedFile

    def __init_subclass__(cls, prefix, **kwargs):
        """
        https://docs.python.org/3/reference/datamodel.html#object.__init_subclass__

        This (hook =) dunder method is called
        is called whenever the containing class is subclassed.
        
            `cls` is then the new subclass.
        
            If defined as a normal instance method,
            this method is implicitly converted to a class method.

        https://stackoverflow.com/questions/45400284/understanding-init-subclass

        It is used to populate the `cls._registry`.
        
        (
        It is useful
        for registering subclasses in some way
        _and_
        for setting default attribute values on those subclasses.
        
        Keyword arguments which are given to a new class
        are passed to the parent class's `__init_subclass__`.
        )
        """
        super().__init_subclass__(**kwargs)
        cls._registry[prefix] = cls

    def __new__(cls, path: str, key=None):
        # Parse out the prefix from the `path`.
        prefix, sep, suffix = path.partition(':///')
        if sep:
            file = suffix
        else:
            file = prefix
            prefix = 'file'
        
        subclass = cls._registry[prefix]

        obj = object.__new__(subclass)
        obj.file = file
        obj.key = key
        return obj
    
    def read(self) -> str:
        raise NotImplementedError


class PlaintextFile(EncryptedFile, prefix='file'):
    def read(self):
        with open(self.file, 'r') as f:
            return f.read()


class ROT13EncryptedFile(EncryptedFile, prefix='rot13'):
    def read(self):
        with open(self.file, 'r') as f:
            encrypted_text = f.read()
        decrypted_text = codecs.decode(encrypted_text, 'rot_13')
        return decrypted_text


class OneTimePadXorEncryptedFile(EncryptedFile, prefix='otp'):
    def __init__(self, path, key):
        if isinstance(self.key, str):
            self.key = self.key.encode()
    
    def read(self):
        with open(self.file, 'rb') as f:
            encrypted_bytes = f.read()
        decrypted_bytes = self._xor_bytes_with_key(encrypted_bytes)
        return decrypted_bytes.decode()
    
    def _xor_bytes_with_key(self, bs: bytes) -> bytes:
        return bytes(
            b_1 ^ b_2
            for b_1, b_2 in zip(
                bs,
                itertools.cycle(self.key),
            )
        )
        

def encrypted_file_example():
    print('ENCRYPTED FILE EXAMPLE')
    print(
        EncryptedFile('file_5_1_plaintext_hello.txt').read(),
    )
    print(
        EncryptedFile('rot13:///file_5_2_rot13_hello.txt').read(),
    )
    print(
        EncryptedFile(
            'otp:///file_5_3_otp_hello.txt',
            key='1234',
        ).read(),
    )


if __name__ == '__main__':
    encrypted_file_example()
