with open("../data/train_with_summary.txt", 'r', encoding='utf-8') as file:
    i = 0
    for line in file.readlines():
        with open("../data/mini_set_test.txt", 'a', encoding='utf-8') as f:
            lines = str(line)
            countleft = lines.count('{', 0,len(lines))
            countright = lines.count('}', 0, len(lines))
            countdouble = lines.count('"', 0, len(lines))
            if countleft == 1 and countright == 1 and countdouble==8:
                f.write(str(line).replace("\\",""))
