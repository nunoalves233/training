from tabulate import tabulate

data = [["Mavs", 99], 
        ["Suns", 91], 
        ["Spurs", 94], 
        ["Nets", 88]]

col_names = ["Team", "Points"]

print(tabulate(data, headers=col_names, tablefmt="grid", showindex="always"))