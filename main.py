from flask import *
from data import *
app=Flask(__name__)
@app.route('/login')
def main():
    return render_template('S.html')
@app.route('/att_gen')
def fac():
    return render_template('1.html')
@app.route('/std_att')
def stud():
    return render_template('2.html')
@app.route('/registration')
def reg():
    return render_template('3.html')
@app.route('/mys',methods=['POST','GET'])
def mys():
    result=request.form
    storedata(result)
    return 'S'
if __name__=='__main__':
    app.run(debug=True)

