from flask import Flask
import smtplib

app = Flask(__name__)

def correobienvenida(correo):
    cuerpo= 'subject: Bienvenido a Cine Colombia\n\nBienvenido a CineColombia, vea los mejores estrenos y asegure su silla en https://cinecolombiawz.herokuapp.com/'

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()

    servidor.login('cinecolombiawz@gmail.com','123cinecolombiawz')

    servidor.sendmail('cinecolombiawz@gmail.com',correo,cuerpo)

    servidor.quit()

def recuperarcontaseña(correo,contraseña):
    cuerpo= 'subject: Cambio de contraseña en Cine Colombia\n\nBienvenido a CineColombia, su nueva contraseña es: {}'.format(contraseña)

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()

    servidor.login('cinecolombiawz@gmail.com','123cinecolombiawz')

    servidor.sendmail('cinecolombiawz@gmail.com',correo,cuerpo.encode("utf8"))

    servidor.quit()


# from flask import Flask
# import flask_mail, Mail, Message

# # Configuración de correo electrónico

# MAIL_SERVER = "smtp.qq.com" # Servidor de correo electrónico, uso el servidor de correo electrónico qq 
# MAIL_PORT = 465 # Puerto
# MAIL_USE_SSL = True # QQ usa el protocolo SSL
# MAIL_USE_TSL = False
# MAIL_USERNAME = "cinecolombiawz@gmail.com" # Buzón qq propio
# MAIL_PASSWORD = "123cinecolombiawz" # La contraseña aquí es la última introducción
# MAIL_DEFAULT_SENDER = "cinecolombiawz@gmail.com"

# app = Flask(__name__) # pick the name
# mail = Mail()
# mail.init_app(app)

# def bienvenidaemail(correo):
#     msg = Message( 
#                 'Bienvenido a CineColombia, vea los mejores estrenos y asegure su silla en https://cinecolombiawz.herokuapp.com/', 
#                 sender ='cinecolombiawz@gmail.com', 
#                 recipients = [correo] 
#                ) 
#     msg.body = 'Hello Flask message sent from Flask-Mail'
#     mail.send(msg)

# def recuperarcontraseña(correo):
#     msg = Message( 
#                 'Bienvenido a CineColombia, vea los mejores estrenos y asegure su silla en https://cinecolombiawz.herokuapp.com/', 
#                 sender ='cinecolombiawz@gmail.com', 
#                 recipients = [correo] 
#                ) 
#     msg.body = 'Hello Flask message sent from Flask-Mail'
#     mail.send(msg)