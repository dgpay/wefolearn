from app import *
from models import *
from hashlib import md5

@app.route('/')
def showHome():
    return render_template('index.html')


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        try:
            idM = request.form['id_mahasiswa']
            firstnam = request.form['firstname']
            lastnam = request.form['lastname']
            kls = request.form['kelas']
            passw = request.form['password']
            mail = request.form['email']

            
            register = mahasiswa(id_Mahasiswa= idM,firstname=firstnam,lastname=lastnam,kelas=kls, password = passw, email = mail)
            db.session.add(register)
            db.session.commit()
            flash("REGISTASI BERHASIL!!")
            return redirect(url_for("showHome")) 
        except:
            flash("Maaf,Silahkan lengkapi data pribadi anda!") 

    return render_template("registrasi.html")


# @app.route("/login",methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         uname = request.form["uname"]
#         passw = request.form["passw"]
        
#         login = user.query.filter_by(username=uname, password=passw).first()
#         if login is not None:
#             return redirect(url_for("index"))
#     return render_template("login.html")    

