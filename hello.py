from flask import Flask
import subprocess
import RPi.GPIO as GPIO
from time import sleep

app = Flask(__name__)

@app.route('/')
def hello():
    GPIO.setmode(GPIO.BOARD)
    Motor1A = 16
    Motor1B = 18
    Motor1E = 22

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    print("Turning motor on")

    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

    sleep(20)
    print("stopping motor")
    GPIO.output(Motor1E,GPIO.LOW)

    GPIO.cleanup()

    return "Test"

@app.route('/lumiere/allume/<valeurlum>')
def lumiereAllume(valeurlum):
    return 'True %s' % valeurlum

@app.route('/lumiere/eteint/<valeurlum>')
def lumiereEteint(valeurlum):
    return 'False %s' % valeurlum

@app.route('/volet/ouvre/<valeurVolet>')
def voletOuvre(valeurVolet):
    return 'True %s' % valeurVolet

@app.route('/volet/ferme/<valeurVolet>')
def voletFerme(valeurVolet):
    return 'False %s' % valeurVolet
