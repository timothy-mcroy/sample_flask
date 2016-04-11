from flask import Flask, render_template, Response, request, jsonify

app = Flask(__name__)


class sample_model(object):
    def __init__(self):
        self.channel = 0
        self.name = ""

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    model = sample_model()
    model.channel = 3
    model.name = name
    return render_template('hello.html', model = model)

@app.route('/updatevals', methods= ['POST'])
def update_values():
    data = request.form
    print(data)
    return jsonify(**data)


if __name__ == '__main__':
    app.debug= True
    app.run()
