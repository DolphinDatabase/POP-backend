from email.message import EmailMessage
import os
import ssl
import smtplib


def send_email():
    email_password = os.environ.get("EMAIL_PASS")
    email_sender = "dolphin.dbfatec@gmail.com"
    # email_password = "text"
    email_receiver = "vivictoaraujo@gmail.com"

    subject = "Important Privacy Terms Update for POP Platform"
    body = """
    Dear POP user,

    We hope this message finds you well. At POP, we are committed to safeguarding your privacy and ensuring the security of your data. In line with our ongoing efforts to provide you with the best user experience, we have updated our Privacy Terms.

    These changes are designed to enhance transparency and further protect your personal information. We have outlined the key updates in a user-friendly and comprehensive manner, which you can review at [Link to Updated Privacy Terms].

    Your continued trust in us is invaluable, and we want to assure you that your data remains under the same rigorous safeguards you've come to expect from POP.

    Should you have any questions or concerns regarding these updates, please don't hesitate to reach out to our dedicated support team at [Support Email Address]. We are here to assist you.

    Thank you for being a part of the POP community. Your privacy matters to us, and we appreciate your continued support.

    Best regards,
    POP Platform Team.

    [Contact Information: dolphin.dbfatec@gmail.com]
    """

    em = EmailMessage()
    em["From"] = email_sender
    em["to"] = email_receiver
    em["Subject"] = subject

    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


if __name__ == "__main__":
    # Envia um email de teste.
    send_email()
