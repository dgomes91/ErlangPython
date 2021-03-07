import math
#Erlang Formula
def ErlangC(NCalls,Period,AHT,Time):
  CallsHour = (NCalls / Period) * 60
  Erlangs = int((CallsHour * AHT)/3600)
  SL = float(0)
  N = Erlangs
  Y= float(0)
  x = float(0)
  while SL < SLA:
    Y= float(0)
    N = (N + 1)
    x = math.pow(Erlangs,N) /math.factorial(N)*(N /(N-Erlangs))
    for i in range(int(N)):
      Y = float(Y + (math.pow(Erlangs,i)/math.factorial(i)))
    Pw = 0
    Pw = x / ( Y + x)
    SL = 1-(Pw * (math.exp(-((N - Erlangs)*(Time/AHT)))))
    Agents = N
    ASA = (Pw * AHT)/(N - Erlangs)
  return Agents, ASA, SL*100
#Maing Program
print(f'#'*25)
print('## Erlang Calculator C ##')
print(f'#'*25)
#Variables
NCalls = float(input('Insert the number of calls: '))
Period = float(input('Insert the period in minutes: '))
AHT = float(input('Insert the average handled time in seconds: '))
SLA = float(input('Insert the service level: '))
Time = float(input('Insert the time in seconds that a call has to wait: '))
#Return
Agents, ASA, SL = ErlangC(NCalls,Period,AHT,Time)
#Result
print(f'Head Count = {Agents} Agts\n ASA = {ASA:.2f} seconds\n Service Level = {SL:.2f}%')
input('Press enter to exist...')