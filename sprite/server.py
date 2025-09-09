"""
Static file server implementation for Sprite CLI.
"""

import http.server
import socketserver
import threading
from pathlib import Path
import mimetypes


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler with better error handling and logging."""
    
    def __init__(self, *args, directory=None, **kwargs):
        self.directory = directory
        super().__init__(*args, **kwargs)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom logging format."""
        pass
    
    def guess_type(self, path):
        """Improved MIME type guessing."""
        mimetype, encoding = mimetypes.guess_type(path)
        
        # Handle common web file types
        if path.endswith('.css'):
            return 'text/css'
        elif path.endswith('.js'):
            return 'application/javascript'
        elif path.endswith('.json'):
            return 'application/json'
        elif path.endswith('.svg'):
            return 'image/svg+xml'
        
        return mimetype or 'text/plain'


class StaticServer:
    """Static file server for serving local websites."""
    
    def __init__(self, host='localhost', port=8000, directory=None):
        self.host = host
        self.port = port
        self.directory = directory or Path.cwd()
        self.httpd = None
        self.server_thread = None
    
    def create_handler(self):
        """Create a request handler with the specified directory."""
        def handler(*args, **kwargs):
            return CustomHTTPRequestHandler(*args, directory=str(self.directory), **kwargs)
        return handler
    
    def start(self):
        """Start the server in a separate thread."""
        handler = self.create_handler()
        
        try:
            self.httpd = socketserver.TCPServer((self.host, self.port), handler)
            self.httpd.allow_reuse_address = True
            
            # Start server in a separate thread
            self.server_thread = threading.Thread(target=self.httpd.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            
            return True
            
        except Exception as e:
            raise Exception(f"Failed to start server: {e}")
    
    def serve_forever(self):
        """Start the server and serve forever (blocking)."""
        handler = self.create_handler()
        
        try:
            with socketserver.TCPServer((self.host, self.port), handler) as httpd:
                httpd.allow_reuse_address = True
                self.httpd = httpd
                httpd.serve_forever()
                
        except Exception as e:
            raise Exception(f"Failed to start server: {e}")
    
    def stop(self):
        """Stop the server."""
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
            
        if self.server_thread and self.server_thread.is_alive():
            self.server_thread.join(timeout=5)
    
    def is_running(self):
        """Check if the server is currently running."""
        return self.httpd is not None and self.server_thread and self.server_thread.is_alive()