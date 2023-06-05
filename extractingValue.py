import re

pattern = 'Figure [0-9]+|Fig\. [0-9]+|Figura [0-9]+'

with open("wyniki3.txt", encoding='utf-8') as f:
    lines = f.readlines()

for i in range(0, 300):
    matches_fig = re.findall(pattern, lines[i])
    if matches_fig:
        list2 = matches_fig
        l = [s.split()[-1] for s in list2]
        for y in range(len(l)):
            l[y] = int(l[y])
        print(max(l))

