from flask import Flask, flash

app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'hello world!'

@app.route("/<name>")
def hello_name(name):
    return f'ola {name}!'



@app.route("/<number1>+<number2>")
def soma(number1,number2):
    return f'A soma de {number1} + {number2} = {number1+number2}'
@app.route("/<number1>-<number2>")
def subtrair(number1,number2):
    return f'A subtração de {number1} - {number2} = {number1-number2}'
@app.route("/<number1>*<number2>")
def multiplicacao(number1,number2):
    return f'A multiplicação de {number1} * {number2} = {number1*number2}'
@app.route("/ <number1>/<number2>")
def somar(number1,number2):
    try:
        divisao = (int(number1) + int(number2))
        return str(divisao)
    except ValueError:
        return 'erro'







if __name__ == "__main__":
    app.run(debug=True)
