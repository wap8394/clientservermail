#import socket module
from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Adding nothing in order for the socket to connect to the mailserver and port in the definition
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv)
    # You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfromcommand = "MAIL FROM: <wap8394@nyu.edu>\r\n"
    clientSocket.send(mailfromcommand.encode())
    recv2 = clientSocket.recv(1024)
    print(recv2)
    if recv2[:3] != '250':
        print('MAIL FROM not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpttocommand = "RCPT TO: <wap8394@nyu.edu>\r\n"
    clientSocket.send(rcpttocommand.encode())
    recv3 = clientSocket.recv(1024)
    print(recv3)
    if recv3[:3] != '250':
        print('RCPT TO not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    datacommand = "DATA"
    clientSocket.send(datacommand.encode())
    recv4 = clientSocket.recv(1024)
    print(recv4)
    if recv4[:3] != '250':
        print('Data not received from server')
    # Fill in end

    # Send message data.
    # Fill in start
    messagecommand = str(msg + endmsg)
    clientSocket.send(messagecommand.encode())
    recv5 = clientSocket.recv(1024)
    print(recv5)
    if recv5[:3] != '250':
        print('message not received from server')
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # added message in section above
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitcommand = "QUIT\r\n"
    clientSocket.send(quitcommand.encode())
    recv6 = clientSocket.recv(1024)
    print(recv6)
    if recv6[:3] != '250':
        print('Quit not received from server')
    # Fill in end
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')