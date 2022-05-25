import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Keep it on the hush."

@app.route('/')
def index():
    if 'random_number' not in session:
        print('Generating random number')
        session['random_number'] = random.randint(1,100)
        session['attempts']=0
    else:
        print('Random number already exists')
    return render_template('index.html')

@app.route('/outcome', methods=['POST'])
def evaluate_predictions():
    print('Got outcome')
    print(request.form)
    if request.form['guess']:
        session['attempts'] = session['attempts'] + 1
        session['guess']=int(request.form['guess'])
        session['outcome_color']="--bs-red"
        if session['guess']>session['random_number']:
            print("too high")
            session['outcome_text']="Too high!"
        elif session['guess']<session['random_number']:
            print("too low")
            session['outcome_text']="Too low!"
        else:
            print("CORRECT!")
            session['correct_answer']=True
            session['outcome_text']=f"You guessed it! The number was {session['random_number']}."
            session['outcome_color']="--bs-green"
    return redirect('/')

@app.route('/playagain', methods=['POST'])
def reset_game():
    print('Resetting game')
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
    # app.run(debug=True) For non-Mac users