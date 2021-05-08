file = open('Beyond the Wall of Sleep.txt', encoding="utf8")
Beyond= file.read()
file2 = open('Pride and Prejudice.txt', encoding="utf8")
Pride= file2.read()
Beyond=Beyond.lower().split()
Pride=Pride.lower().split()
dublucated = set(Beyond) & set(Pride)
dublucated = str(dublucated)
import re

newdublucated = re.sub(r'[^\w\s]','',dublucated)
def list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

newdublucated=' '.join(list(newdublucated.split()))
file.close()
file2.close()
res = re.findall(r'\w+', newdublucated)
len(res)
theword = str(res)
print(theword)