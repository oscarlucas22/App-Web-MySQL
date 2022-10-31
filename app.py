from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL 

app = Flask(__name__)

# MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'flaskpeliculas'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM peliculas')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', peliculas=data)

@app.route('/add_pelicula', methods=['POST'])
def add_pelicula():
    if request.method == 'POST':
        NombrePelicula = request.form['NombrePelicula']
        Genero = request.form['Genero']
        Director = request.form['Director']
        AnoEstreno = request.form['AnoEstreno']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO peliculas (NombrePelicula, Genero, Director, AnoEstreno) VALUES (%s, %s, %s, %s)', (NombrePelicula, Genero, Director, AnoEstreno))
        mysql.connection.commit()
        flash('Contact Added successfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:NombrePelicula>')
def delete_pelicula(NombrePelicula):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM peliculas WHERE NombrePelicula = {0}'.format('NombrePelicula'))
    mysql.connection.commit()
    flash('Film Removed Successfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)