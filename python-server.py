import os # 导入操作系统接口模块
import http.server # 导入HTTP服务器模块

# 定义一个自定义 的HTTP请求处理程序类，继承自SimpleHTTPRequestHandler
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    #  重写list_directory方法，实现自定义的目录列表功能
    def list_directory(self, path):
        try:
            # 获取目录内容并按字母顺序排序（忽略大小写
            directory_listing = os.listdir(path)
            directory_listing.sort(key=lambda a: a.lower())

            # 构造响应头，返回纯文本
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()

            # 构造纯文本形式的目录内容，目录项之间使用换行符
            response = "\n".join(directory_listing)
            # 将响应内容编码为UTF-8并返回
            return self.wfile.write(response.encode("utf-8"))
        except OSError:
            # 如果发生OSError异常，发送404错误响应
            self.send_error(404, "Directory listing failed")
            return None
        
# 如果当前模块是主模块，则启动HTTP服务器
if __name__ == "__main__":
    # 启动服务器
    PORT = 8000
    # 创建一个支持多新城的HTTP服务器实例，绑定到指定端口，并使用自定义的请求处理程序
    with http.server.ThreadingHTTPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
