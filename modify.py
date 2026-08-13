from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Server Live & Running"}

@app.get("/csm")
def get_data_base(target: str):
    conn = sqlite3.connect('kalyan_classrooms.db')
    cursor = conn.cursor()

    # 1. First run SQL file script to create table & insert data
    try:
        with open('kalyan_small_prototype.sql', 'r') as file:
            sql_script = file.read()
            cursor.executescript(sql_script)
            conn.commit()
    except Exception as e:
        print("SQL Execute Exception:", e)

    # 2. Query data
    try:
        cursor.execute("SELECT * FROM kalyan_first_projects1 WHERE roll_no = ?", (target,))
        data = cursor.fetchall()
        return {"data": data}
    except Exception as e:
        return {"error_detail": str(e)}
    finally:
        conn.close()