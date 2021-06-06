# install package for CentOS7
yum install wget
yum install python3

Install MySQL on CentOS7's Process：
https://www.mysqltutorial.org/install-mysql-centos/


# Create database
mysql> CREATE DATABASE DB_FullStackTest;

# Create table
mysql> use DB_FullStackTest;
mysql> CREATE TABLE Table_FullStackTest 
    (ID INT AUTO_INCREMENT,
    Date VARCHAR(99) NULL,
    Time VARCHAR(99) NULL,
    usec VARCHAR(99) NULL,
    SourceIP VARCHAR(99) NULL,
    SourcePort VARCHAR(99) NULL,
    DestinationIP VARCHAR(99) NULL,
    DestinationPort VARCHAR(99) NULL,
    FQDN TEXT NULL,
    PRIMARY KEY(ID));

# Frameworks: Flask (Python)
[cmd] python3 app.py

dir:
.
├─ app.py
├─ static
│  ├─ css
│  │   └ style.css 
│  └─ figure
│       ├ Logo.png
│       └ Photo_Joy.jpg
└─ templates
     ├ home.html
     ├ login.html
     └ table.html

# Database: MySQL
Password: MySQL!@#2021Test

# More info
1. URL for login: 0.0.0.0:5432
2. Login name: joy@gmail.com
3. Login password: password