import web

render = web.template.render("templates/views/")

class Docker():

    def GET(self):
        try:
            return render.docker()
        except Exception as e:
            return "ERROR " + str(e.args)
