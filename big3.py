from flask import Flask, render_template

app = Flask(__name__)

@app.route('/big3')
def home():
  return render_template('Big3.html')

@app.route('/AML')
def AML():
  return render_template('AML.html')

@app.route('/Prod')
def prod():
  return render_template('Prod.html')


if __name__ == '__main__':
  app.run()
