import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("email","password")
server.sendmail("from:","to:","text")
server.quit()
