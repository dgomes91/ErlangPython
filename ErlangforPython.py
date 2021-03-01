import math
NCalls = float(100)
Period = float(30)
AHT = float(180)
SLA = float(0.8)
Time = float(20)

def ErlangC(NCalls,Period,AHT,Time):
  CallsHour = (NCalls / Period) * 60
  Erlangs = (CallsHour * AHT)/3600
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
Agents, ASA, SL = ErlangC(NCalls,Period,AHT,Time)

print(f'Head Count = {Agents} Agts\n ASA = {ASA:.2f} seconds\n Service Level = {SL:.2f}%')