from simple_term_menu import TerminalMenu
from prettycli import red, yellow, green
from models import User, Item

class Cli():
    def __init__(self):
        pass

    def start(self):

        # self.clear()

        print(green("Step into the gateway of rediscovery at our Lost and Found Box!"))
        print(green("Please select an option"))
        options = ["Report a lost and found Item","Claim an Item" "All lost/found Items", "All recently claimed Items","Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")


        import ipdb
        

        if

        # print("Step into the gateway of rediscovery at our Lost and Found Box! \n")
        # print("1. Lost an Item")
        # print("2. Found an Item")
        # print("3. ")
        # print()

        app= Cli()
        app.start()