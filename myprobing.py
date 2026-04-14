import util

args = util.parse_args()
ip_addr = util.gethostbyname(args.host.strip())
TRACEROUTE_PORT_NUMBER = 33434
ttl = 2

message = "hi!".encode()

mysendsock = util.Socket.make_udp()
myrecvsock = util.Socket.make_icmp()

mysendsock.set_ttl(ttl)
mysendsock.sendto(message,(ip_addr, TRACEROUTE_PORT_NUMBER))

if(myrecvsock.recv_select()):
    raw_bytes, data_tuple = myrecvsock.recvfrom()
    hex_bytes = raw_bytes.hex()
    print(hex_bytes)
    
class UDP:
    src_port:int
    dst_port:int
    len:int
    cksum:int
    def __init__(self, buffer:bytes):
        array = "".join(format(byte, "08b") for byte in [*buffer])
        self.src_port = int(array[0:16],2)
        self.dst_port = int(array[16:32],2)
        self.len = int(array[32:48],2)
        self.cksum = int(array[48:64],2)
    
    def __str__(self) -> str:
        pass


class ICMP:
    type:int
    code:int
    cksum:int
    rest:int
    def __init__(self, buffer:bytes):
        array = "".join(format(byte, "08b") for byte in [*buffer])
        self.type = int(array[0:16],2)
        self.code = int(array[16:32],2)
        self.cksum = int(array[32:48],2)
        self.rest = int(array[48:64],2)
    
    def __str__(self) -> str:
        pass


class IPv4:
    version:int
    header_len:int
    tos:int
    length:int
    id:int
    flags:int
    offset:int
    ttl:int
    proto:int
    cksum:int
    src:int
    dest:int
    ops:int


    def __init__(self, buffer:bytes):
        array = "".join(format(byte, "08b") for byte in [*buffer])
        self.version = int(array[0:4],2)
        self.header_len = int(array[4:8],2)
        self.tos = int(array[8:16],2)
        self.length = int(array[16:48],2)
        self.id = int(array[48:64],2)
        self.flags = int(array[64:67],2)
        self.offset = int(array[67:80],2)
        self.ttl = int(array[80:88],2)
        self.proto = int(array[88:96],2)
        self.cksum = int(array[96:112],2)
        self.src = int(array[112:144],2)
        self.dest = int(array[144:176],2)
        self.ops = int(array[176: self.header_len * 32 - 176],2)

    def __str__(self) -> str:
        pass


