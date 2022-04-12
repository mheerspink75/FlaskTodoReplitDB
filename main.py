from flask import Flask, render_template, redirect, request
from datetime import datetime
from replit import db

app = Flask(__name__)

date = datetime.now().date()

class Todo:
    def __init__(self, id, task, date, completed):
        self.id = id
        self.task = task
        self.date = str(date)
        self.completed = completed


@app.route('/', methods=['POST', 'GET'])
def index():
    if not db.__contains__('tasks'):
        try:
            tasks = {'tasks': []}
            db.set_bulk(tasks)
        except:
            return 'The is a problem creating the database'
    if request.method == 'POST':
        try:
            if db.__contains__('tasks'):
                new_task = request.form['content']
                todo = Todo(len(db['tasks']), new_task, date, False)
                for key in db.keys():
                    db[key].append(vars(todo))
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        my_tasks = db['tasks']
        for i in range(len(my_tasks)):
            if i != my_tasks[i]['id']:
                my_tasks[i]['id'] = i
        return render_template('index.html', my_tasks=my_tasks)


@app.route('/delete/<int:id>')
def delete(id):
    try:
        my_tasks = db['tasks']
        del my_tasks[id]
        return redirect('/')
    except:
        return 'There was a problem deleting your task'


@app.route('/complete/<int:id>')
def complete(id):
    try:
        my_tasks = db['tasks']
        my_tasks[id]['completed'] = not my_tasks[id]['completed']
        return redirect('/')
    except:
        return 'There was a problem deleting your task'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = db['tasks'][id]['task']
    if request.method == 'POST':
        task_content = request.form['content']
        try:
            db['tasks'][id]['task'] = task_content
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', id=id, task=task)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
