from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os, webbrowser
PORT=8000
os.chdir(Path(__file__).resolve().parent)
url=f"http://localhost:{PORT}/index.html"
print(f"Prieds TMS running at {url}")
try: webbrowser.open(url)
except Exception: pass
ThreadingHTTPServer(("127.0.0.1",PORT),SimpleHTTPRequestHandler).serve_forever()
