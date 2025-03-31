html = """
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI WebSocket Chat</title>
    </head>
    <body>
        <h1>💬 FastAPI WebSocket Chat</h1>
        <input id="messageInput" type="text" autocomplete="off"/>
        <button onclick="sendMessage()">Send</button>
        <ul id='messages'></ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage() {
                var input = document.getElementById("messageInput")
                ws.send(input.value)
                input.value = ''
            }
        </script>
    </body>
</html>
"""
