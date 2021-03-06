
from fileinput import filename
from pydoc import describe
from re import U
from app import app 
from flask import render_template, request, redirect,jsonify,make_response

import os
from werkzeug.utils import secure_filename
# from datetime import datetime

# @app.template_filter("clean_date")
# def clean_date(dt):
#       return dt.strftime("%d %b %y")

@app.route('/')
def index():
   return render_template("public/index.html ")

@app.route("/jinja")
def jinja():
    my_name = "NTN"
    age = 28
    langs = ["Python","JavaScript","C#","Ruby"]
    friends = {
        "Tom": 30,
        "Amy": 56,
        "Tony": 33,
        "bvp": 121
    }
    colours = ("Red","Green")
    cool = True
    class GitRemote:
        def __init__(self, name, description, url):
            self.name=name
            self.description= description
            self.url= url
        def pull(self):
            return f"Pullin repo {self.name}"
        def clone(self):
            return f"Cloning into {self.url}"
        
    my_remote = GitRemote(
        name= "Flask Jinja",
        description="Template design ",
        url="wwww3school.com"
    )
    
    def  repeat(x, qty):
        return x * qty
      
    # date = datetime.utcnow(datetime)
    
        
    return render_template("public/jinja.html", my_name=my_name,
                           langs=langs,age=age,friends=friends,
                           colours=colours,cool=cool,GitRemote=GitRemote,
                           repeat=repeat, my_remote=my_remote)

@app.route("/about")
def about():
    return "<h1 style='color:red'>About</h1>"


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        req = request.form
        
        username = req["username"]
        email = req.get("email")
        password = redirect.form["password"]

        print(username,email,password)
        return redirect(request.url)

    return render_template("public/sign_up.html")



users = {
    "mitsuhiko": {
    "name": "Armin Ronacher",
    "bio": "Creator if the Flask framwork",
    "twitter_handle": "@mitsuhiko"
    },
     "gvanrossum": {
    "name": "Guido Van Rossum",
    "bio": "Creator if the Flask framwork",
    "twitter_handle": "@gvanrossum"
    },
     "elonmusk": {
    "name": "Elon Musk",
    "bio": "Creator if the Flask framwork",
    "twitter_handle": "@elonmusk"
    },
     "NTN": {
    "name": "Nghia Nguyen ",
    "bio": "Creator if the Flask framwork",
    "twitter_handle": "@nghianguyen"
    }

}

@app.route("/profile/<username>")
def profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template("public/profile.html",username=username, user = user)


# @app.route("multiple/<foo>/<bar>/<baz>")
# def multi(foo,bar,baz):
#     return f"foo is {foo}, bar is {bar}, baz is {baz}"


@app.route("/json", methods=["POST"])
def json():

    if request.is_json:
        req = request.get_json()

        response = {
            "message" :  "JSON received!",
            "name": req.get("name")
        }

        res = make_response(jsonify(response), 200)

        return res
    else:
        res = make_response(jsonify({"message": "No received!"}),400 )
        return "No JSON received!", 400

    # return "Thanks!", 200


    #Fetch API (Ajax)

@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()
    
    print(req)
    
    res = make_response(jsonify(req), 200)
    return res


@app.route("/query")
def query():
    
   
    # if request.args:
    #     args = request.args
    #     serialized = "," .join(f"{k}: {v}" for k, v in args.items() ) 

    #     return f"(Query) {serialized}" ,200
    # else:
    #     return "No query received", 200 

    print(request.query_string)
    return "No query received", 200

app.config["IMAGE_UPLOADS"]="C:/Users/kisst/OneDrive/M??y t??nh/python/app/static/img/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG","JPEG", "GIF"]

def allowed_image(filename):
    if not "." in filename:
        return
    ext = filename.rsplit(".",1)[1]
    
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False
    
@app.route("/upload-image", methods=["GET","POST"])
def upload_image():

    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename =="":
                
               print("Image must have a filename")
               return redirect(request.url) 
            if allowed_image(image.filename):
                print("That image extension is not allowed")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))



            
            print("Image saved")
            return redirect(request.url)
    return render_template("public/upload_image.html")    