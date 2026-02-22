class ProcessedInfo:
    def __init__(self, message, target=None):
        self.message = message
        self.target = target if target is not None else {}

def _broadcast_to_qq(msg):
    # Add target parameter to force messages to group 817621853
    processed_info = ProcessedInfo(msg, target={"817621853": "group"})
    # Logic to send the message
    send_message_to_qq(processed_info)

# Example for sending message
# _broadcast_to_qq("Hello, QQ Group!")