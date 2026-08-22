"""
Orion Industrial Digital Twin Platform - Master Launcher
Starts a local HTTP server and opens the 3D Digital Twin Dashboard in the browser.
"""

import http.server
import socketserver
import webbrowser
import socket
import os
import sys

DEFAULT_PORT = 8080

def find_available_port(start_port=8080, max_attempts=20):
    for p in range(start_port, start_port + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('127.0.0.1', p))
                return p
            except OSError:
                continue
    return start_port

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = find_available_port(DEFAULT_PORT)
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("127.0.0.1", port), Handler) as httpd:
        url = f"http://127.0.0.1:{port}/index.html"
        print("=" * 65)
        print("   ORION INDUSTRIAL DIGITAL TWIN PLATFORM   ")
        print("=" * 65)
        print(f" Server running at: {url}")
        print(" Opening Orion in your default web browser...")
        print(" Press Ctrl+C to stop the server.")
        print("=" * 65)
        sys.stdout.flush()
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down Orion server. Goodbye!")

if __name__ == "__main__":
    run_server()
