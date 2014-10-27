cip = eval(open('p059_cipher.txt').read())
pad = bytes(max(range(ord('a'),ord('z')+1),
    key = lambda k: sum(c^k == ord(' ') for c in part))
        for part in (cip[i::3] for i in range(3)))
msg = bytes(c^pad[i%3] for i, c in enumerate(cip))
print(pad.decode(), msg.decode(), sum(msg))
