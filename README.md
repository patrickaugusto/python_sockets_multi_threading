# Atividade de Redes

This is a small example of socket programming that is able to connect multiple clients to a server using python 3 sockets. It can send messages from clients to server, and from server to clients. This example also shows how to host the socket server locally or globally across the internet so anyone can connect. This uses the python 3 socket and threading module.

## Alunos
### Patrick Augusto do Nascimento
### Antonio Rodrigues de Carvalho Neto


* Encoding the message from a string into bytes so that we can actually send it through the socket.
* Then follow protocol where length of the first message we send is the length of the message that is about to come.
* (`send_length = str(msg_length).encode(FORMAT)`)Length of first message that we send, representing the length of (`message`) ... which is the message we actually want to send.

