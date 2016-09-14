import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "email@email.email"
toaddr = "email@email.email"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "YOUR IMAGE LINKS"

var1 = raw_input("cat or dog: ")
var2 = raw_input("baby or old person: ")
var3 = raw_input("win or fail: ")

if var1 == 'cat' :
	var1result = 'CAT: https://s-media-cache-ak0.pinimg.com/236x/ff/db/78/ffdb783d33d132470318966dc1ba5ec5.jpg  '
elif var1 == 'dog':
	var1result = 'DOG: http://lh3.googleusercontent.com/-z0opiDRji70/VVKyrewOIcI/AAAAAAAAFqE/Qw21oAzBsO8/s640/Funny%20Dog%20Photos%20For%20Whatsapp%20MyWhatsappimages.blogspot.comIMG_45916619536719.jpg   '
else: var1result = 'CAT OR DOG: not a real answer, try again!'

if var2 == 'baby' :
	var2result = 'BABY: http://370g431nca8u23kfvb3cilkf.wpengine.netdna-cdn.com/wp-content/uploads/2013/05/6a0133f30ae399970b01901c5cf6ec970b-800wi.jpg  '
elif var2 == 'old person':
	var2result = 'OLD PERSON: http://funnystack.com/wp-content/uploads/2014/03/Funny-Old-People-3.jpg  '
else: var2result = 'BABY OR OLD PERSON: not a real answer, try again!   '

if var3 == 'win' :
	var3result = 'WIN: http://i.dailymail.co.uk/i/pix/2011/05/20/article-1389182-0C155FB300000578-158_634x516.jpg   '
elif var3 == 'fail' :
	var3result = 'FAIL: http://img.memecdn.com/Epic-Catch-Fail_o_145727.jpg'
else: var3result = 'WIN OR FAIL: not a real answer, try again!   '

result = var1result + var2result + var3result

body = result

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "*****")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

