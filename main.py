from flask import Flask, redirect, request, render_template
app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/')
def index():    

    return render_template('form.html')

@app.route('/', methods=['POST'])
def validate():

    user_name = request.form['user-name-input']
    password = request.form['password-input']
    verify_password = request.form['verify-password-input']
    email = request.form['email-input']

    user_name_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if len(user_name) < 3 or len(user_name) > 20:
        user_name_error = 'Username must be between 3-20 characters.'
        
    if ' ' in user_name:
        user_name_error = 'Username cannot contain a space.'
        user_name = ''

    if len(password) < 3 or len(password) > 20:
        password_error = 'Password must be between 3-20 characters.'
        password = ''

    if ' ' in password:
        password_error = 'Password cannot contain a space.'
        password = ''
        verify_password = ''
    
    if verify_password != password:
        verify_password_error = 'Password does not match.'
        verify_password = ''

    if len(email) == 0: 
        email_error = ''

    elif len(email) < 3 or len(email) > 20:
        email_error = 'Your email must be between 3-20 characters.'

    elif '@' not in email or '.' not in email:
        email_error = 'This is not a valid email format.'

    if not user_name_error and not password_error and not verify_password_error and not email_error:
        
        return redirect('/validated-user?user_name={0}'.format(user_name))

    else:
        return render_template('form.html', user_name=user_name, user_name_error=user_name_error, password=password, password_error=password_error, verify_password=verify_password, verify_password_error=verify_password_error, email=email, email_error=email_error)

@app.route('/validated-user')
def validated():
    user_name = request.args.get('user_name')

    return render_template('validated-user.html', user_name=user_name)


app.run()
