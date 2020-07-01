import mysql.connector
from _ast import In
from enum import IntFlag

def create_conn():
    return mysql.connector.connect(host='localhost',username='root',password='',database='marmik')
def create_table():
    conn = create_conn()
    cursor = conn.cursor()
    cursor.execute("create table python(rno int,sname varchar(30),email varchar(30))")
    conn.commit()
    conn.close()

def insert_data(rno,sname,email):
    conn = create_conn()
    cursor = conn.cursor()
    args=(rno,sname,email)
    query = 'insert into python(rno,sname,email) values(%s,%s,%s)'
    cursor.execute(query,args)
    conn.commit()
    conn.close()
    print("data inserted sucessfully.....")
    
    
roll_number= int(input('Enter roll number: '))
name = input('Enter name: ')
email_id = input('enter email: ')
insert_data(roll_number,name,email_id)