from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/viajes')
def viajes():
    return render_template('viajes.html')

@app.route('/visas')
def visas():
    return render_template('visas.html')

@app.route('/contactenos')
def contactenos():
    return render_template('contactenos.html')

if __name__ == '__main__':
    app.run(debug=True)








