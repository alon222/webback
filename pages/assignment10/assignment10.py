from flask import Flask , redirect, url_for,render_template
from flask import request,session,Blueprint
from interact_with_DB import *

# about blueprint definition
assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')



@assignment10.route("/assignment10")
def index():
    query = 'select * from users;'
    users = interact_db(query=query,query_type='fetch')
    message=''
    if session.get('message'):
        message = session['message']
        session['message'] = ''
    return render_template('assignment10.html', users=users, mes=message)

@assignment10.route("/delete-user", methods=['POST'])
def delete_user():
    id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % id
    interact_db(query=query,query_type='commit')
    session['message'] = 'the user is deleted'
    return redirect('/assignment10')

@assignment10.route("/insert_user", methods=['POST'])
def handleinsert():
    name = request.form['username']
    nickname = request.form['nickname']
    email = request.form['email']
    password = request.form['password']
    query="INSERT INTO users(name,nickname,email,password) VALUES ('%s','%s','%s','%s');" % (name,nickname,email,password)
    interact_db(query=query,query_type='commit')
    session['message'] = 'A new user created in db'
    return redirect("/assignment10")

@assignment10.route("/update-user", methods=['POST'])
def update_user():
    id = request.form['id']
    query = "select * from users where id='%s';"%id
    user = interact_db(query=query,query_type='fetch')
    name = request.form['name']
    if name == '':
        name = user[0].name
    nickname = request.form['nickname']
    if nickname == '':
        nickname = user[0].nickname
    email = request.form['email']
    if email == '':
        email = user[0].email
    password = request.form['password']
    if password == '':
        password = user[0].password
    query = "UPDATE users SET name='%s',nickname='%s',email='%s',password='%s' WHERE id='%s';" % (name,nickname,email,password,id)
    interact_db(query=query,query_type='commit')
    session['message'] = 'the user has been updated'
    return redirect("/assignment10")
