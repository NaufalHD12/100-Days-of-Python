import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email Configuration
EMAIL_SENDER = "hadinaufal06@gmail.com"
EMAIL_PASSWORD = "wagt rwwt hsqf jjrr"  # Gunakan App Password jika pakai Gmail
EMAIL_RECEIVER = "naufalhd4@gmail.com"
SMTP_SERVER = "smtp.gmail.com"  # Bisa diubah sesuai provider
SMTP_PORT = 587

# Konstanta
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# API Keys (Sebaiknya gunakan environment variable)
stock_api = "8N3XLAI1BUNL0L4I"
news_api = "4780397ae55141219670eed624913ef6"

# Ambil data saham
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api,
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

# Cek validitas data
if "Time Series (Daily)" not in stock_data:
    print("Error: Data saham tidak ditemukan.")
    exit()

# Ambil harga penutupan
daily_data = stock_data["Time Series (Daily)"]
dates = list(daily_data.keys())
if len(dates) < 2:
    print("Error: Tidak cukup data untuk analisis.")
    exit()

yesterday = dates[0]
day_before_yesterday = dates[1]
closing_price_yesterday = float(daily_data[yesterday]["4. close"])
closing_price_before = float(daily_data[day_before_yesterday]["4. close"])

# Hitung perubahan harga saham
price_diff = closing_price_yesterday - closing_price_before
percentage_change = (abs(price_diff) / closing_price_yesterday) * 100
direction = "🟢" if price_diff > 0 else "🔴"

if percentage_change > 5:
    print(f"📉 {STOCK}: Perubahan harga {percentage_change:.2f}%")

    # Ambil berita
    news_params = {
        "q": COMPANY_NAME,
        "sortBy": "popularity",
        "apiKey": news_api,
        "language": "en",
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()

    if "articles" not in news_data or len(news_data["articles"]) == 0:
        print("Error: Tidak ada berita yang ditemukan.")
        exit()

    articles = news_data["articles"][:3]  # Ambil 3 berita pertama

    # Format email
    email_subject = f"{STOCK}: {direction}{percentage_change:.2f}%"
    email_body = ""

    for article in articles:
        headline = article["title"]
        brief = article["description"] or "No description available"
        link = article["url"]
        email_body += f"📰 **Headline:** {headline}\n📜 **Brief:** {brief}\n🔗 [Read more]({link})\n\n"

    # Kirim email
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = email_subject
    msg.attach(MIMEText(email_body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("📧 Email berhasil dikirim!")
    except Exception as e:
        print(f"❌ Gagal mengirim email: {e}")
