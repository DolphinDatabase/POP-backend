from email.message import EmailMessage
from threading import Thread
from typing import List

import configuration
import ssl
import smtplib
from model import Grupo, Servico, Usuario
from .termo_service import TermoService


class EmailService:
    def notify_group(self, grupo: Grupo):
        termo_antigo = TermoService.get_last_termo_by_grupo(grupo)
        if termo_antigo is None:
            return
        for condicao in termo_antigo.condicoes:
            if condicao.servico == Servico.ENVIO_EMAIL.value:
                usuarios = [aceite.usuario for aceite in condicao.aceites if aceite.aceite]
                Thread(target=self.notify_users, args=(usuarios,)).start()

    def notify_users(self, usuarios: List[Usuario]):
        for usuario in usuarios:
            self.send_email(usuario)

    @staticmethod
    def send_email(usuario: Usuario):
        email_sender = "hrszanini@gmail.com"

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
            smtp.login(email_sender, "rfqy xmln xhxx mukm")
            smtp.login(email_sender, "oyka gijf mgmx vvhp")
            smtp.sendmail(email_sender, usuario.email, em.as_string())
