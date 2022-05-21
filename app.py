import web

urls = (
    '/', 'templates.mvc.index.Index',
    '/siguiente', 'templates.mvc.docker.Docker',
    '/siguiente1', 'templates.mvc.ubuntu.Ubuntu',
)
app = web.application(urls, globals())



if __name__ == "__main__":
    app.run()
