#import libraries
import PySimpleGUI as sg
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

#matplotlib parameters
plt.rcParams['figure.figsize'] = (5, 3)
plt.rcParams['figure.dpi'] = 75

#set up the lists
todays_expenses = []
headings = ['Date (MM/DD/YYYY)', 'Expense name', 'Expense amount']

#design the popup window
sg.theme('LightPurple')
layout = [ [sg.Text(headings[0]), sg.Input(key=headings[0])],
           [sg.Text(headings[1]), sg.Input(key=headings[1])],
           [sg.Text(headings[2]), sg.Input(key=headings[2])],
           [sg.Button('Add expense'), sg.Button('End')],
           [sg.Table(todays_expenses, headings, key='expense_table')]]
window = sg.Window('Expense Tracker', layout)

#loop to add expense info
while True:
    event, values = window.read()
    if event == 'Add expense':
        todays_expenses.append([values[headings[0]],
                                values[headings[1]],
                                values[headings[2]]])
        window['expense_table'].update(values=todays_expenses)
    if event == sg.WIN_CLOSED or event == 'End':
        break
window.close()

#use numpy to convert list to array to table
expenses_array = np.array(todays_expenses)
expenses_2d = expenses_array.reshape(3,3) # make it work with more than 3 rows

#use pandas to convert table to data frame
df = pd.DataFrame(expenses_2d, columns=['Date','Expense name','Expense amount'])

#convert date and expense amount to appropriate data types
df['Date'] = pd.to_datetime(df['Date'])
df['Expense amount'] = pd.to_numeric(df['Expense amount'])
print(df)

#run some stats
#expenditure sum
expense_sum = df['Expense amount'].sum()
print("Total expenditures: $" + str(expense_sum))

#top 5 expenses
sorted_df = df.sort_values(by=['Expense amount'], ascending=False).head(5)
sorted_list = sorted_df['Expense name'].tolist()
print("Your top 5 expenses were: " + str(sorted_list))

#use matplotlib to plot expenses over time
plt.scatter(x=df['Date'], y=df['Expense amount'], color='teal', alpha=0.5)
plt.title('Recent expenditures')
plt.xlabel('Date')
plt.ylabel('Expense amount')
plt.tick_params(axis='x', direction='out', labelrotation=30)
plt.axhline(y=expense_sum) #add AB line for sum
plt.annotate(text='Total expenses', xy=(0, expense_sum)) #didnt work
plt.show()

#show percentage breakdown for top 5 expenses
#top_vals_df = df.sort_values(by=['Expense amount'], ascending=False).head(5))
#plt.pie(x=df['Expense amount'], labels=df['Expense name'])

#set a budget + show amount left in budget + warning if budget is exceeded + add AB line for budget


#make a suggestion


#store expenses to an sqlite database (using sqlite3)



