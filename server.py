from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/answers/', methods=['POST', 'GET'])
def answers_mode(answer=None, prompt=None):
    if request.method == 'POST':
        print(request.form)
        answer = request.form['answer']
        #add answer to the databse
        return redirect(url_for('answers_mode'))
    else:
        prompt = "this is an example prompt"
        return render_template('ArgumentMode.html', debatePrompt=prompt)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)