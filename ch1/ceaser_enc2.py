def encrypto(text, shift):
    a = ord('A');
    conv = lambda n : chr((ord(n) - a + shift ) % 26 + a)
    enc1 = lambda n : conv(n) if 'A' <= n <= 'Z' else n
    return ''.join([enc1(n) for n in text])

enc = encrypto("I LOVE YOU", 3)
dec = encrypto(enc, -3)
print(enc, "=>" , dec)
