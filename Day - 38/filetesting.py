import pandas
import pandas as pd
import datetime
time_now = datetime.datetime.now()


raw_data = {'Day':"Monday",
            'Workout Type': "Run",
            'Duration': '1 hour',
            'Input': 'had an hour run'}



main_date = pd.DataFrame(["Monday","Run","1 hours",'Had an hour long run'],columns=[time_now.date()],index=['Day','Workout Type','Duration','Input'])

df = pd.DataFrame(["Tuesday","climb","3 hours",'Climbed with lisa for 3 hours'],columns=['dsadw'],index=['Day','Workout Type','Duration','Input'])

df.to_csv("new file.csv",mode='a',header=False,index=1)

data = pandas.read_csv("final_data.csv")
print(data)