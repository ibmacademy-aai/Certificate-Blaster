import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import time

# Fungsi untuk mengirim email dengan HTML
def kirim_email_html(from_email, password, to_email, subject, html_message):
    # Setup MIME
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Menambahkan isi pesan HTML
    msg.attach(MIMEText(html_message, 'html'))

    try:
        # Menghubungkan ke SMTP server Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print(f"Email berhasil dikirim ke {to_email}")
    except Exception as e:
        print(f"Gagal mengirim email ke {to_email}. Error: {str(e)}")

# Pengaturan akun email pengirim
email_pengirim = ""  # Ganti dengan email pengirim
password_pengirim = "" 

# Membaca CSV yang berisi nama, email, email institusi, dan password
with open('single.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        name = row['name']
        email = row['email']  # Email pribadi
        link_sertif_si = row['link_sertif_si']
        link_sertif_intern = row['link_sertif_intern']
        personal_mentor = row['personal_mentor']
        html_message = f"""
     <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <title>Sertifikat Akhir</title>
</head>

<body style="font-family: 'Poppins', Arial, sans-serif;">
    <div style="display: flex; justify-content: center; flex-direction: column; align-items: center; margin: 10px;">
        <div
            style="background-color: beige; width: 95%; border: 2px solid purple; padding: 1em; margin: 1em 5em 1em 5em; border-radius: 7px;">
            <span>
                <h1 style="text-align: center;">Infinite Learning</h1>
                <h3 style="text-align: center;">IBM Academy - Advance AI</h3>
                <br>
                <b>Hi {name}! 👋</b>
                <br>
                <b>Selamat!</b> Kamu telah menyelesaikan perjalananmu di Studi Independen IBM Academy - Advance AI Batch
                7 dengan sukses.
                Terima kasih banyak atas dedikasi dan kontribusi luar biasa yang telah kamu berikan selama 4 bulan ini.
                Kami bangga memilikimu sebagai bagian dari keluarga Infinite Learning!
                <br>
                <br>
                Silahkan download <b>sertifikat studi independen</b> kamu di link berikut :

            </span>
            <div style="margin: 12px 0px 12px 0px; text-align: center; display: flex; justify-content: center;">
                <a href="{link_sertif_si}" style="background-color: aquamarine; text-decoration: none; color: inherit; display: flex;
                border: 1px solid black;
                border-radius: 4px;
                overflow: hidden;
                cursor: pointer;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                transition: all 0.3s ease; padding: 7px;">
                    Sertifikat Studi Independen
                </a>
            </div>
            <div>
                Seperti yang sudah kami janjikan bahwa kami akan memberikan <b>sertifikat internship</b> bagi peserta
                studi independen karena telah melewati beberapa project dengan luar biasa, silakan download melalui link
                berikut:
                <div style="margin: 12px 0px 12px 0px; text-align: center; display: flex; justify-content: center;">
                    <a href="{link_sertif_intern}" style="background-color: aquamarine; text-decoration: none; color: inherit; display: flex;
                    border: 1px solid black;
                    border-radius: 4px;
                    overflow: hidden;
                    cursor: pointer;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    transition: all 0.3s ease; padding: 7px;">
                        Sertifikat Internship
                    </a>
                </div>
                Ini bukan hanya sebuah sertifikat, tetapi juga bukti akan kerja keras dan semangatmu yang luar biasa. Tetaplah bersemangat, dan jangan pernah berhenti bermimpi.
                <br>
                <p align="center" style="background-color: aquamarine; padding: 7px; text-align: center; border-radius: 7px;">"Education is the most powerful weapon which you can use to change the world."
                    -Nelson Mandela</p>
                <p align="center" style="background-color: aquamarine; padding: 7px; text-align: center; border-radius: 7px;">"Investasi terbaik yang bisa kamu lakukan adalah investasi pada dirimu sendiri."
                    ― Warren Buffett</p>
                <br>
                Selamat merayakan kesuksesanmu! Kami bangga menjadi bagian dari perjalananmu.
                <br>
                Selamat sukses dan sampai berjumpa lagi!
                <br>
                <br>
                Salam hangat!
                <br>
                Personal Mentor kamu di IBM Academy - Advance AI <br> 
                <br>
                {personal_mentor}
                <br>
                Infinite Learning
            </div>
        </div>
    </div>
</body>

</html>
        """
        
        # Subjek email
        subject = f"Sertifikat Studi Independen - {name}"
        
        # Kirim email ke masing-masing murid (email pribadi)
        kirim_email_html(email_pengirim, password_pengirim, email, subject, html_message)
        time.sleep(2)  # Jeda antar email

print("Semua email telah dikirim")