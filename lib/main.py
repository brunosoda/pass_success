from pass_success.lib.interface import *
from pass_success.lib.archive import *
from time import sleep
import statistics
import scipy.stats

# ------------------------ ABOUT THE CODE ----------------------------
header('\033[32mPASS SUCCESS PERCENT (PSP)\033[m')
sleep(1)
print('This code is about a soccer statistic analysis.'
      '\nSource: www.whoscored.com')
line()
sleep(1)
print("\nChoose 2 of the 3 pass success samples below:"
      "\n- Each sample is from a different team"
      "\n- Each sample is from Brasileirão matches"
      "\n")

# -------------------- CHOOSING THE SAMPLES ---------------------------
sleep(1)
teams = []
while True:
    n = menu(['São Paulo 2020 (SPFC20)', 'São Paulo 2021 (SPFC21)', 'Atlético MG 2021 (ATMG21)'])
    if n == 1:
        teams.append('SPFC20')
        print('\033[32m -> SPFC20 selected as sample 1\033[m')
        break
    elif n == 2:
        teams.append('SPFC21')
        print('\033[32m -> SPFC21 selected as sample 1\033[m')
        break
    elif n == 3:
        teams.append('ATMG21')
        print('\033[32m -> ATMG21 selected as sample 1\033[m')
        break
    else:
        print('\033[31mERROR! Invalid input.\033[m')
while True:
    s2 = readInt('Choose the second sample: ')
    if s2 == n:
        print('\033[33mPlease choose another sample\033[m')
    else:
        if s2 == 1:
            teams.append('SPFC20')
            print('\033[32m -> SPFC20 selected as sample 2\033[m')
            break
        elif s2 == 2:
            teams.append('SPFC21')
            print('\033[32m -> SPFC21 selected as sample 2\033[m')
            break
        elif s2 == 3:
            teams.append('ATMG21')
            print('\033[32m -> ATMG21 selected as sample 2\033[m')
            break
        else:
            print('\033[31mERROR! Invalid input.\033[m')
print(teams)

# ------------------------- READING THE SAMPLES -------------------------------
sleep(1.5)
header(f'\033[34mFirst Sample: {teams[0]}\033[m')
readArchive(teams[0]+'.txt')
sleep(1.5)
header(f'\033[34mSecond Sample: {teams[1]}\033[m')
readArchive(teams[1]+'.txt')

# ------------------------------- STATISTICS ---------------------------------
sleep(1.5)
header('\033[34mSTATISTICS\033[m')
# ------- TURNING .txt DATA INTO PYTHON LIST
sample1 = listing(teams[0]+'.txt')
sample2 = listing(teams[1]+'.txt')

print('\033[33m -> HYPOTHESIS\033[m')
print('Null Hypothesis: X1 = X2', end=' '
      'Alternative Hypothesis: X1 <> X2')

print('\n\033[33m -> MEAN\033[m')
avg1 = statistics.mean(sample1)
avg2 = statistics.mean(sample2)
print(f"{teams[0][:4]}'s average PSP in Brasileirão 20{teams[0][-2:]}: {avg1:.2f}%")
print(f"{teams[1][:4]}'s average PSP in Brasileirão 20{teams[1][-2:]}: {avg2:.2f}%")

print('\n\033[33m -> STANDARD DEVIATION\033[m')
stdev1 = statistics.stdev(sample1)
print(f"{teams[0][:4]}'s PSP standard deviation in 20{teams[0][-2:]}: {stdev1:.2f}%")
stdev2 = statistics.stdev(sample2)
print(f"{teams[1][:4]}'s PSP standard deviation in 20{teams[1][-2:]}: {stdev2:.2f}%")

print('\n\033[33m -> STANDARD ERROR OF THE MEAN\033[m')
sterror = float(sem(stdev1, stdev2, len(sample1), len(sample2)))
print(f'Standard error of the mean (SEM): {sterror}%')

print('\n\033[33m -> T-STATISTIC\033[m')
ts = tstat(avg1, avg2, sterror)
print(f't-Statistic: {ts:.2f}')

print('\n\033[33m -> T-CRITICAL VALUE\033[m')
df = dfis(len(sample1), len(sample2))
print(f'Degrees of freedom: {df}')
tcv = scipy.stats.t.ppf(1-.05/2, df=df)
print(f't-Critical values: -{tcv:.2f} and {tcv:.2f}')

print('\n\033[33m -> CONCLUSION\033[m')
print('With alfa=0.05 and two-tailed test')
if ts >= tcv or ts <= -tcv:
    print('We reject the null hypothesis, then the results of the test are statistically significant')
else:
    print('We fail to reject the null hypothesis, then the results of the test are not statistically significant')
