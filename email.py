import smtplib
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("500061440@stu.upes.ac.in","vedansh1516")
server.sendmail("500061440@stu.upes.ac.in","vedanshsinghal@gmail.com","hello i just send a email using python")
server.quit()