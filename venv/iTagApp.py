from flask import render_template,url_for, redirect
from __init__ import app
'commit'
@app.route('/')
def index():
    return render_template('index.html')
' uses __init__.py'
if __name__=='__main__':
    app.run(host="localhost", port=5001, debug=True)
