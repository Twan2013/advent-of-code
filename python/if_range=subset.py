# Creator: Twan Terstappen
# Created: 13-12-2022
# porpose: check if range is overlapping in both ways.
# See day 4 - Advent of code 2022
import re

def main():
    # set params
    count = 0
    # import file
    f = open('message.txt', 'r')
    content = f.read()
    f.close()
    # extracts the number out of the file and save it as index.
    content = re.findall(r'\d+',content)
    content = [eval(i) for i in content]
    # Group the numbers in the list by 4
    list_grouped = list(zip(*(iter(content),) * 4))


    # cycle through the groups
    for group in list_grouped:
        # setting ranges of the first-second and third and fourth
        rangex = range(group[0], group[1]+1)
        rangey = range(group[2], group[3]+1)

        # check if the range is the subset of the other range
        if set(rangex).issubset(rangey):
            count +=1
        elif set(rangey).issubset(rangex):
            count += 1

    # Printing the total numbers of subsets in a range
    print(f'Total number of subset in a range: {count}')

if __name__ == '__main__':
    main()
