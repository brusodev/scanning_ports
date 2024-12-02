# Scaneando portas abertas de um domínio

## Escrevi esse código para verificar se as portas de um hostname estão abertas, consultando diretamente pelo domínio.

### Neste exemplo de uso, basta você colocar na variavel "target" o domínio que deseja consultar, em seguida digite as portas que deseja consultar se realmente estão abertas. Tudo pronto, ao término do "scanning", retornará se as portas especificadas estão abertas.

target = "brechomiraluh.com.br"
ports = [21, 22, 80, 443, 8080]
port_scanner(target, ports)
