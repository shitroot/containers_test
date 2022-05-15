from flask import Flask, jsonify
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')

mysql = MySQL()
mysql.init_app(app)

user = {
    'name': 'Duvan Bedoya',
    'role': 'Software Engineer'
}


@app.route('/users/me')
def get_current_user():
    return jsonify(user)


@app.route('/healthcheck')
def health_check():
    return 'healthy', 200


@app.route('/dbinfo')
def db_info():
    cursor = mysql.connect().cursor()
    cursor.execute('select localtimestamp(), version()')
    info = cursor.fetchone()
    local_date, version = info
    return jsonify({
        "db": "mysql",
        "version": version,
        "localdate": str(local_date)
    })


if __name__ == "__main__":
    app.run(debug=True)
