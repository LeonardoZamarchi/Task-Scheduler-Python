import subprocess
from datetime import datetime
import pandas as pd
import time
def run_file(title, path, file, time):
    try:
        filepath = (path+file)
        print('Running the process, '+title+' at '+ str(time))
        p = subprocess.Popen(filepath, shell=True)
        stdout, stderr = p.communicate()     
        res = ('Process '+ title + ' was finished at '+str(time)+' STATUS: SUCCESS')
        return res
    except:
        res = ('Process '+ title + ' was finished at '+str(time)+' STATUS: FAILED')
        return res

while True:
    #csv structure needs to be at the sample
    df = pd.read_csv('tasks.csv')
    ls = df.values.tolist()
    for i in ls:
        now = datetime.now().strftime("%H:%M:%S")
        if i[3] == now:
            exec = run_file(i[0],i[1],i[2],i[3])
            time.sleep(10)
            print(exec)