from app import *
from models import *
from hashlib import md5

# def whoThis():
#     session.permanent = True
#     if request.form["id_mahasiswa"]!='' and request.form["password"]!='' :
#         idM = request.form["id_mahasiswa"]
#         session["idM"]=idM
#         passw = request.form["password"]
#         session["passw"]=passw

#         found_user = mahasiswa.query.filter_by(id_Mahasiswa=idM, password=passw).first()
#         if found_user is not None:
#             flash("LOgin Succsessfull!!")
#             return redirect(url_for("mhs"))
        
#     elif request.form["id_mahasiswa"]!='' and request.form["password"]!='' :
#         idAS = request.form["id_dosAsis"]
#         session["idAS"]=idAS
#         passwAS = request.form["password_AS"]
#         session["passw"]=passwAS

#         found_user = Dos_Asis.query.filter_by(id_DosAsis=idAS, password=passwAS).first()
#         if found_user is not None:
#             flash("LOgin Succsessfull!!")
#             return redirect(url_for("mhs"))
    

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


@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        if request.form["id_mahasiswa"]!='' and request.form["password"]!='' :
            idM = request.form["id_mahasiswa"]
            session["idM"]=idM
            passw = request.form["password"]
            session["passw"]=passw

            found_user = mahasiswa.query.filter_by(id_Mahasiswa=idM, password=passw).first()
            if found_user is not None:
                flash("LOgin Succsessfull!!")
                return redirect(url_for("mhs"))
        
        elif request.form["id_dosAsis"]!='' and request.form["password_AS"]!='' :
            idAS = request.form["id_dosAsis"]
            session["idAS"]=idAS
            passwAS = request.form["password_AS"]
            session["passw"]=passwAS

            found_user = Dos_Asis.query.filter_by(id_DosAsis=idAS, password=passwAS).first()
            if found_user is not None:
                flash("LOgin Succsessfull!!")
                return redirect(url_for("mhs"))
        else:
            flash("Ada kesalahan dalam pengisian form!!")
            return redirect(url_for("login"))
    else:
        if "idM" and "passw" in session:
            flash("already login!")
            return redirect(url_for("mhs"))
        elif "idAS" and "passwAS" in session:
            flash("already login!")
            return redirect(url_for("dosAs"))
        return render_template("login.html")  

@app.route('/mahasiswa')
def mhs():
    if "idM" in session:
        return render_template('mahasiswa.html')  
    else:
        flash("you are not login")
        return redirect(url_for("login"))

@app.route('/dosen-asisten')
def dosAs():
    if "idAS" in session:
        return render_template('dosAsis.html')  
    else:
        flash("you are not login")
        return redirect(url_for("login"))
    

@app.route('/view-profil-siswa')
def view():
    return render_template("view.html",values=mahasiswa.query.all())
