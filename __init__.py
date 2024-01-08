from flask import Flask, render_template, url_for, request, redirect, session
import shelve
from Forms import *
import hashlib
from User import *
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'cbgKTH304'


def createStaff():
    db = shelve.open("users.db", "c")
    password = "staff1234"
    staff = Staff(1, "staff@ilovemeals.com", hashlib.sha256(password.encode()).hexdigest())

    if "Users" in db:
        if staff.get_user_id() not in db["Users"]:
            db["Users"][staff.get_email()] = staff
    else:
        users = {}
        users[staff.get_email()] = staff
        db["Users"] = users
    db.close()


def fetchUser(user_id=None):
    db = shelve.open("users.db", "c")
    if user_id is not None:
        for id, user in db["Users"].items():
            if id == user_id:
                response = user
                db.close()
                return response
    else:
        if 'email' in session:
            currentUser = {}
            for id, user in db["Users"].items():
                if session["email"] == user.get_email():
                    currentUser = user
            db.close()
            return currentUser

        

@app.route('/')
def home():
    createStaff()
    return render_template('home.html')



@app.route('/login', methods=['GET', 'POST'])
def login_user():
    user = fetchUser()
    if user:
        return redirect("/")
    login_user_form = UserLoginForm(request.form)
    if request.method == 'POST' and login_user_form.validate():
        db = shelve.open("users.db", "c")
        users = db["Users"]
        

        login_email = login_user_form.email.data
        login_password = login_user_form.password.data

        password_hash = hashlib.sha256(login_password.encode()).hexdigest()

        for user_id, user in users.items():
            if user.get_email() == login_email and user.get_password() == password_hash:
                now = datetime.now()
                session['logged_in'] = True
                session['email'] = login_email
                session['account_type'] = user.get_account_type()
                user.set_last_login(now)
                db['Users'] = users

                db.close()

                if session['account_type'] == 'Admin':
                    return redirect(url_for('staff_page'))
                else:
                    return redirect(url_for('customer_page'))
                
    return render_template('login.html', form=login_user_form)


@app.route('/customerPage', methods=['GET', 'POST'])
def customer_page():
    # if 'email' not in session:  # Check if user is logged in
    #     return redirect(url_for('login_user'))  # Redirect to login page if not
    user = fetchUser()    
    if not user: # if it's None / has no value??, then redirect to loginUser (can rename the login page to just login, same for reg)
        return redirect("/login")
    
    return render_template('customerPage.html', user=user)
    

@app.route('/logout', methods=['POST']) 
def logout():
    session["logged_in"] = False
    session.pop('email')
    session.pop('account_type')
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    user = fetchUser()
    if user:
        return redirect("/")
    register_customer_form = CustomerRegisterForm(request.form)
    if request.method == 'POST' and register_customer_form.validate():
        db = shelve.open("users.db", "c")
        users = db["Users"]
        count = len(users)
        id = count + 1

        first_name = register_customer_form.firstname.data
        last_name = register_customer_form.lastname.data
        email = register_customer_form.email.data
        password = register_customer_form.password.data
        confirm_password = register_customer_form.confirm.data
        dob = register_customer_form.dob.data
        contactnumber = register_customer_form.contactnumber.data

        if password != confirm_password:
            return 'Error: Passwords do not match'

        password_hash = hashlib.sha256(password.encode()).hexdigest()

        for key in db["Users"].keys():
            if db["Users"][key].get_email() == email:
                return "Email already exists"
            
        user = Customer(id, first_name, last_name, email,
                        password_hash, dob, contactnumber)

        try:
            users[user.get_email()] = user
            db['Users'] = users

            session['logged_in'] = True
            session['email'] = email
            session['account_type'] = 'Customer'
        except:
            print('Error in retrieving Customers from user.db.')

        #TEST CODES
        print(user.get_email(), 'was stored in user.db successfully with customer_id ==', user.get_user_id())

        db.close()

        return redirect(url_for('customer_page'))

    return render_template('register.html', form=register_customer_form)


@app.route('/retrieveUsers')
def retrieve_users():
    db = shelve.open('users.db', 'r')
    users = db['Users']

    users_list = []
    for key in users:
        user = users.get(key)
        users_list.append(user)
    db.close()

    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)


if __name__ == '__main__':
    app.run(debug=True)
    # if there are errors, we can catch them immediately!

