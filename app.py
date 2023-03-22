# ------------------------------------------------------------
# Josua Alejandro Zamarrón Ramírez 
# Marzo/22/2023
# ------------------------------------------------------------

from flask import Flask, render_template, request, redirect, abort
from requests import get, post


app= Flask(__name__)

url = 'https://api-todo-list3.onrender.com/api/tasks'

@app.route('/', methods=['GET','POST'])

def home():

    complete_tasks= {}
    incomplete_tasks={}

    if request.method== 'GET':
        try:
            tasks = get(url+'tasks').json()
        except:
            abort(500)
        
        for task in tasks['tasks']:
            if task['estado']:
                complete_tasks[task['id']] = task
                complete_tasks[task['id']].pop('id')

        return render_template('index.html', content={'complete_tasks':complete_tasks,'incomplete_tasks':incomplete_tasks},uncompleted_len=len(incomplete_tasks),completed_len=len(complete_tasks))
    
    else: #Post
        post_data = {'name':request.form.get('name')}
        try:
            task = post(url+'append',data=post_data).json()
        except:
            abort(500)
        
        for task in tasks['tasks']:
            if task['estado']:
                complete_tasks[task['id']] = task
                complete_tasks[task['id']].pop('id')
            elif not task['estado']:
                incomplete_tasks[task['id']] = task
                incomplete_tasks[task['id']].pop('id')
     
        return render_template('index.html', content={'complete_tasks':complete_tasks,'incomplete_tasks':incomplete_tasks},uncompleted_len=len(incomplete_tasks),completed_len=len(complete_tasks))


if __name__ == '__main__':
    app.run(debug=True)

