# Room Chat (Socket.IO + Python)

This project is based on a template from the course [Stepik: Writing WebSockets in Python](https://stepik.org/course/195202/info). It is a simple real-time chat application built with Python and Socket.IO. In this project, I learned how to work with WebSockets, handle real-time communication, and manage room-based chat functionality.

## Features

- Real-time interaction with users via WebSockets 
- Users can join and leave chat rooms 
- Support for multiple predefined rooms: "lobby", "general", and "random"
- Users can send and receive messages within their joined room 
- User session management with name and room tracking 
- Basic error handling and input validation

## Installation and Setup

1. **Clone the repository:**
    
    ```sh
    git clone https://github.com/kateutkate23/socketio-room-chat.git
    cd socketio-room-chat
    ```
    
2. **Create a virtual environment and activate it:**
    
    ```sh
    python -m venv venv
    # On Linux
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate
    ```
    
3. **Install dependencies:**
    
    ```sh
    pip install -r requirements.txt
    ```
    
4. **Run the application:**
    
    ```sh
    python main.py
    ```
    
5. **Open in your browser:**
    
    - Visit `http://127.0.0.1:8000/` to start chatting.

## Technologies Used

- Python
- Socket.IO
- Eventlet
- Pydantic (for data validation)
- Loguru (for logging)

---

### License

This project is for learning purposes and is open for modification and improvement.
