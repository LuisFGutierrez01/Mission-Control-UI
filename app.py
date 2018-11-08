from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/demo")
def demo():
    return render_template('demo.html')

@app.route("/info")
def info():
    return render_template('info.html')

@app.route("/stream")
def stream():
    return render_template('stream.html')


if __name__ == '__main__':
    app.run(debug=True)
