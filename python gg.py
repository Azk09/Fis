import time
import requests

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot<7417866195:AAFu4UQ0zL9T5V9ApQfU-KlpuqBVPHIPN1A>/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

chat_id = "2095865760"  # ID чата или название чата
while True:
    current_hour = time.localtime().tm_hour
    
    if current_hour % 3 == 0:
        send_message(chat_id, "/relax")
    else:
        send_message(chat_id, "/gym")
    
    time.sleep(3600)  # Подождать 1 час перед следующим отправлением сообщения