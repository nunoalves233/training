def grades_frequency(grades):
    ngrades = len(grades)
    freq = dict()
    for grade in range(21):
        freqgrade = grades.count(grade)
        if freqgrade > 0:
            freq[grade] = round(100 * freqgrade / ngrades , 1)
    return freq

n = int(input(""))
grades = [0] * n
for i in range(n):
    grades[i] = float(input(""))
freq = grades_frequency(grades)
print(freq)
