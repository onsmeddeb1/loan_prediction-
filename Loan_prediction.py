import numpy as np



with open('Loan_prediction_dataset.csv', mode='r') as file:

    data = np.genfromtxt(file, delimiter=',', skip_header=1, usecols=(8), filling_values=np.nan)


    loan_amounts = data


    mean_loan_amount = np.nanmean(loan_amounts)
    median_loan_amount = np.nanmedian(loan_amounts)
    std_loan_amount = np.nanstd(loan_amounts)


    print(f"Mean Loan Amount: {mean_loan_amount:.2f}")
    print(f"Median Loan Amount: {median_loan_amount:.2f}")
    print(f"Standard Deviation of Loan Amount: {std_loan_amount:.2f}")



