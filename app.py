from flask import Flask, render_template, request, redirect
import requests
app= Flask(__name__)

url = 'https://api-todo-list3.onrender.com/api/tasks'

@app.route('/', methods=['GET','POST'])

def home():
    if request.method== 'GET':
        tasks = requests.get(url).json()['tasks']
        completed=[]
        incompleted=[]
        for task in tasks:
            if task['status']== True:
                completed.append(task)
            else:
                incompleted.append(task)
        
        print(f'COMPLETADAS: {completed}')
        print(f'INCOMPLETED: {incompleted}')

        response ={'completed': completed,
                   'incompleted':incompleted}
        return render_template('index.html', response=response)


    else:  #Post
        pass



if __name__ == '__main__':
    app.run(debug=True)

