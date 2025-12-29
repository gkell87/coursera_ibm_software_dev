from Maths.mathematics import sum, diff, mult
from flask import Flask, render_template, request

app = Flask('Mathematics Problem Solver')

@app.route('/sum')
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = sum(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route('/sub')
def diff_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = diff(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route('/mul')
def mult_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = mult(num1, num2)
    if result.is_integer():
        result = int(result)
    return str(result)

@app.route('/')
def render_index_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)