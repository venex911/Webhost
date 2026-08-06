# Webhost

A Python tool for uploading HTML files to a web server and receiving shareable links.

## Features

- Upload HTML files to remote server
- Automatic file hosting with direct URL
- Discord webhook integration for notifications
- Server status checker
- Beautiful CLI interface with colored output

## Installation

```bash
git clone https://github.com/yourusername/webhost.git
cd webhost
pip install -r requirements.txt
```

## Requirements

- Python 3.6+
- `requests`
- `colorama`
- `pystyle`

## Usage

Run the tool:

```bash
python webhost.py
```

### Menu Options

1. **Upload code** - Upload an HTML file and get a shareable URL
2. **Check if server is active** - Verify the hosting server status
3. **Exit** - Close the application

### Upload Process

1. Select option `1`
2. Enter the path to your HTML file
3. Enter your Discord webhook URL (optional)
4. The tool will upload your file and return a direct URL

### Discord Webhook Integration

When you provide a Discord webhook URL, the tool will send an embed with:
- Filename and size
- Upload timestamp
- Direct download URL

## Example

```
Enter path to your html file: /home/user/index.html
Enter discord webhook: https://discord.com/api/webhooks/...
Upload finish
File URL: http://www.grand-test.com/uploads/index.html
Webhook sent successfully.
```

## Disclaimer

This tool is for educational and testing purposes only. Use it responsibly and only on servers you have permission to use.

## Author

Venex

## Version

1.0
