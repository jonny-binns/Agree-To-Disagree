from flask import Flask, render_template, request, redirect, url_for
import translationtxt as t
app = Flask(__name__)

@app.route('/', methods=['GET'])
def menu():
    return render_template('Menu.html')

@app.route('/answers/', methods=['POST', 'GET'])
def answers_mode(answer=None, prompt=None, proArgument=None, conArgument=None):
    if request.method == 'POST':
        #print(request.form)
        answer = request.form['answer']
        replyTo = request.form.getlist('reply')
        #add to db
        t.addArgument(answer)
        return redirect(url_for('answers_mode'))
    else:
        #call method to read in from file
        arguments = t.getArguments()
        prompt = arguments[0]
        proArgument = arguments[1]
        conArgument = arguments[2]

        #set variables to correct values
        #prompt = "this is an example prompt"
        #proArgument = "this is an example argument in support of the prompt"
        #conArgument = "this is an example argument in opporsition of the prompt"
        return render_template('ArgumentMode.html', prompt=prompt, proArgument=proArgument, conArgument=conArgument)

@app.route('/pureTest/', methods=['GET'])
def pure_test():
    prompt = "this is an example prompt"
    proArgument = "this is an example argument in support of the prompt"
    conArgument = "this is an example argument in opporsition of the prompt"
    return render_template('ArgumentModePureTest.html', prompt=prompt, proArgument=proArgument, conArgument=conArgument)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)