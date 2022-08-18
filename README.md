```
python-dunder-methods $ python3 --version
Python 3.8.3
```

```
python-dunder-methods $ python3 file_1_dunder_methods.py 
new <class '__main__.A'> (1, 2, 3) {'x': 4}
init <__main__.A object at 0x7fb8e2b592e0> (1, 2, 3) {'x': 4}
```

```
python-dunder-methods $ python3 file_2_subclass_builtin_immutable_types.py 
UPPERCASE TUPLE EXAMPLE
('HI', 'THERE')
```

```
python-dunder-methods $ python3 file_4_same_as_file_3_but_on_steroids.py 
CLIENT CACHE EXAMPLE

reading info about client (with ID 0) from db.sqlite3
returning existing client (with ID 0) from cache
x is y: True

reading info about client (with ID 1) from db.sqlite3
```

```
python-dunder-methods $ echo 'hello world' > file_5_1_plaintext_hello.txt

(
https://stackoverflow.com/questions/5442436/using-rot13-and-tr-command-for-having-an-encrypted-email-address
)
python-dunder-methods $ echo 'hello world' | tr 'A-Za-z' 'N-ZA-Mn-za-m' > file_5_2_rot13_hello.txt

# TODO: figure out how to apply One-Time-Pad encryption to "subscribetomcoding"
#       (and to "subscribe to mcoding") using the key "123412341234123412341234"

python-dunder-methods $ python3 file_5_4_another_dunder_method.py 
ENCRYPTED FILE EXAMPLE
hello world

hello world

subscribetomcoding
```

```
python-dunder-methods $ python3 file_5_5_metaclass.py 
<class '__main__.UpperAttrMetaclass'>
Message
()
{'__module__': '__main__', '__qualname__': 'Message', 'id': 1, 'text': 'hello'}

hasattr(Message, 'id') = False
hasattr(Message, 'text') = False

hasattr(Message, 'ID') = True
hasattr(Message, 'TEXT') = True

# TODO: study https://stackoverflow.com/questions/63054541/how-to-type-the-new-method-in-a-python-metaclass-so-that-mypy-is-happy
```

# Bibliography

1. `mCoding`'s video called "\_\_new__ vs \_\_init__ in Python", which can be found at https://www.youtube.com/watch?v=-zsV0_QrfTw

2. https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
