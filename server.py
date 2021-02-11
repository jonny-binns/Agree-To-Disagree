from flask import Flask, render_template, request, redirect, url_for
import translation as t
import fileManager as fm
import sadface as sf
import json

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
        #answer = request.form['answer']
        #replyTo = request.form.getlist('reply')
        #add to db
        #t.addArgument(answer)

        #get prompt
        prompt = request.form['prompt']
        #get newArgument
        newArgument = request.form['newArgument']
        #get what text newArgument is replying to
        parent = request.form['parent']
        #get whether newArgument is agreeing or disagreeing
        stance = request.form['stance']

        #add newArgument to db
        argArr = [prompt, newArgument, parent, stance]
        t.addArgument(argArr)

        return redirect(url_for('answers_mode'))
    else:
        #set variables to correct values
        #prompt = "this is an example prompt"
        #proArgument = "this is an example argument in support of the prompt"
        #conArgument = "this is an example argument in opposition of the prompt"
        
        #read from random file
        sfStr = fm.getRandomFile()

        #get prompt then two random, yet paired arguments
        prompt = t.getPrompt(sfStr)
        
        arguments = t.getArguments(sfStr)

        proArgument = arguments[0]
        conArgument = arguments[1]

        #display arguments/render template
        return render_template('ArgumentMode.html', prompt=prompt, proArgument=proArgument, conArgument=conArgument)
    

#route for questions mode
@app.route('/questions/', methods=['POST', 'GET'])
def questions_mode():
    if request.method == 'POST':
        #add prompt to db
        prompt = request.form['prompt']
        t.addPrompt(prompt)
        return redirect(url_for('questions_mode'))
    else:
        #get random prompt to be displayed
        sfStr = fm.getRandomFile()
        prompt = t.getPrompt(sfStr)
        return render_template('QuestionsMode.html', examplePrompt=prompt)


#route for voting mode
@app.route('/vote/', methods=['POST', 'GET'])
def voting_mode():
    if request.method == 'POST':
        #add prompt to db
        print("you did a post request")
    else:
        #arguments = t.getArguments()
        #prompt = arguments[0]
        #proArgument = arguments[1]
        #conArgument = arguments[2]
        prompt = "this is an example prompt"
        proArgument = "this is an example argument in support of the prompt"
        conArgument = "this is an example argument in opposition of the prompt"
        return render_template('VotingMode.html', prompt=prompt, proArgument=proArgument, conArgument=conArgument)


#route for about page
@app.route('/about/', methods=['GET'])
def about():
    return render_template('About.html')

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)