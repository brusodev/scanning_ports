import socket

def port_scanner(target, ports):
    hostname = socket.gethostbyname(target)
    print(f"Mapeando... {target} ({hostname})")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((hostname, port))

        if result == 0:
            print(f"Porta {port} está aberta")
        sock.close()
        if result != 0: 
            print(f"Porta {port} está fechada")
        
    print("Scan finalizado")


#Exemplo de uso
target = "brechomiraluh.com.br"
ports = [21, 22, 80, 443, 8080]
port_scanner(target, ports)
