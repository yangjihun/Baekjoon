plastic = input()
s = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}

for k in plastic:
  if k=='9':
    s['6']+=1
  else:
    s[k]+=1
s['6'] = s['6']//2 + s['6']%2
print(max(s.values()))