from os import curdir,sep
import json
from cgi import parse_qs,escape,FieldStorage
import Cookie
def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    try:
        if environ['REQUEST_METHOD']=='GET':
            path=environ['PATH_INFO'][1:]
            if path.endswith(".html"):
                response_headers = [('Content-Type', 'text/html')]
                start_response(status, response_headers)
                f = open(curdir + sep + path,'rb')  # self.path has /test.html

                return f.read()
                f.close()
            elif path.endswith(".jpg"):
                response_headers = [('Content-Type', 'image/jpg')]
                start_response(status, response_headers)
                f = open(curdir + sep + path,'rb')  # self.path has /test.html

                return f.read()
                f.close()
            elif path.endswith(".gif"):
                response_headers = [('Content-Type', 'image/gif')]
                start_response(status, response_headers)
                f = open(curdir + sep + path,'rb')  # self.path has /test.html

                return f.read()
                f.close()
            elif path.endswith(".js"):
                response_headers = [('Content-Type', 'application/javascript')]
                start_response(status, response_headers)
                f = open(curdir + sep + path,'rb')  # self.path has /test.html

                return f.read()
                f.close()
            elif path.endswith(".css"):
                response_headers = [('Content-Type', 'text/css')]
                start_response(status, response_headers)
                f = open(curdir + sep + path,'rb')  # self.path has /test.html

                return f.read()
                f.close()
            else:
                f = open(curdir + sep + path, 'rb')  # self.path has /test.html

                return f.read()
                f.close()
        if environ['REQUEST_METHOD'] == 'POST':
            path = environ['PATH_INFO'][1:]
            if path.endswith("new.html"):
                try:
                    request_body_size = int(environ['REQUEST_HEADERS']['Content-Length'])
                except (ValueError):
                    request_body_size = 0


                input=environ['wsgi.input']
                request_body = environ['wsgi.input']
                handler = {}
                if 'Cookie' in environ['REQUEST_HEADERS']:
                    if environ['REQUEST_HEADERS']['Cookie']:
                        cookies=environ['REQUEST_HEADERS']['Cookie']
                        cookies = cookies.split('; ')
                        handler = {}
                        for cookie in cookies:
                            cookie = cookie.split('=')
                            handler[cookie[0]] = cookie[1]
                        print handler
                    d = parse_qs(request_body)
                    food = d.get('name11', [''])[0]
                    if 'username' in handler:
                        if handler['username']=='nikhil':
                            return handler['username']+'take your yummy'+food
                        else:
                            return "please login dude yaar"
                    else:
                        return "please login dude"
                else:
                    return "please login bro"
            if path.endswith("upload.html"):
                try:
                    request_body_size = int(environ['REQUEST_HEADERS']['Content-Length'])
                except (ValueError):
                    request_body_size = 0


                input = environ['wsgi.input']
                request_body = environ['wsgi.input']
                handler = {}
                print 'wsgi.input text is here'
                print environ['wsgi.input']
                print 'REQUEST_BODY input is here'
                print environ['REQUEST_BODY']
                data=environ['wsgi.input']
                data = data.split('\r\n\r\n')
                fi = data[1].split(';')
                fi = fi[2].split('\r\n')
                fi = fi[0]
                leng = len(fi)
                filename = fi[11:len(fi) - 1]
                f = open(filename, 'wb')
                finaldata = data[2].split('\r\n')
                # print finaldata
                f.write(finaldata[0])
                f.close()

                return "success"
            if path.endswith("login.html"):
                try:
                    request_body_size = int(environ['REQUEST_HEADERS']['Content-Length'])
                except (ValueError):
                    request_body_size = 0


                input=environ['wsgi.input']
                request_body = environ['wsgi.input']
                d = parse_qs(request_body)
                username = d.get('username', [''])[0]
                password = d.get('password', [''])[0]
                if username=='nikhil' and password=='nikhil':
                    C = Cookie.SimpleCookie()
                    C['username']='nikhil'
                    C['password']='nikhil'
                    print C
                    response_headers = [('Content-Type', 'text/html'),('Cookie',C)]
                    start_response(status, response_headers)
                    f = open('new.html', 'rb')  # self.path has /test.html

                    return f.read()
                    f.close()
                else:
                    f = open('login.html', 'rb')  # self.path has /test.html
                    return f.read()
                    f.close()

    except IOError:
        status ='404 Not Found'
        start_response(status, response_headers)
        return "404 Not found"

