from flask import Flask   # 导入flask模块中的 Flask 方法

app = Flask(__name__)    # 新建一个Flask对象


@app.route("/")             # 新建一个路由装饰器和对应的视图函数
def hello():
    return 'hello world !'

if __name__ == '__main__':    # 运行
    app.run(debug=True)       # 开启debug模式，修改后会自动重启