my_dict = {}
size = ['B', 'KB', 'MB', 'GB', 'TB']

with open('input.txt') as f:
    lst = [i.split() for i in f.readlines()]
    for i in lst:
        key = i[0].split('.')[-1]
        if key not in my_dict.keys():
            my_dict[key] = [[int(i[1]), i[2]], i[0]]
        else:
            my_dict[key].append(i[0])
            if i[2] == my_dict[key][0][1]:
                my_dict[key][0][0] += int(i[1])
            elif size.index(my_dict[key][0][1]) < size.index(i[2]):
                my_dict[key][0][0] /= (2 ** (10 * (size.index(i[2]) - size.index(my_dict[key][0][1]))))
                my_dict[key][0][0] += int(i[1])
                my_dict[key][0][1] = i[2]
            else:
                my_dict[key][0][0] += (int(i[1]) / (2 ** (10 * (size.index(my_dict[key][0][1]) - size.index(i[2])))))
            if my_dict[key][0][0] > 1024:
                while my_dict[key][0][0] > 1024:
                    my_dict[key][0][0] /= 1024
                    my_dict[key][0][1] = size[size.index(my_dict[key][0][1]) + 1]

for i in my_dict.values():
    i[0][0] = round(i[0][0])

with open('output.txt', 'w') as f:
    for i in sorted(my_dict.keys()):
        for j in sorted(my_dict[i][1:]):
            f.write(j + '\n')
        f.write('----------\n')
        f.write(f'Summary: {' '.join(str(i) for i in my_dict[i][0])}\n\n')
