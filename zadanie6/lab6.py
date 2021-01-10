with open('face.png', 'rb') as byte_reader:
    print(byte_reader.read(1))
    print(byte_reader.read(3))
    print(byte_reader.read(2))
    print(byte_reader.read(1))
    print(byte_reader.read(1))

    
#Wynik   
'\x89'
b'PNG'
b'\r\n'
b'\x1a'
b'\n'
PS C:\U
