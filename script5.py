import socket
DARK_RED = "\033[38;5;88m"
DARK_BLUE = "\033[38;5;18m"
RESET = "\033[0m"

logo = r"""
        ^__^
        (oo)\_______
        (__)\       )\/\
           ||----w |
           ||     ||
"""
text = r"""
   ___              ____                 
  / __|___ __ ___  / ___|  ___ __ _ _ __ 
 | |__/ _ \ V  V | \___ \ / __/ _` | '_ \
  \___\___/\_/\_/  |____/ \___\__,_| .__/
                                    |_|
"""
print(DARK_BLUE + logo + RESET)
print(DARK_RED + text + RESET)

target = input("Target: ")
ports = input("Ports: ")

ports = ports.split(",")

for port in ports:
    port = int(port)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    try:
        service = socket.getservbyport(port, "tcp")
    except OSError:
        service = "Unknown"

    if result == 0:
        print(f"[OPEN]   {port} - {service}")
    else:
        print(f"[CLOSED] {port} - {service}")

    sock.close()