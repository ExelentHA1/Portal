from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def Login():
    return render_template('login.html')

@auth.route('/logout')
def Logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def SignUp():
    if request.method == "POST":
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        pass1 = request.form.get('password')
        pass2 = request.form.get('confirm_password')
        # print(request.form)
    return render_template('sign_up.html')