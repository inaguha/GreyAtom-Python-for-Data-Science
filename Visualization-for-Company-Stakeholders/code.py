# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)


# Step 1 
loan_status = data['Loan_Status'].value_counts()
plt.bar(loan_status.index, loan_status)
plt.show()


# Step 2
property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Property_Area')
plt.ylabel('Loan Status')

plt.xticks(rotation=45)


# Step 3
education_and_loan = data.groupby(['Education', 'Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')

plt.xticks(rotation=45)



# Step 4 
graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']

graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')

#For automatic legend display
plt.legend()



# Step 5
fig, (ax_1, ax_2, ax_3) = plt.subplots(1, 3, figsize=(20,8))

ax_1.scatter(data['ApplicantIncome'], data["LoanAmount"])
ax_1.set(title='Applicant Income')


ax_2.scatter(data['CoapplicantIncome'], data["LoanAmount"])
ax_2.set(title='Coapplicant Income')


data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

ax_3.scatter(data['TotalIncome'], data["LoanAmount"])
ax_3.set(title='Total Income')





