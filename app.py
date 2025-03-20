from flask import Flask, flash

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'hello world!'


@app.route("/")
def hello_name():
    return f'ola!'


@app.route("/<number1>+<number2>")
def soma(number1, number2):
    try:

        number1 = int(number1)
        number2 = int(number2)

        return f'A soma de {number1} + {number2} = {number1 + number2}'
    except ValueError:
        return 'Valores invalidos'


@app.route("/<number1>-<number2>")
def subtrair(number1, number2):
    try:

        number1 = int(number1)
        number2 = int(number2)
        resultado = number1 - number2
        return f'A subtração de {number1} - {number2} = {resultado}'
    except ValueError:
        return 'Valores invalios!'


@app.route("/<number1>*<number2>")
def multiplicacao(number1, number2):
    try:

        num1 = int(number1)
        num2 = int(number2)
        resultado = num1 * num2
        return f'A multiplicação de {number1} * {number2} = {resultado}'
    except ValueError:
        return 'Dado inserido é invalido, favor inserir valores númericos'


@app.route("/<number1>/<number2>")
def somar(number1, number2):
    try:

        divisao = (int(number1) / int(number2))
        return str(divisao)
    except ValueError:
        return 'Numero invalido'


@app.route("/<number1>")
def parOuImpar(number1):
    try:
        if int(number1) % 2 == 0:
            return f'O numero {number1} é par'
        else:
            return f'O numero {number1} é impar'
    except ValueError:
        return 'Valores invalios'

if __name__ == "__main__":
    app.run(debug=True)
