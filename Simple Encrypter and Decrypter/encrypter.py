'''
We are replacing a single letteror number or symbol with two random string object.
During the decryption, we will reverse the process and will find the appropriate letter
'''

def to_encrypt(a):
    for n, i in enumerate(a):
        if a[n] == 'A':
            a[n] = '0q'
        if a[n] == 'B':
            a[n] = 'w0'
        if a[n] == 'C':
            a[n] = '0e'
        if a[n] == 'D':
            a[n] = 'r0'
        if a[n] == 'E':
            a[n] = '0t'
        if a[n] == 'F':
            a[n] = 'y0'
        if a[n] == 'G':
            a[n] = '0u'
        if a[n] == 'H':
            a[n] = 'i0'
        if a[n] == 'I':
            a[n] = '0o'
        if a[n] == 'J':
            a[n] = 'p0'
        if a[n] == 'K':
            a[n] = '0a'
        if a[n] == 'L':
            a[n] = 's0'
        if a[n] == 'M':
            a[n] = '0d'
        if a[n] == 'N':
            a[n] = 'f0'
        if a[n] == 'O':
            a[n] = '0g'
        if a[n] == 'P':
            a[n] = 'h0'
        if a[n] == 'Q':
            a[n] = '0j'
        if a[n] == 'R':
            a[n] = 'k0'
        if a[n] == 'S':
            a[n] = '0l'
        if a[n] == 'T':
            a[n] = 'z0'
        if a[n] == 'U':
            a[n] = '0x'
        if a[n] == 'V':
            a[n] = 'c0'
        if a[n] == 'W':
            a[n] = '0v'
        if a[n] == 'X':
            a[n] = 'b0'
        if a[n] == 'Y':
            a[n] = '0n'
        if a[n] == 'Z':
            a[n] = 'm0'
        if a[n] == 'a':
            a[n] = '1Z'
        if a[n] == 'b':
            a[n] = 'X1'
        if a[n] == 'c':
            a[n] = '1C'
        if a[n] == 'd':
            a[n] = 'V1'
        if a[n] == 'e':
            a[n] = '1B'
        if a[n] == 'f':
            a[n] = 'N1'
        if a[n] == 'g':
            a[n] = '1M'
        if a[n] == 'h':
            a[n] = 'A1'
        if a[n] == 'i':
            a[n] = '1S'
        if a[n] == 'j':
            a[n] = 'D1'
        if a[n] == 'k':
            a[n] = '1F'
        if a[n] == 'l':
            a[n] = 'G1'
        if a[n] == 'm':
            a[n] = '1H'
        if a[n] == 'n':
            a[n] = 'J1'
        if a[n] == 'o':
            a[n] = '1K'
        if a[n] == 'p':
            a[n] = 'L1'
        if a[n] == 'q':
            a[n] = '1Q'
        if a[n] == 'r':
            a[n] = 'W1'
        if a[n] == 's':
            a[n] = '1E'
        if a[n] == 't':
            a[n] = 'R1'
        if a[n] == 'u':
            a[n] = '1T'
        if a[n] == 'v':
            a[n] = 'Y1'
        if a[n] == 'w':
            a[n] = '1U'
        if a[n] == 'x':
            a[n] = 'I1'
        if a[n] == 'y':
            a[n] = '1O'
        if a[n] == 'z':
            a[n] = 'P1'
        if a[n] == '1':
            a[n] = 'qw'
        if a[n] == '2':
            a[n] = 'as'
        if a[n] == '3':
            a[n] = 'zx'
        if a[n] == '4':
            a[n] = 'er'
        if a[n] == '5':
            a[n] = 'df'
        if a[n] == '6':
            a[n] = 'cv'
        if a[n] == '7':
            a[n] = 'ty'
        if a[n] == '8':
            a[n] = 'gh'
        if a[n] == '9':
            a[n] = 'vb'
        if a[n] == '0':
            a[n] = 'yu'
        if a[n] == '~':
            a[n] = 'po'
        if a[n] == '!':
            a[n] = 'oi'
        if a[n] == '@':
            a[n] = 'iu'
        if a[n] == '#':
            a[n] = 'yt'
        if a[n] == '$':
            a[n] = 'tr'
        if a[n] == '%':
            a[n] = 're'
        if a[n] == '^':
            a[n] = 'ew'
        if a[n] == '&':
            a[n] = 'wq'
        if a[n] == '*':
            a[n] = 'lk'
        if a[n] == '(':
            a[n] = 'kj'
        if a[n] == ')':
            a[n] = 'hg'
        if a[n] == '_':
            a[n] = 'gf'
        if a[n] == '+':
            a[n] = 'fd'
        if a[n] == '{':
            a[n] = 'ds'
        if a[n] == '}':
            a[n] = 'sa'
        if a[n] == '|':
            a[n] = 'mn'
        if a[n] == ':':
            a[n] = 'nb'
        if a[n] == '"':
            a[n] = 'bv'
        if a[n] == '?':
            a[n] = 'vc'
        if a[n] == '>':
            a[n] = 'cx'
        if a[n] == '<':
            a[n] = 'xz'
        if a[n] == '`':
            a[n] = '12'
        if a[n] == '-':
            a[n] = '23'
        if a[n] == '=':
            a[n] = '34'
        if a[n] == '\\':
            a[n] = '45'
        if a[n] == ']':
            a[n] = '56'
        if a[n] == '[':
            a[n] = '67'
        if a[n] == "'":
            a[n] = '78'
        if a[n] == ';':
            a[n] = '89'
        if a[n] == '/':
            a[n] = '90'
        if a[n] == '.':
            a[n] = '01'
        if a[n] == ',':
            a[n] = '$&'
        if a[n] == ' ':
            a[n] = 'Ax'
    return a
