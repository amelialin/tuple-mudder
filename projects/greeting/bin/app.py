# LPTHW Ex 51

import web # imports the web.py module

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
    def GET(self):
        # form = web.input(name="Nobody")
        # greeting = "Hello"

        # return render.index(greeting = greeting, name = form.name)
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greeting="Hello")
        greeting = form.greeting
        return render.index(greeting = greeting, name = form.name)
if __name__ == "__main__":
    app.run()