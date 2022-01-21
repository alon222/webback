from re import search
from flask import Flask , redirect, url_for,render_template
from flask import request,session,Blueprint,jsonify
import requests
import random
import json
app = Flask(__name__)
app.secret_key='123'
app.config['DEBUG'] = True
from interact_with_DB import *



from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

@app.route("/")
def home():
    return render_template('cv.html')

@app.route("/contact-me")
def contact():
    return render_template('cv1.html')


@app.route("/assignment8")
def assignment8():
    ishobbies=True
    hobbies=['swimming','running','tennies','sleeping']
    music=['pop','ישראלי','Country']
    return render_template('assignment8.html',user_name='David',ishobbies=ishobbies,hobbies=hobbies,music=music)

@app.route("/assignment9", methods=['GET','POST'])
def assignment9():
    users={
        'user1':
            {'name':'avi','email':'avilon@gmail.com','nickname':'av'},
        'user2':
            {'name':'adi','email':'adi@gmail.com','nickname':'ad'},
        'user3':
            {'name':'tom','email':'tom@gmail.com','nickname':'tomi'},
        'user4':
            {'name':'tami','email':'tami@gmail.com','nickname':'tamtam'},
        'user5':
            {'name':'alon','email':'alon@gmail.com','nickname':'alony'}
        }
    if request.method == 'GET':
        if 'search' in request.args:#no query parameters
            if request.args['search']=='':
                return render_template('assignment9.html', users=users)
            else:
                search_term = request.args['search']
                for k,v in users.items(): #loop in the users
                    for key,val in v.items(): #loop inside to find math in name or email or nickname
                        if val==search_term: #check if there is a match
                            users={'user1':v} #append the user data to show in template
                            return render_template('assignment9.html',users=users) #user found
                return render_template('assignment9.html',message='no users found') # no user found
        return render_template('assignment9.html')
    if request.method == 'POST':
        nickname=request.form['nickname']
        session['nickname'] = nickname
        return render_template('assignment9.html')

# python -m flask run

@app.route("/logout")
def log_out():
    session['nickname'] = ''
    return render_template('assignment9.html')

@app.route("/home-page")
@app.route("/home")
def home_page():
    return redirect(url_for('home'))

@app.route("/assignment11/users")
def user_api():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return jsonify(users)

@app.route("/assignment11/outer_source")
def fetch_ex():
    if request.args:
        id = request.args['reqid']
        res = requests.get(f'https://reqres.in/api/users/{id}')
        res = res.json()
        return render_template('assignment11.html', res=res)
    return render_template('assignment11.html')

# @app.route("/assignment11/request_backend")
# def handle_request():
#     id=request.args['reqid']
#     res=requests.get(f'https://reqres.in/api/users/{id}')
#     res=res.json()
#     return render_template('assignment11.html',res=res)

@app.route("/assignment12/restapi_users/", defaults={'user_id':10})
@app.route("/assignment12/restapi_users/<int:user_id>")
def user_api_ex12(user_id):
    query = 'select * from users where id=%s;' % user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users)==0:
        user_dict={
            'status':'failed',
            'message':'user not found in the database'
        }
    else:
        user_dict = {'id': users[0].id,
                     'name': users[0].name,
                     'nickname': users[0].nickname,
                     'email': users[0].email,
                     'create_date': users[0].create_date
                     }
    return jsonify(user_dict)


if __name__=='__main__':
    app.run(debug=True)