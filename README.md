# Group Chat Application using Python Sockets

This project is a simple group chat application implemented using Python sockets. It includes a server and multiple clients that can connect simultaneously to send and receive messages.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [How to Run](#how-to-run)
4. [Conclusion](#conclusion)

---

## Introduction

This project is designed as part of a computer networks course to demonstrate the implementation of a group chat system using Python sockets. The server can handle multiple clients simultaneously and ensures messages are correctly sent and received between clients.

---

## Features

- **Multiple Client Support:** The server can handle multiple clients at the same time.
- **Send and Receive Messages:** Clients can send messages and receive messages from other clients.
- **Error Handling:** Errors such as disconnections and failed responses are managed properly.
- **Console Display:** Received messages are displayed in the console.

---

## How to Run

### Prerequisites

- Python 3.x
- No external libraries are required.

### Running the Server

1. Run the `server.py` file:

   ```bash
   python server.py

    The server will start listening on 127.0.0.1 and port 7000.
   ```

Running the Client

    Run the client.py file:
    bash
    Copy

    python client.py

    Enter your username and start chatting.

Conclusion

This project effectively demonstrates how to create a simple group chat system using Python sockets. The optimal buffer size for receiving data was determined to be 1024 bytes, as it provides a good balance between speed and memory usage. Enabling TCP_NODELAY significantly reduced latency for small data transmissions. Finally, using TCP was more suitable for this group chat application due to its reliability.

Author: MohammadJavad HosseinPoor
Date: 2025-03-21
