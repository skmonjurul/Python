from flask import Flask, render_template

app1=Flask(__name__)

@app1.route('/')
def homePage():
    return render_template("homepage.html")

@app1.route('/firstpg')
def firstPage():
    return render_template("first_page.html")

if __name__=="__main__":
    app1.run(debug=True)
