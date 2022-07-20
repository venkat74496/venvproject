from flask import *
from data import *
app=Flask(__name__)
app.secret_key = 'any random string'

@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/reg')
def reg():
    
    return render_template("reg.html")
@app.route('/store',methods=["POST"])
def store():
    x=request.form
    storestudent(x)
    return render_template("index.html")
@app.route('/storebatch',methods=["POST"])
def storebatch():
    x=request.form
    
    e=[str(x)for x in range(10)]
    a=[chr(x)for x in range(ord('a'),ord('z')+1)]
    b=[chr(x)for x in range(ord('A'),ord('Z')+1)]
    import random
    n=''
    for k in range(2):
        n+=random.choice(e)
        n+=random.choice(a)
        n+=random.choice(b)
    stores(x,n,session['email'])
    return n
@app.route('/storeat',methods=["POST"])
def storeat():
    x=request.form
    storeats(x,session['email'])
    return "s"
@app.route('/afterlogin',methods = ['POST', 'GET'])
def afterlogin():
    result = request.form
    print(result)
    n=[]
    n=login(result["email"],result["pswd"])
    if(len(n)!=0):
         session['name']=n[0][0]
         session['role']=n[0][1]
         session['email']=n[0][2]
         if n[0][1]=="faculty":
             return render_template("admin.html")
         else:
            return render_template("student.html")
    else:
        error = 'Invalid username or password. Please try again!'
        return render_template("index.html",error=error)
@app.route('/logout')
def logout():
    error = 'Your Logged out successfully'
    session.pop('name', None)
    session.pop('role', None)
    session.pop('email', None)
    return render_template("index.html",error=error)
if __name__=='__main__':
    app.run(debug="True")
