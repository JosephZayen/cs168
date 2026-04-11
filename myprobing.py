import util

args = util.parse_args()
ip_addr = util.gethostbyname(args.host.strip())
TRACEROUTE_PORT_NUMBER = 33434

message = "hi i wanna fuck u!".encode()

mysendsock = util.Socket.make_udp()
myrecvsock = util.Socket.make_icmp()

mysendsock.set_ttl(1)
mysendsock.sendto(message,(ip_addr, TRACEROUTE_PORT_NUMBER))

if(myrecvsock.recv_select()):
    print(myrecvsock.recvfrom())


