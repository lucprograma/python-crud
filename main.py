# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import controllers.create as create
from controllers.get import get_registers
from controllers.delete import delete
from controllers.update import update
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #create.create_register('Python')
    for category in get_registers():
        print(category)
    #delete(11)
    #update({"id": 3, "name": 'horror'})
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
