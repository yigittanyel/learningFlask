from flask import Flask,render_template,url_for,redirect

app=Flask(__name__)
@app.route("/")
def index():
    #return "Merhaba"
    return "<h1> Merhaba </h1>"
    #return render_template('index.html')
    #return redirect(url_for('about'))

@app.route("/about")
def about():
    return "<h2> About page </h2>"

@app.route("/meyveler")
def meyveler():
    meyveler=["elma","armut","muz","kivi"]
    return render_template("meyveler.html",meyveler=meyveler)

@app.route("/name/<string:name>",methods=["GET"])
def name(name):
    return "Hello,%s" %name

@app.route("/kisi/<int:id>")
def kisiId(id):
    return "Hoşgeldin %d" %id

@app.route("/static")
def static_image():
    return render_template('static.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__=='__main__':
    app.run()

