## flask_app/app.py

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Required for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name', '')
        age_str = request.form.get('age', '')
        
        # Error handling
        if not name:
            flash('Please enter your name')
            return render_template('form.html')
        
        try:
            age = int(age_str)
            if age <= 0:
                flash('Age must be a positive number')
                return render_template('form.html')
        except ValueError:
            flash('Please enter a valid age')
            return render_template('form.html')
        
        greeting = f"Hello, {name}! You are {age} years old."
        return render_template('form.html', greeting=greeting)
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)