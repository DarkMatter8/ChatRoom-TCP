import Tkinter as tk
import socket
import select
import sys
from thread import *

root = tk.Tk()
root.title('Chat Room Client!')
root.geometry('300x300')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send():
	message = e2.get()
	server.send(message)
	sys.stdout.write("<You>")
	sys.stdout.write(message)
	lb.insert(tk.END, "<You>"+message)
	lb.update_idletasks()
	sys.stdout.flush()

def callback():
	start_new_thread(start_client,())

def start_client():
	
	IP_address = e1.get()
	Port = 9999
	server.connect((IP_address, Port))
	
	while True:
	 
	    # maintains a list of possible input streams
	    sockets_list = [server]
	 
	    """ There are two possible input situations. Either the
	    user wants to give  manual input to send to other people,
	    or the server is sending a message  to be printed on the
	    screen. Select returns from sockets_list, the stream that
	    is reader for input. So for example, if the server wants
	    to send a message, then the if condition will hold true   
	    below.If the user wants to send a message, the else
	    condition will evaluate as true"""
	    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
	 
	    for socks in read_sockets:
	        if socks == server:
	            message = socks.recv(2048)
	            print message
	            lb.insert(tk.END, message)
	            lb.update_idletasks()
	        else:
	            message = sys.stdin.readline()
	            server.send(message)
	            sys.stdout.write("<You>")
	            sys.stdout.write(message)
	            sys.stdout.flush()
	server.close()

w = tk.Label(root, text="Welcome to Chat Room").grid(row=0, columnspan=2)
ip = tk.Label(root, text="IP:").grid(row=1)
e1 = tk.Entry(root)
e1.grid(row=1, column=1)
connect = tk.Button(root, text="Connect !", command=callback).grid(row=2, columnspan=2)
lb = tk.Listbox(root)
lb.grid(row=3, columnspan=2)
connect = tk.Button(root, text="Send", command=send).grid(row=4, column=2, columnspan=2)
e2 = tk.Entry(root)
e2.grid(row=4, column=1)	

root.mainloop()
