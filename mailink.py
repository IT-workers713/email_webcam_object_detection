import smtplib
import mimetypes
from email.message import EmailMessage

password="reuadxmuwmkqgcon"
SENDER="sender email adreesse"
RECIPIENT="receiver email adresse"
def send_email(image_path):
    email_mesg= EmailMessage()
    email_mesg["Subject"] = "Nouveau Client Rentre"
    email_mesg.set_content("Bonjour , Nous avons vu un nouveau client")

    with open(image_path,"rb") as file:
        content = file.read()
    maintype, subtype = mimetypes.guess_type(image_path)[0].split('/')
    email_mesg.add_attachment(content, maintype=maintype, subtype=subtype)

    gmail = smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,password)
    gmail.sendmail(SENDER,RECIPIENT,email_mesg.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path="images/19.png")
