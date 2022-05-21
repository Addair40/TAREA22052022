import web

render = web.template.render("templates/views/")

class Ubuntu():

    def GET(self):
        try:
            return render.ubuntu()
        except Exception as e:
            return "ERROR " + str(e.args)
