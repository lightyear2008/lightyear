from flask import request, Flask, render_template

#更改run_app的值来选择运行哪个app
run_app = 6
print(f'app{run_app} is running!',end = '\n\n')


app1 = Flask(__name__)
@app1.route('/')
#最简单的路由，访问根目录时显示Hello, World!
def submit1():
    return '<h1>Hello, World!</h1>'


app2 = Flask(__name__)
@app2.route('/', methods=['POST'])#只能用POST请求访问
#获取请求表单中的username并显示(data字典)
def submit2():
    username = request.form.get('username')#form用于处理表单数据
    return f'Form submitted by {username}!'


app3 = Flask(__name__)
@app3.route('/<param>')
#把HTML文件(保存在templates文件夹中)渲染到浏览器上，并把URL中的param参数以username为名传递给HTML文件(在HTML中用{{username}}来调用)
def submit3(param):
    return render_template('hello.html', username=param)
@app3.route('/')
#当没有指定username参数时显示错误信息(这仍然是一个200状态码的响应)
def submit3_error():
    return '<h1>Please enter a username in the URL</h1>'


app4 = Flask(__name__)
@app4.route('/')
#获得请求头中的User-Agent并显示
def submit4():
    users_agent = request.headers.get('User-Agent')
    return f'Your users_agent is: {users_agent}'
#当app4运行出现404错误时调用的函数，errorhandler括号中可以指定错误代码(>=400)
@app4.errorhandler(404)
def not_found(error):
    return 'Page not found', 404


app5 = Flask(__name__)
@app5.route('/')
def submit5():
    return '<h1>Hello, World!</h1>'
#访问根目录前执行的函数(钩子)
@app5.before_request
def app5_before_request():
    print('before_request')
#访问根目录后执行的函数(钩子)
@app5.after_request
def app5_after_request():
    print('after_request')


import os
from flask import send_from_directory#用于从指定目录中发送文件到客户端
app6 = Flask(__name__)
@app6.route('/upload', methods=['POST'])
#获取post请求中file参数并保存到upload文件夹中
def submit6():
    file = request.files.get('file')
    if file:#检查是否有文件上传
        upload_folder = 'upload/'
        if not os.path.exists(upload_folder):#如果路径不存在则创建路径
            os.makedirs(upload_folder)
        file.save(os.path.join(upload_folder, file.filename))
        return 'File uploaded successfully'
    return 'No file uploaded'
#用于查看上传的文件(例如向http://127.0.0.1:5000/upload上传了test.txt文件，则在http://127.0.0.1:5000/uploads/test.txt可以查看上传的文件)
@app6.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('upload', filename)#把文件发到客户端


if __name__ == '__main__':
    if run_app == 1:
        app1.run(host='0.0.0.0', port=5000,debug=True)
    elif run_app == 2:
        app2.run(host='0.0.0.0', port=5000,debug=True)
    elif run_app == 3:
        app3.run(host='0.0.0.0', port=5000,debug=True)
    elif run_app == 4:
        app4.run(host='0.0.0.0', port=5000,debug=True)
    elif run_app == 5:
        app5.run(host='0.0.0.0', port=5000,debug=True)
    elif run_app == 6:
        app6.run(host='0.0.0.0', port=5000,debug=True)
