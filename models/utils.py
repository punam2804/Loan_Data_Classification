
import pickle
import json
import pandas as pd
import numpy as np
import config


class Loan():
    def __init__(self, credit_policy, int_rate, installment, log_annual_inc, dti, fico, days_with_cr_line, revol_bal, revol_util, inq_last_6mths, delinq_2yrs, pub_rec, purpose):
        
        self.credit_policy = credit_policy
        self.int_rate = int_rate
        self.installment = installment
        self.log_annual_inc = log_annual_inc
        self.dti = dti
        self.fico = fico
        self.days_with_cr_line = days_with_cr_line
        self.revol_bal = revol_bal
        self.revol_util = revol_util
        self.inq_last_6mths = inq_last_6mths
        self.delinq_2yrs = delinq_2yrs
        self.pub_rec = pub_rec
        self.purpose = "purpose_"+purpose
        

    def load_model(self):
        # with open(r'E:\Practies\Machine_Learning\Logistic\Loan_Data\models\Loanpkl.pkl', "rb") as f:
        with open (config.Pickle_file,"rb") as f:
            self.model = pickle.load(f)

        # with open(r'E:\Practies\Machine_Learning\Logistic\Loan_Data\models\json_data.json', "r") as f:
        with open (config.json_file,"rb") as f: 
            self.json_data = json.load(f)

    def get_predicted(self):

        self.load_model()  # Calling load_model method to get model and json_data

        
        array = np.zeros(len(self.json_data['column_name']))

        array[0] = self.credit_policy
        array[1] = self.int_rate
        array[2] = self.installment
        array[3] = self.log_annual_inc
        array[4] = self.dti
        array[5] = self.fico
        array[6] = self.days_with_cr_line
        array[7] = self.revol_bal
        array[8] = self.revol_util
        array[9] = self.inq_last_6mths
        array[10] = self.delinq_2yrs
        array[11] = self.pub_rec
        
        array[self.json_data["column_name"].index(self.purpose)] = 1 
       

        
        predicted = self.model.predict([array])[0]
        # print("Predicted",predicted)
        return (predicted)


if __name__ == "__main__":
    
    credit_policy = 1.000000
    int_rate = 0.118900
    installment = 829.100000
    log_annual_inc = 11.350407
    dti = 19.480000
    fico = 737.000000
    days_with_cr_line = 5639.958333
    revol_bal = 28854.000000
    revol_util = 52.100000
    inq_last_6mths = 0.000000
    delinq_2yrs = 0.000000
    pub_rec = 0.000000
    purpose = 'credit_card'

    loa = Loan(credit_policy, int_rate, installment, log_annual_inc, dti, fico, days_with_cr_line, revol_bal, revol_util, inq_last_6mths, delinq_2yrs, pub_rec, purpose)
    charges = loa.get_predicted()
    if charges == 1:
        print("That person is going to Pay Loan ")
    else:
        print("That person is not going to Pay Loan")
    
  
        