import socket
import sys

GROUP = "224.0.0.1"
PORT = 8123
PY_VERSION = sys.version[0]

def main():
    help = """
    -s untuk sender
    -r untuk receiver
    -h untuk menampilkan pesan ini
    """
    if (len(sys.argv)>1):
        if (sys.argv[1] == "-s"):
            sender()
        elif (sys.argv[1] == "-r"):
            receiver()
        elif (sys.argv[1] == "-h"):
            print (help)
        else :
            print ("Argumen tidak dikenali")
            print (help)
    else:
        print ("Argumen tidak dikenali")
        print (help)

def sender():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    while(True):
        pesan = ""
        if (PY_VERSION == '2'):
            pesan = str(raw_input("Pesan : "))
        else:
            pesan = input("Pesan : ").encode('ascii')
        sock.sendto(pesan, (GROUP, PORT))
    

def receiver(buf_size=1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', PORT))

    # setting multicast
    sock.setsockopt(
        socket.IPPROTO_IP,
        socket.IP_ADD_MEMBERSHIP,
        socket.inet_aton(GROUP) + socket.inet_aton('127.0.0.1'))
    
    while True:
        pesan, pengirim= sock.recvfrom(buf_size)
        # byte to string 
        pesan = pesan.decode("utf-8") 
        #print pesan sama pengirimnya
        print (str(pengirim) + ' => ' + str(pesan))

if __name__ == '__main__':
    main()
