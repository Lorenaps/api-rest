from flask import Flask
app = Flask('app')

@app.route("/")
def hello():
    return "Hello World!"

app.run(debug=True, use_reloader=True)

if __name__ == "__main__":
    app.run()

