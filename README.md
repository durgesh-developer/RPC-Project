# Task
## Create client server model
### Problem Statement
### Client Side
Client send message and token number. Each token number represents task to covert message in lowercase, uppercase and sentence case
Task Number
1 lowercase
2 uppercase
3 sentence case
Server will send response and client will print the message
To close connection client will send close/quit message
### Server Side
Server will setup each connection with new thread and each therad will do the task and send corresponding result to client
### Output
![op](https://github.com/durgesh-developer/RPC-Project/assets/78478098/6e238991-2d23-40a8-807b-a4efc6130a1d)
### How to run!
1. Run commands in terminal
   `git clone <url>`
   `cd <clone-folder>`
2. Open 2 terminals in clone folder
   and run each commands into a seperate terminal
   `python server.py`
   `python client.py`
