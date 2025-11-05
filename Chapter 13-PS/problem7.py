# at chapter 13-PS folder open cmd
# pip freeze > requirements.txt
# virtualenv dibboenv
# pip install flask
# search flask. enter the flask link.then at quick start go to the a minimal application and copy the code
from flask import Flask # aager gula install korle ei error dekhabe  ah

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()
# flask will help to create api and website
# other process of flask, we can learn from documentation