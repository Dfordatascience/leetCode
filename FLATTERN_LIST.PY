flat_list = []
input_list = [[0, 1, 2], [3, 4, [5, [6, [7]], 8]], 9, 11, [15, 78, 99], [110]]

temp_list = []


def extract_list(flattern_list):
    for i in flattern_list:
        if type(i) == list:
            extract_list(i)
        else:
            temp_list.append(i)


if __name__ == '__main__':
    print(extract_list(input_list))
