from flast import Flask


app= flast(__name__)

@app.route("/info")
def lw():
    return "Welcome, this is Abhishek Malviya"

app.run(host='0.0.0.0')
