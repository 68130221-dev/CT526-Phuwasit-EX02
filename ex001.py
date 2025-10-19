from flask import Flask, jsonify,render_template

app = Flask(__name__)

@app.route('/sum/<para1>/<para2>')
def sum(para1, para2):
    try:
        int1 = int(para1)
        int2 = int(para2)
        result = int1 + int2
        return 'The Result of sum between'+(para1)+' and '+(para2)+' is ' + str(result)
    except ValueError:
        return 'You are using miss data type for operation.'
    
@app.route('/concat/<para1>/<para2>')
def concat(para1, para2):
    result = para1 + para2
    return 'The Result of concatanate between'+(para1)+' and '+(para2)+' is ' + str(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
