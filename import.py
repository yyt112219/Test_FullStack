import mysql.connector
import pandas as pd
import datetime

# Connect MySQL
maxdb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQL!@#2021Test",
)
cursor = maxdb.cursor()

# Read csv into pandas dataframe
df = pd.read_csv("./dns_sample.csv", error_bad_lines=False)

# Split time to Date, Time, usec
df["time"] = pd.to_datetime(df["frame.time_epoch"])
df["Date"] = df["time"].apply(lambda x: x.strftime("%Y-%m-%d"))
df["Time"] = df["time"].apply(lambda y: y.strftime("%H:%M:%S"))
df["usec"] = df["time"].apply(lambda z: z.strftime("%f"))
df = df.fillna("")
# Use database = "DB_FullStackTest"
cursor.execute("use DB_FullStackTest")
# Insert values from dataframe into MySQL DB
table = "Table_FullStackTest"
records = []
# Combine needed records
for row in range(len(df)):
    row_values = (
        df["Date"][row], df["Time"][row], df["usec"][row],
        df["ip.src"][row], df["udp.srcport"][row], df["ip.dst"][row],
        df["udp.dstport"][row], df["dns.qry.name"][row]
    )
    records.append(row_values)
# Insert multiple records
sql_cmd = f"""INSERT INTO {table}
    (Date, Time, usec, SourceIP, SourcePort, DestinationIP, DestinationPort, FQDN)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
cursor.executemany(sql_cmd,records)
maxdb.commit()
