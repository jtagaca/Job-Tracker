import smtplib
import ssl


def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "jtagaca11@gmail.com"
    receiver_email = "jtagaca11@gmail.com"
    password = "Qwerty002!"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message)
            print('email sent!')
        except:
            print("could not login or send the mail.")
