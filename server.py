from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['GET'])
def menu():
    return render_template('Menu.html')

@app.route('/answers/', methods=['POST', 'GET'])
def answers_mode(answer=None, prompt=None, proArgument=None, conArgument=None):
    if request.method == 'POST':
        print(request.form)
        answer = request.form['answer']
        #add answer to the databse
        return redirect(url_for('answers_mode'))
    else:
        prompt = "this is an example prompt"
        proArgument = "this is an example argument in support of the prompt"
        conArgument = "this is an example argument in opporsition of the prompt"
        return render_template('ArgumentMode.html', prompt=prompt, proArgument=proArgument, conArgument=conArgument)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)