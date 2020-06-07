from app import db

class mahasiswa(db.Model):

    id_Mahasiswa = db.Column(db.String, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, index=True)

class Dos_Asis(db.Model): #ini dosen dan asisten

    id_DosAsis = db.Column(db.String, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, index=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True, index=True)

if __name__ == "__main__":
    print("Membuat Table nya...")
    db.create_all()
    print("SELESAI!")