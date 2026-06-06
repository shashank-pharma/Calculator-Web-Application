from flask import Flask,request,render_template,jsonify
app = Flask(__name__)

#route 1 jo templates ka formate return krega.
@app.route('/')
def home_page():
    return render_template('index.html')

#route 2 abh ham check krenhe ki konsa operation hai. 
@app.route('/math',methods =['POST'])
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            r = num1 + num2
            result = "The sum of " + str(num1) + " " + 'and ' + str(num2) + " " + "is " + str(r)
        elif(ops == 'subtract'):
            r = num1 - num2
            result = "The sum of " + str(num1) +  " " + 'and ' + str(num2) + " " +"is " + str(r)
        elif(ops == 'multiply'):
            r = num1 * num2
            result = "The sum of " + str(num1) + " " +'and ' + str(num2) + " " +"is " + str(r)
        elif(ops == 'divide'):
            r = num1 / num2
            result = "The sum of " + str(num1) + " " +'and ' + str(num2) + " " +"is " + str(r)
       
        return render_template('results.html',result=result)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)