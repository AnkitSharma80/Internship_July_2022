from flask import Flask,render_template, request
import re

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        target = request.form.get('target')
        regex = request.form.get('regex')
        lst = re.findall(regex,target)
        length_lst = len(lst)

        return render_template("code.html",lst=lst, length_lst=length_lst,target=target)
    return render_template("code.html")

if __name__ == '__main__':
    app.run(debug=True)