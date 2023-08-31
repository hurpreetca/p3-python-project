from simple_term_menu import TerminalMenu
from prettycli import red, yellow, green

class cli():
    def __init__(self):
        pass

    def start():

        print(green("Step into the gateway of rediscovery at our Lost and Found Box!"))
        print(green("Please select an option"))
        options = ["Lost an Item", "Found an Item", "All Lost Items", "All Found Items","Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")

        # print("Step into the gateway of rediscovery at our Lost and Found Box! \n")
        # print("1. Lost an Item")
        # print("2. Found an Item")
        # print("3. ")
        # print()