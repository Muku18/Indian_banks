from flask import Flask, jsonify
from db import mysql

app = Flask(__name__)

@app.route('/banks')
def get_banks():
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, name FROM banks')
    banks = cur.fetchall()
    cur.close()
    return jsonify({'banks': banks})

@app.route('/banks/<int:bank_id>/branches/<int:branch_id>')
def get_branch(bank_id, branch_id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT id, name, address, hours, phone FROM branches WHERE bank_id = %s AND id = %s', (bank_id, branch_id))
    branch = cur.fetchone()
    cur.close()
    return jsonify(branch)

if __name__ == '__main__':
    app.run()