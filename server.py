from flask import Flask, render_template, request, redirect, url_for
import translationtxt as t
app = Flask(__name__)

#route for the manu/home page
@app.route('/', methods=['GET'])
def menu():
    return render_template('Menu.html')


#route for answers mode
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
    

#route for questions mode
@app.route('/questions/', methods=['POST', 'GET'])
def questions_mode():
    if request.method == 'POST':
        #add prompt to db
        print("you did a post request")
    else:
        #call method to read in from file
        arguments = t.getArguments()
        prompt = arguments[0]
        proArgument = arguments[1]
        conArgument = arguments[2]

        return render_template('QuestionsMode.html', prompt=prompt)


#route for voting mode
@app.route('/vote/', methods=['POST', 'GET'])
def voting_mode():
    if request.method == 'POST':
        #add prompt to db
        print("you did a post request")
    else:
        arguments = t.getArguments()
        prompt = arguments[0]
        proArgument = arguments[1]
        conArgument = arguments[2]

        return render_template('VotingMode.html', prompt=prompt, proArgument=proArgument, conArgument=conArgument)


#route for about page
@app.route('/about/', methods=['GET'])
def about():
    return render_template('About.html')

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)