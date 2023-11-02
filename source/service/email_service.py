from email.message import EmailMessage
import configuration
import ssl
import smtplib
from model import Grupo, Servico, Usuario
from .usuario_service import UsuarioService
from .termo_service import TermoService


class EmailService:
    def notify_group(self, grupo: Grupo):
        for usuario in UsuarioService.get_usuario_by_grupo():
            termo_aceite = TermoService.get_last_termo_aceite(usuario)
            for condicao in termo_aceite.condicoes:
                if condicao.servico == Servico.ENVIO_EMAIL.value:
                    self.send_email(usuario)
                    break

    def send_email(self, usuario: Usuario):
        email_sender = "dolphin.dbfatec@gmail.com"

        subject = "Important Privacy Terms Update for POP Platform"
        body = f"""
        Dear {usuario.nome},

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
        em["to"] = usuario.email
        em["Subject"] = subject

        em.set_content(body)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, configuration.EMAIL_PASSWORD)
            smtp.sendmail(email_sender, usuario.email, em.as_string())
