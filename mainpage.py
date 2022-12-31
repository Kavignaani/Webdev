from flask import Flask, render_template,request,redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return render_template('mainpage.html')

@app.route('/big3', methods=['GET'])
def big():
  return render_template('Big3.html')

@app.route('/Finance', methods=['GET'])
def fin():
  return render_template('Finance.html')

@app.route('/Operations', methods=['GET'])
def ops():
  return render_template('Operations.html')


@app.route('/Prod',methods=['GET'])
def prod():
  return render_template('Prod.html')

@app.route('/AML',methods=['GET'])
def aml():
  return render_template('AML.html')


@app.route('/submit', methods=['GET','POST'])
def getvalue():
  print("Step1over")     
  name=request.form['name']
  date=request.form['date']
  intime=request.form['intime']
  outtime=request.form['outtime']

  inh=int(intime[0:2])
  outh=int(outtime[0:2])
  intm=int(intime[3:5])
  if intm > 0 :
    k=1
  else :
    k=0
  global rows
  rows=outh-inh+k
  print("Steip2")
  x=[]
  for i in range(1,rows+1):
    k="PJ"+str(i)
    x.extend(request.form[k])
  print("WORKED")
  print(x)
  return render_template('AML.html')


if __name__ == '__main__':
  app.run(debug=True)
