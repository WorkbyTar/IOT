import RPi.GPIO as GPIO
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.IN)
GPIO.setup(15,GPIO.OUT)
prev_input01 = 0
prev_input02 = 0
counter01 = 0
counter02 = 0

while True:
  input01 = GPIO.input(7) 
  input02 = GPIO.input(13)

  if (input01 == True):
    GPIO.output(11,GPIO.HIGH)
  else:
    GPIO.output(11,GPIO.LOW)

      
  if ((not prev_input01) and input01):
    #GPIO.output(11,GPIO.LOW)
    print("Button Pressed Player 1")
    counter01 = counter01+1
    print counter01
  prev_input01 = input01
  time.sleep(0.05)

  if (counter01 > 20):
    fromaddr = "email@gmail.com"
    toaddr = "email@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg ['Subject'] = "THE WINNER IS"

    body = "PLAYER 1"
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromaddr,'****')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    break
    GPIO.output(11,GPIO.HIGH)


  if (input02 == True):
    GPIO.output(15,GPIO.HIGH)
  else:
    GPIO.output(15,GPIO.LOW)

      
  if ((not prev_input02) and input02):
    #GPIO.output(11,GPIO.LOW)
    print("Button Pressed Player 2")
    counter02 = counter02+1
    print counter02
  prev_input02 = input02
  time.sleep(0.05)

  if (counter02 > 20):
    fromaddr = "Email@gmail.com"
    toaddr = "Email@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg ['Subject'] = "THE WINNER IS"

    body = "PLAYER 2"
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromaddr,'****')
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    break

    GPIO.output(15,GPIO.HIGH)

GPIO.cleanup()
