from flask import request, redirect, url_for, session

def authenticate_handler(response):
    if request.endpoint in 'static':
        return response
    
    if request.endpoint not in ('login', 'logout') and 'user_name' not in session:
        return redirect(url_for('login', next=request.url))

    return response

