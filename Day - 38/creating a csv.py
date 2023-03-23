import pandas
import pandas as pd
import datetime

time_now = datetime.datetime.now()

raw_data = {"Date":[time_now.strftime("%m/%d/%Y")],
            'Day':["Monday"],
            'Workout Type': ["Run"],
            'Duration': ['1 hour'],
            'Input': ['had an hour run']}

new_data = {"Date":[time_now.strftime("%m/%d/%Y")],
            'Day':["Tuesday"],
            'Workout Type': ["climb"],
            'Duration': ['3 hours'],
            'Input': ['Climbed with lisa for 3 hours']}


data = pandas.DataFrame(raw_data)
data.to_csv('Final Data.csv')
print(data)
#
# original_data = pandas.read_csv('Final Data.csv')
#
date = pandas.DataFrame(new_data)

date.to_csv('Final Data.csv', mode='a', header=False)

# main_date = pd.DataFrame(["Monday","Run","1 hours",'Had an hour long run'],columns=[time_now.date()],index=['Day','Workout Type','Duration','Input'])
# new_data = pd.DataFrame(["Tuesday","climb","3 hours",'Climbed with lisa for 3 hours'],columns=['Day','Workout Type','Duration','Input'],index=["0"])
#

# new_data.to_csv('new file.csv')
# main_date.to_csv('new file.csv',mode='a',index=True,header=True)
# new_data.to_csv('new file.csv',mode='a',index=True,header=True)
#
# data = pandas.read_csv('new file.csv')
# print(data)
