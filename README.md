# Ecommerce_Price_Tracker
I built the project using Python and Flask. I used Requests and BeautifulSoup for web scraping, SQLite for storing product and price data, and SMTP with Gmail App Passwords for sending email alerts. The application follows a modular structure with separate files for scraping, database handling, and notifications.

🧰 Technologies, Libraries & Concepts Used
🔹 Programming Language

Python

Core logic

Web scraping

Email automation

Database operations

🔹 Web Framework

Flask

Routing (@app.route)

Handling GET & POST requests

Connecting backend with HTML templates

Running local development server

🔹 Web Scraping

Requests

Fetching HTML content from product URLs

BeautifulSoup (bs4)

Parsing HTML pages

Extracting product price from DOM elements

Handling different page structures

🔹 Database

SQLite

Lightweight relational database

Storing:

Product URL

Current price

Target price

Price history

sqlite3 (Python module)

Database connection

Insert & fetch queries

🔹 Email Notification

smtplib

Connecting to Gmail SMTP server

email.mime.text (MIMEText)

Formatting email content

Gmail App Password

Secure authentication for sending emails

🔹 Frontend

HTML

User input form (URL, target price)

Display tracked products

CSS (optional)

Styling the UI

Jinja2

Dynamic data rendering in HTML templates

🔹 Automation & Logic

Conditional Logic

Price comparison (current_price <= target_price)

Modular Programming

Separate files:

scraper.py

database.py

alert.py

app.py

Exception Handling

Preventing crashes during scraping or email failures

🔹 Development Tools

Virtual Environment (venv)

Isolated dependency management

pip

Installing project dependencies
