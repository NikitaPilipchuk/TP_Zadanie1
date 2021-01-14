def count_puddle(lst):
    index = []
    count = 0
    for i in range(len(lst)):
        if i == 0 and lst[i+1] < lst[i] or i == len(lst)-1 and lst[i-1] < lst[i] or lst[i-1] < lst[i] > lst[i+1]:
            index += [i]
    for i in range(len(index)-1):
        edge =  lst[index[i]] if lst[index[i]] < lst[index[i+1]] else lst[index[i+1]]
        for i in lst[index[i]+1:index[i+1]]:
            count += edge - i
    return count

   
with open("island.txt") as f:
    lst = [list(map(int, i)) for i in "".join(f.read().split("\n")).split("0") if i] #Считывает файл, если есть нулевые значения, то разбивает землю по ним на отдельные "острова" и выводит информацию по каждому
    for i in range(len(lst)):
        print(f"Количество блоков, занятых водой{'' if len(lst) == 1 else ', на острове ' + str(i+1)}: {count_puddle(lst[i])}")
            
