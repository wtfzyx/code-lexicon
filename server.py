import os
import webbrowser
import http.server
import socketserver

PORT = 8000  # 如果提示端口被占用，改成 8001、8002 都行

# 切换到脚本所在文件夹，确保服务器能找到 index.html
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class MyServer(socketserver.TCPServer):
    allow_reuse_address = True  # 允许停止后立刻重新启动，不报端口占用

if __name__ == "__main__":
    with MyServer(("127.0.0.1", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
        print(f"服务器已启动！地址：http://localhost:{PORT}")
        print("想停止服务：点 PyCharm 的红色方块，或关掉运行窗口")
        webbrowser.open(f"http://localhost:{PORT}")  # 自动帮你打开浏览器
        httpd.serve_forever()  # 一直运行，直到你手动停止