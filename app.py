from flask import Flask, render_template, request, flash, redirect, session

app = Flask(__name__)
app.secret_key="verysupersecretkey"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('greeting.html', name=name)
    return render_template('form.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback = request.form['feedback']
        session['feedback'] = feedback
        # flash(f"Feedback submitted successfully: {feedback}", 'success')
        return redirect('/feedback_page')
    return render_template('feedback_form.html')

@app.route('/feedback_page')
def feedback_page():
    feedback = session.get('feedback', 'No feedback received')
    return render_template('feedback_page.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)