package javamail;

import java.util.Calendar;
import java.util.Properties;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.PasswordAuthentication;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;


public class JavaMail {
    
    public String emailOrigen = "";
    public String contrasena="";
    
    public String emailDestino="";
    
    
    public void SendMail() {
        Properties props = new Properties();
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.host", "smtp.gmail.com");
        props.put("mail.smtp.ssl.trust", "smtp.gmail.com");
        props.put("mail.smtp.port", "587");

        Session session = Session.getInstance(props,
                new javax.mail.Authenticator() {
                    @Override
                    protected PasswordAuthentication getPasswordAuthentication() {
                        return new PasswordAuthentication(emailOrigen, contrasena);
                    }
                });

        try {

            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(emailOrigen));
            message.setRecipients(Message.RecipientType.TO,
                    InternetAddress.parse(emailDestino));
            message.setSubject("Recordatorio de pago");
            message.setText("Le recuerdo que debe de pagar su mensualidad.");

            Transport.send(message);
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        
        JavaMail jm = new JavaMail();
        Calendar fecha = Calendar.getInstance();
        
        
        boolean pagado=false;
        //Hacemos un sleep simulando la espera.
        System.out.println("Esperamos.");
        Thread.sleep(15);
        //Otra forma de hacerlo sería enviar los dias 15 de cada mes. Comprobar todos los dias al principio del dia si es 15.
        /*int dia = fecha.get(Calendar.DAY_OF_MONTH);
        if(dia==15 && pagado==false){
            //ENVIAR MAIL
            jm.SendMail();
        }
        */
        
        if(pagado==false){
            //ENVIAR MAIL
            System.out.println("Enviamos mail de recordatorio");
            jm.SendMail();
        }
    }

}
