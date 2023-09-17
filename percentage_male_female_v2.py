n = int(input())
names = [input() for i in range(n)]
female_names = [name for name in names if name[-1] == 'a']
female_percent = len(female_names) / n * 100
print(f"Male: {(100-female_percent):.2f}%, Female: {female_percent:.2f}%")