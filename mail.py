from flask import Flask
import smtplib

app = Flask(__name__)

def correobienvenida(correo):
    cuerpo= 'subject: Bienvenido a SawFilms\n\nBienvenido a SawFilms, vea los mejores estrenos y asegure su silla en https://sawfilms.herokuapp.com/'

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()

    servidor.login('sawfilms2021@gmail.com','sawfilms0987654321')

    servidor.sendmail('sawfilms2021@gmail.com',correo,cuerpo)

    servidor.quit()

def recuperarcontaseña(correo,contraseña):
    cuerpo= 'subject: Cambio de contraseña en SawFilms\n\nBienvenido a SawFilms, su nueva contraseña es: {}'.format(contraseña)

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()

    servidor.login('sawfilms2021@gmail.com','sawfilms0987654321')

    servidor.sendmail('sawfilms2021@gmail.com',correo,cuerpo.encode("utf8"))

    servidor.quit()