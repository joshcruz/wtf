from flask import render_template
from app import app

import random

@app.route('/')
@app.route('/index')
def wtf():
    with open('wtf-extension.txt','r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        print(random_line)
    return render_template("index.html", random_line=random_line)

if __name__ == '__main__':
    app.run(debug=True)