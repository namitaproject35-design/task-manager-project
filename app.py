from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "taskmanager123"


# DATABASE SETUP
def init_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # Users Table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Tasks Table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            due_date TEXT NOT NULL,
            priority TEXT DEFAULT 'Medium',
            status TEXT DEFAULT 'Pending'
        )
    ''')

    conn.commit()
    conn.close()


init_db()


# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        try:
            cur.execute(
                "INSERT INTO users(username,password) VALUES (?,?)",
                (username, password)
            )
            conn.commit()

        except:
            conn.close()
            return "Username already exists!"

        conn.close()

        return redirect('/login')

    return render_template('register.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cur.fetchone()

        conn.close()

        if user:
            session['user'] = username
            return redirect('/')

        return "Invalid Username or Password"

    return render_template('login.html')


# LOGOUT
@app.route('/logout')
def logout():

    session.pop('user', None)
    return redirect('/login')


# HOME
@app.route('/')
def home():

    if 'user' not in session:
        return redirect('/login')

    search = request.args.get('search', '')

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    if search:
        cur.execute(
            "SELECT * FROM tasks WHERE task_name LIKE ?",
            ('%' + search + '%',)
        )
    else:
        cur.execute("SELECT * FROM tasks")

    tasks = cur.fetchall()

    conn.close()

    return render_template(
        'index.html',
        tasks=tasks,
        username=session['user'],
        search=search
    )


# ADD TASK
@app.route('/add', methods=['POST'])
def add_task():

    if 'user' not in session:
        return redirect('/login')

    task_name = request.form['task_name']
    due_date = request.form['due_date']
    priority = request.form['priority']

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute(
        '''
        INSERT INTO tasks(task_name,due_date,priority,status)
        VALUES (?,?,?,?)
        ''',
        (task_name, due_date, priority, "Pending")
    )

    conn.commit()
    conn.close()

    return redirect('/')


# UPDATE STATUS
@app.route('/update_status/<int:id>')
def update_status(id):

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute(
        "SELECT status FROM tasks WHERE id=?",
        (id,)
    )

    current_status = cur.fetchone()[0]

    if current_status == "Pending":
        new_status = "In Progress"

    elif current_status == "In Progress":
        new_status = "Completed"

    else:
        new_status = "Pending"

    cur.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        (new_status, id)
    )

    conn.commit()
    conn.close()

    return redirect('/')


# DELETE TASK
@app.route('/delete/<int:id>')
def delete_task(id):

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM tasks WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)