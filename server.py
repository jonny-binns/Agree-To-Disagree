from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/answers/', methods=['POST', 'GET'])
def answers_mode(name=None):
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        return render_template('hello.html')
    else:
        return render_template('hello.html')
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)