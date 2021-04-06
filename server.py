from flask import Flask, render_template, request, redirect, url_for, send_file
import translation as t
import fileManager as fm
import sadface as sf
import json

app = Flask(__name__)

#route for the menu/home page
@app.route('/', methods=['GET'])
def menu():
    return render_template('Menu.html')


#route for answers mode
@app.route('/answers/', methods=['POST', 'GET'])
def answers_mode(answer=None, prompt=None, proArgument=None, conArgument=None):
    if request.method == 'POST':
        #get prompt
        prompt = request.form[str('formPrompt')]
        prompt = prompt.strip()
        #get newArgument
        newArgument = request.form[str('newArgument')]
        #get what text newArgument is replying to
        parent = request.form[str('formParent')]
        parent = parent.strip()
        #get whether newArgument is agreeing or disagreeing
        stance = request.form[str('stance')]

        #add newArgument to db
        argArr = [prompt, newArgument, parent, stance]
        t.addArgument(argArr)

        return redirect(url_for('answers_mode'))
    else:
        #get random debate from file
        sfStr = fm.getRandomFile()
        
        #get all data from debate
        argData = t.getData(sfStr)

        #serialize to string, using # as the delimiter
        argDataStr = ""
        for i in range(len(argData)):
            for j in range(0,3):
                argDataStr = argDataStr + argData[i][j] + "#"

        return render_template('ArgumentMode.html', argDataStr=argDataStr)
    

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
#is not implemented, data is set in order for the ui to be developed
@app.route('/vote/', methods=['POST', 'GET'])
def voting_mode():
    if request.method == 'POST':
        #add prompt to db
        print("you did a post request")
    else:
        prompt = "this is an example prompt"
        proArgument = "this is an example argument in support of the prompt"
        conArgument = "this is an example argument in opposition of the prompt"
        return render_template('VotingMode.html', prompt=prompt, proArgument=proArgument, conArgument=conArgument)


#route for about page
@app.route('/about/', methods=['GET'])
def about():
    return render_template('About.html')


#route for downloading the dataset
@app.route('/download/')
def download_file():
    #zip directory
    return send_file(path, as_attachment=True)
    #delete .zip after returning

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)