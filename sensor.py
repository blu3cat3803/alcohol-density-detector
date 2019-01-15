import serial
import sqlite3
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
conn = sqlite3.connect('/home/pi/Case/db.sqlite3')
c = conn.cursor()
c.execute("delete from chart_alcohol")
conn.commit()
conn.close()
i = 0
m = 0

while 1 :
    conn = sqlite3.connect('/home/pi/Case/db.sqlite3')
    c = conn.cursor()
    i = i + 1
    v_read = ser.readline()
    vol = v_read.split(':', 4)
    if i > 100:
       m = m + 1
       c.execute("delete from chart_alcohol WHERE t = {}".format(m))
       conn.commit()
    for x in range(5):
        v = map(float, vol)
    c.execute("INSERT INTO chart_alcohol(t, v1, v2, v3, v4, v5) VALUES ('{}','{}', '{}', '{}', '{}', '{}')".format(i, v[0], v[1], v[2], v[3], v[4]))
    conn.commit()
    conn.close()
    time.sleep(1)
