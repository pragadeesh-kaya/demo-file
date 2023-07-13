txt=input("Enter your text to write in file->")
a=open("15mintask.txt","w")
a.write(txt)
a.close()
import smtplib

sender_email = "pragu.kaya@gmail.com"
password = "tfajoiyvvrmnbajq"
to_email = "veera4012@gmail.com"
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_email, password)
print("login successful")
server.sendmail(sender_email,to_email,txt)
print("email sent to ",to_email)
server.quit()