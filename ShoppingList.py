# provide menu for (1) adding items ADD, (2) assistance HELP, (3) print list SHOW (4) deleting items DELETE  commands

# provide list of all items

shopping_list = []

def show_help():
    # print instructions to use menu on app

    print("""
  ---------------------------------------------------------------------------------------------------------------------

  SHOPPING LIST MENU:

  1. ADD : to add new items to shopping list
  2. HELP : to bring up menu
  3. SHOW : to print list of current items
  4. DELETE : to delete items from shopping list

  ---------------------------------------------------------------------------------------------------------------------
  """)

    user = input("What is your name?\n")
    print ("Hello", user, "!")
    print ("What do you need to get?")

def show_list():
    # print current list of items

    print ("Your shopping list: ")

    for item in shopping_list:
        print (item)


def add_item_to_list(new_item):
    # add new item to shopping list

    shopping_list.append(new_item)
    print ("{} has been added. Your Shopping List now has {} items.".format(new_item, len(shopping_list)))


show_help()
while True:
    # user will be asked for new items to add

    new_item = input("> ")
    # user have option to quit app

    if new_item == "ADD":
        show_list()
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    elif new_item == "DELETE":
        show_list()
        continue

    add_item_to_list(new_item)