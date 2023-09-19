n = int(input())
st = []
male = 0
female = 0
pmale = 0
pfemale = 0
for i in range(0, n):
    st.append(input())
for x in range(0, n):
    if(st[x][-1] == "o") or (st[x][-1] == "s"):
        male += 1
    if(st[x][-1] == "a"):
        female += 1
    else: continue

pmale = (male/n)*100
pfemale = (female/n)*100

print(f"Male: {pmale:.2f}%, Female: {pfemale:.2f}%")