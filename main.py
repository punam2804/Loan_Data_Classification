
from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import Loan
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to API")
    # return 'Success'
    return render_template("index.html")


@app.route('/predict_charges')
def get_loan():

    if request.method == "GET":
        print("We are using GET Method")
        
        data = request.form
        print("data :",data)
    

        credit_policy = eval(request.args.get("credit_policy"))
        int_rate = eval(request.args.get("int_rate"))
        installment = eval(request.args.get("installment"))
        log_annual_inc = eval(request.args.get("log_annual_inc"))
        dti = eval(request.args.get("dti"))
        fico = eval(request.args.get("fico"))
        days_with_cr_line = eval(request.args.get("days_with_cr_line"))
        revol_bal = eval(request.args.get("revol_bal"))
        revol_util = eval(request.args.get("revol_util"))
        inq_last_6mths = eval(request.args.get("inq_last_6mths"))
        delinq_2yrs = eval(request.args.get("delinq_2yrs"))
        pub_rec = eval(request.args.get("pub_rec"))
        purpose = (request.args.get("purpose"))

        print("credit_policy, int_rate, installment, log_annual_inc, dti, fico, days_with_cr_line, revol_bal, revol_util, inq_last_6mths, delinq_2yrs, pub_rec, purpose\n",
              credit_policy, int_rate, installment, log_annual_inc, dti, fico, days_with_cr_line, revol_bal, revol_util, inq_last_6mths, delinq_2yrs, pub_rec, purpose)

        loa = Loan(credit_policy, int_rate, installment, log_annual_inc, dti, fico, days_with_cr_line, revol_bal, revol_util, inq_last_6mths, delinq_2yrs, pub_rec, purpose)
        charges = loa.get_predicted()
        if charges == 1:
            return render_template("index.html", prediction = 'Person is going to Pay Loan')
        else:
            return render_template("index.html", prediction = 'Person is not going to Pay Loan')
        # return jsonify({"Result" : f"Predicted is {charges}"})

    else:
        print("We are using POST Method")

        credit_policy = (request.args.get("credit_policy"))
        int_rate = (request.args.get("int_rate"))
        installment = (request.args.get("installment"))
        log_annual_inc = (request.args.get("log_annual_inc"))
        dti = (request.args.get("dti"))
        fico = (request.args.get("fico"))
        days_with_cr_line = (request.args.get("days_with_cr_line"))
        revol_bal = (request.args.get("revol_bal"))
        revol_util = (request.args.get("revol_util"))
        inq_last_6mths = (request.args.get("inq_last_6mths"))
        delinq_2yrs = (request.args.get("delinq_2yrs"))
        pub_rec = (request.args.get("pub_rec"))
        purpose = (request.args.get("purpose"))

        print("credit_policy, int_rate, installment, log_annual_inc, dti, fico, days_with_cr_line, revol_bal, revol_util, inq_last_6mths, delinq_2yrs, pub_rec, purpose\n",
              credit_policy, int_rate, installment, log_annual_inc, dti, fico, days_with_cr_line, revol_bal, revol_util, inq_last_6mths, delinq_2yrs, pub_rec, purpose)

        loa = Loan(credit_policy, int_rate, installment, log_annual_inc, dti, fico, days_with_cr_line, revol_bal, revol_util, inq_last_6mths, delinq_2yrs, pub_rec, purpose)
        charges = loa.get_predicted()
        if charges == 1:
            return render_template("index.html", prediction = 'Person is going to Pay Loan')
        else:
            return render_template("index.html", prediction = 'Person is not going to Pay Loan')

        # return render_template("index.html", prediction = charges)
        # return jsonify({"Result" : f"Predicted is {charges}"})


if __name__ == "__main__":
    app.run(host='0.0.0.0' , port= config.PORT_NUMBER, debug=True)