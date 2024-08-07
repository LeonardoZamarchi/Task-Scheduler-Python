from cmath import nan
import subprocess
from datetime import datetime
import pandas as pd
import time
import os

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


def valida_exec(title,filepath,time,now_dt):
    print('Valida Execução')
    time_last_up = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%d-%m-%Y")
    if time_last_up < now_dt:
        f = open("log.txt", "a")
        f.write(now_dt + ' - '+ title + " - Falhou em atualizar.\n")
        f.close()
    else:
        f = open("log.txt", "a")
        f.write(now_dt + ' - '+ title + " - Atualizou com sucesso.\n")
        f.close()


while True:
    #csv structure needs to be at the sample
    df = pd.read_csv('tasks.csv')
    ls = df.values.tolist()
    
    for i in ls:
        now_dt = datetime.now().strftime("%d-%m-%Y")
        now = datetime.now().strftime("%H:%M:%S")
        weekday = datetime.today().strftime('%A')
        if i[4] != weekday:
            if i[3] == now:
                exec = run_file(i[0],i[1],i[2],i[3])
                time.sleep(60)
                print(exec)
        else:
            if i[4] == weekday and i[3] == now:
                exec = run_file(i[0],i[1],i[2],i[3])
                time.sleep(60)
                print(exec)
