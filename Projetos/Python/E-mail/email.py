from email.message import EmailMessage
import ssl
import smtplib

meu_email = ""             # Inserir o seu e-mail
senha_gerada = ""          # Colocar a senha do e-mail
destinatario_email = ""    # E-mail do destinatário
assunto = ""               # Assunto do e-mail
body = ""                  # Mensagem do E-mail

em = EmailMessage()

em['From'] = meu_email
em['To'] = destinatario_email
em['subject'] = assunto
em .set_content(body)

context = ssl.create_default_context() #criando um contexto SSl seguro

# SMTP é o protocolo que permite enviar emails pela internet.
# fazendo conexão com o servidor SMTP do Gmail usando SSL (tecnologia de segurança)
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(meu_email, senha_gerada) #fazendo o seu login
    smtp.sendmail(meu_email, destinatario_email, em.as_string()) #enviando