#!/usr/bin/python3
# -*- coding:UTF-8 -*-


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import PKCS1_v1_5
import gmpy2
import libnum
import base64


def create_public_key(n, e):
    rsa_components = (n, e)
    keypair = RSA.construct(rsa_components)
    with open('pubkey.pem', 'wb') as f:
        f.write(keypair.exportKey())


def create_private_key(n, e, d, p, q):
    rsa_components = (n, e, d, p, q)
    keypair = RSA.construct(rsa_components)
    with open('private.pem', 'wb') as f:
        f.write(keypair.exportKey())


def read_private_key():
    with open("private.pem", "rb") as f:
        key = RSA.import_key(f.read())
        print('n = %d' % key.n)
        print('e = %d' % key.e)
        print('d = %d' % key.d)
        print('p = %d' % key.p)
        print('q = %d' % key.q)


def read_public_key():
    with open("pubkey.pem", "rb") as f:
        key = RSA.import_key(f.read())
        print('n = %d' % key.n)
        print('e = %d' % key.e)


def encrypt():
    p = int(libnum.generate_prime(1024))
    q = int(gmpy2.next_prime(p))
    n = int(p * q)
    phi = (p-1)*(q-1)
    e = 65537
    d = int(gmpy2.invert(e, phi))
    m = b"flag{you_got_it}"
    public_key = RSA.import_key(RSA.construct((n, e)).export_key())
    public_key = PKCS1_OAEP.new(public_key)
    c = public_key.encrypt(m)
    print(c)

    private_key = RSA.import_key(RSA.construct((n, e, d, p, q)).export_key())
    private_key = PKCS1_OAEP.new(private_key)
    print(private_key.decrypt(c))


def decrypt():
    p = int('''
        157790417717035275943197904823645145281147085252905247447260034051878691034747684303715336348507267921249655103263347914128144476912685213431110454636244692224328066884510063590700506729345331153483633231327359450199822698241355428609085077662488946173655043172957247264543259611018596088670385591091710018977
    ''')
    q = int('''
        167343506005974003380506069679607737381940204686173214188860057004909006055220516074283090160430833007424970980655748310232878462615469792561310560310363430669700009093597847018287568821792168143170329382585883857083334915378884054389878477389765792275111293420203613159303898365894897865177093362621517279751
    ''')
    e = 65537
    n = int('''
        26405201714915839490865227813246218372938736243516916108608439705738170543023112509150522274284238701776297205717958250714972924576706985074311737321016048409831557758205687745692399643151467933196930799657476449865271038382866908177517793954543176769652784274788769353482450910551831498252972857285424471782215525406445071432588374802623485148684255853068532820859835479998199886719945699488858505070686919320144576280217196858823521754407597888769668827432569034617434944912323704501156532854074083408527717809315663187405585840074689387865750105223058720511199252150772925124516509254841404742306560035497627834727
    ''')

    phi = (p-1)*(q-1)
    d = int(gmpy2.invert(e, phi))
    key_info = RSA.construct((n, e, d, p, q))
    key = RSA.importKey(key_info.exportKey())
    key = PKCS1_OAEP.new(key)
    # key = PKCS1_v1_5.new(key)
    fp = '/tmp/flag.enc'
    with open(fp, "r") as f:
        c = f.read()
        c = base64.b64decode(c)
        print(int.from_bytes(c, "little"))
    # PKCS1_OAEP
    m = key.decrypt(c)

    # PKCS1_v1_5
    # m = key.decrypt(c, None)
    print(m)


if __name__ == '__main__':
    decrypt()
