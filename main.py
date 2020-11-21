import tornado.ioloop
import tornado.web
import tornado.escape
import win32gui
import win32api
import win32con

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        hwnd = win32gui.FindWindow(None, tornado.escape.json_decode(self.request.body)['title'])
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, win32api.GetSystemMetrics(0) - 800, win32api.GetSystemMetrics(1) - 600, 800, 600, 0)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()