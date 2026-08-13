from fastapi import FastAPI
import sqlite3
app=FastAPI()
@app.get("/csm")
def get_data_base(target: str):
    conn=sqlite3.connect('kalyan_classrooms.db')
    cursor=conn.cursor()
    try:
        with open('kalyan_small_prototype.sql','r') as file:
            sql_script= file.read()
        cursor.executescript(sql_script)
        conn.commit()
    except Exception as e:
        pass

    cursor.execute("SELECT * FROM kalyan_first_projects1 WHERE roll_no = ?", (target,))
    data=cursor.fetchall()
    conn.close()
    return data

