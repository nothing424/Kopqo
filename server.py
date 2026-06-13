#!/usr/bin/env python3
"""
Kopqo AI — Local Development Server
Run this script to serve Kopqo AI locally on http://localhost:8080
"""

import http.server
import socketserver
import os
import webbrowser
import threading
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Clean, minimal logging
        method = args[0].split()[0] if args else "?"
        path = args[0].split()[1] if args else "?"
        code = args[1] if len(args) > 1 else "?"
        print(f"  {code}  {method:6s} {path}")

    def end_headers(self):
        # Add CORS headers for API calls
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()


def open_browser(port):
    """Open browser after a short delay."""
    import time
    time.sleep(0.8)
    webbrowser.open(f"http://localhost:{port}")


def main():
    global PORT
    if len(sys.argv) > 1:
        try:
            PORT = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port: {sys.argv[1]}. Using default {PORT}.")

    print("\n" + "=" * 50)
    print("  KOPQO AI — Local Server")
    print("=" * 50)
    print(f"  URL    : http://localhost:{PORT}")
    print(f"  Root   : {DIRECTORY}")
    print(f"  Stop   : Ctrl+C")
    print("=" * 50 + "\n")

    # Open browser automatically
    threading.Thread(target=open_browser, args=(PORT,), daemon=True).start()

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except OSError as e:
        print(f"\n  Error: Port {PORT} is in use. Try: python server.py {PORT + 1}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n  Server stopped.\n")


if __name__ == "__main__":
    main()
