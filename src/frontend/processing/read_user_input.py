import csv

# This script will ask the user to search for an item name. If the name doesn't
# match a record, the script will search the known item list for 5 items that
# contain the user input's longest word. 



# inputs: user searches for item
# outputs: item_name






def read_input():
    item_list = []
                        # get current item masterlist
    with open('/Users/kenanbiren/OSRS_Item_Investment_app/data/14day_price.csv', mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            item_list.append(row[0])

                # prompt input
    while(False):
        item = input('What item would you like to search?\n')
        item = item.lower()
        item = item.capitalize()
        print('item: ' + item)
        t = 0
        if item in item_list:
            print('item found! item: ')
            return item
            break
        else:                       # invalid input -> suggestion
            print('Invalid input, please try again. Did you mean:')
            item_split = item.split()
            longest_word = max(item_split, key=len)
            for i in range(len(item_list)):
                if longest_word in item_list[i]:
                    print(item_list[i])
                    t = t + 1
                if t == 5:
                    break



