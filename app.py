from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/destinations')
def destinations():
    return render_template('destinations.html')

@app.route('/culture')
def culture():
    return render_template('culture.html')

@app.route('/plan')
def plan():
    return render_template('plan.html')

if __name__ == '__main__':
    app.run(debug=True)