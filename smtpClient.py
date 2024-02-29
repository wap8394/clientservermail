# import socket module
from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((mailserver, port))
    # Fill in end

    recv = clientsocket.recv(1024).decode()
    #print(recv)
    # You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientsocket.send(heloCommand.encode())
    recv1 = clientsocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfromcommand = "MAIL FROM: <wap8394@nyu.edu>\r\n"
    clientsocket.send(mailfromcommand.encode())
    recv1 = clientsocket.recv(1024).decode
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('MAIL FROM not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpttocommand = "RCPT TO: <wap8394@nyu.edu>\r\n"
    clientsocket.send(rcpttocommand.encode())
    recv1 = clientsocket.recv(1024).decode
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('RCPT TO not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    datacommand = "DATA\r\n"
    clientsocket.send(datacommand.encode())
    recv1 = clientsocket.recv(1024).decode
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('Data not received from server')
    # Fill in end

    # Send message data.
    # Fill in start
    messagecommand = str(msg + endmsg)
    clientsocket.send(messagecommand.encode())
    recv1 = clientsocket.recv(1024).decode
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('message not received from server')
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # added message in section above
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitcommand = "QUIT\r\n"
    clientsocket.send(quitcommand.encode())
    recv1 = clientsocket.recv(1024).decode
    #print(recv1)
    #if recv1[:3] != '250':
    #    print('Quit not received from server')
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
