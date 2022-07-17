import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
  
app = Flask(__name__)
    
app.config['MYSQL_HOST'] = 'host'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'pet'
  
  
mysql = MySQL(app)

app.route('/api/pet/<name>', methods=['GET'])
def get_pet_by_name(name):
    try:
        conection = mysql.connect()
        cursor = conection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name, owner, species FROM pet WHERE name =%s", name)
        pet_result = cursor.fetchone()
        respone = jsonify(petresult)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 


app.run(host='localhost', port=5000)
