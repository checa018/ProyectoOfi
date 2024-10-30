import urllib.parse

class Config:
    # Escapar caracteres especiales en la contraseña
    password = urllib.parse.quote_plus("admin")
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{password}@localhost/proyec"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
