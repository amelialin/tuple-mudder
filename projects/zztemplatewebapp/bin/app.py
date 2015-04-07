import web # imports the web.py module
from web import form # allows you to create forms

urls = (
    '/', 'index', # a mapping; this means that when someone hits the homepage, lpthw.web will go find the class named 'index' and load it
    # here you would list more page mappings
    '/login', 'login'
)

app = web.application(urls, globals())

render = web.template.render('templates/') # go look for an HTML template. This is a web.template.render object. It loads HTML files out of the templates/ directory.

loginform = form.Form(
    form.Textbox('Username:'),
    form.Password('Password:'),
    form.Button('Login'),
)

class index(object):
    def GET(self): # returns string for what lpthw.web should send back to the browser to display
        greeting = "Hello"
        i = web.input(name=None) # looks for a parameter in the URL like "?name=Joe"
        return render.index(greeting = greeting, name = i.name) # calls render.index and passes in greeting variable, with the value set equal to what the local greeting variable is. Makes what's returned on the webpage way fancier. Change render.<filename> to pass the variable to a different template file.

class login(object):
    def GET(self):
        f = loginform() # call login to get a copied instance of the login form
        print f.render() # call the render method on it to convert to HTML
        greeting = 'Login now!'
        return render.login(loginform) # pass the login form to the login.html template

if __name__ == "__main__":
    app.run()