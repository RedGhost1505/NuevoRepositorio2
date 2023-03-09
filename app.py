from flask import Flask, render_template, request, redirect

app= Flask(__name__)

url = 'https://api-todo-list-85ve.onrender.com/api/tasks'

@app.route('/', methods=['GET','POST'])
def home():
    if request.method== 'GET':
        return render_template('index.html')


    else:  #Post
        pass



if __name__ == '__main__':
    app.run(debug=True)

