from random import choice

def encrypter(source,destination,pad):
    with open(source) as mess:
        with open(pad,'w') as otp:
            with open(destination,'w') as dest:
                val='abcdefghijklmnopqrstuvwxyz01234-'
                for line in mess.readlines():
                    for i in range(len(line)):
                        disp=choice(val)
                        otp.write(disp)
                        dest.write(chr(ord(line[i])^ord(disp)))

def decrypter(source,destination,pad):
    with open(source) as mess:
        with open(pad) as otp:
            with open(destination,'w') as dest:
                try:
                    while True:
                        dest.write(chr(ord(mess.read(1))^ord(otp.read(1))))
                except:
                    pass
                    
def showContent(filenames):
    for filename in filenames:
        print(f'{filename} content: ')
        with open(filename) as fh:
            for line in fh.readlines():
                print(line)
def main():
    encrypter('message.txt','encrypted.txt','otp.txt')
    decrypter('encrypted.txt','dec_message.txt','otp.txt')
    showContent(['otp.txt','encrypted.txt','dec_message.txt'])

if __name__ == '__main__':
    main()    