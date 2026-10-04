# Networking-tools-etc
Hello guys these are my networking tools 

What is CowScan?
CowScan is just a reguler port scanner nothing too good for now
and i am planning to make some changes i want this tool to be useful to me

why did i creat cowscan?
-cause i wanted to know how a port scanner works

how does CowScan work?
so firstly we type "target = input("")"
and "ports = input("")"
after this we do ports = ports.split(",") 
why did we do that cause we want to check multiple ports for example if we enter
"22,443,8080" python will see this as
["22","443","8080"]
so it will not be a fully text and then we do 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))
ım pretty sure this code try's to connect to tcp and 
if result == 0:
        print(f"[OPEN]   {port} - {service}")
    else:
        print(f"[CLOSED] {port} - {service}")
we do this so if the result is 0 it says 
[OPEN] 22 ssh
i tried my best explaining please tell me what should i add
