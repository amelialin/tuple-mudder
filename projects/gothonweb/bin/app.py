import web # imports the web.py module
from web import form # allows you to create forms

urls = (
    '/', 'index', # a mapping; this means that when someone hits the homepage, lpthw.web will go find the class named 'index' and load it
    # here you would list more page mappings
    '/addtodo', 'addtodo',
    '/todos', 'todos'
)

app = web.application(urls, globals())

render = web.template.render('templates/') # go look for an HTML template. This is a web.template.render object. It loads HTML files out of the templates/ directory.

todoform = form.Form(
    form.Textbox('username', description='Username:'),
    form.Password('password', 
            form.Validator("Password must be more than 2 chars", lambda x:len(x)>2),
            description='Password:'),
    form.Textarea('todo', 
            form.notnull,
            description='To Do Item:'),
    form.Checkbox('checkbox', description='Check this box:'),
    form.Dropdown('dropdown', ['1','2','3'],description='Pick one:'),
#    form.Button('Login'),
)

db = web.database(dbn='sqlite', db='testdb') # connect Python to SQLite3 db

class index(object):
    def GET(self): # returns string for what lpthw.web should send back to the browser to display
        greeting = "Hello"
        i = web.input(name=None) # looks for a parameter in the URL like "?name=Joe"
        return render.index(greeting = greeting, name = i.name) # calls render.index and passes in greeting variable, with the value set equal to what the local greeting variable is. Makes what's returned on the webpage way fancier. Change render.<filename> to pass the variable to a different template file.

class addtodo(object):
    def GET(self):
        form = todoform() # get a copied instance of the form
        print form.render() # call the render method on it to convert to HTML
        return render.addtodo(form) # pass the form to the addtodo.html template

    # def POST(self): # what happens if the form gets submitted
    #     form = todoform()
    #     if form.validates():
    #         return 'Success! Username: %s' % (form['Password:'].value) # how you pull out values from the form
    #     else:
    #         return render.addtodo(form)

    def POST(self): # post data to db
        form = todoform()
        if form.validates():
            db.insert('todo', title=form['todo'].value)
            return render.addtodo_confirm(form['todo'].value)
        else:
            return render.addtodo(form)

class todos(object):
    def GET(self):
        todos = db.select('todo') # selects the todo table
        return render.todos(todos)

if __name__ == "__main__":
    app.run()