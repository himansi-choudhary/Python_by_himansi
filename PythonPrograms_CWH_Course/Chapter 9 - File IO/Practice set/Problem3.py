# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files. 
# Place these files in a folder for a 13 – year old.

def genratetable(j):
    table = ""
    for i in range(1, 11):
        table += f"{j} X {i} = {j*i}\n"   # + :- update

    # after rumming this code makes files in tables folder
    with open(f"tables/table_{j}", "w") as f:
        f.write(table)
    


for i in range(2, 21):
    genratetable(i)