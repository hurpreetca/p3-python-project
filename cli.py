from simple_term_menu import TerminalMenu
from prettycli import red, green, blue
from models import User, Item
from tabulate import tabulate
from queries import *


class Cli:
    def __init__(self):
        pass

    def start(self):
        self.clear_screen()
        print(
            green("Step into the gateway of rediscovery at our Lost and Found Box! \n")
        )
        print(green("Please select an option"))
        options = [
            "Report an Item",
            "Claim an Item",
            "Display all Items",
            "Exit",
        ]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Report an Item":
            handle_report_item()
        elif options[menu_entry_index] == "Claim an Item":
            self.handle_item_claim()
        elif options[menu_entry_index] == "Display all Items":
            self.handle_all_item_list()
        elif options[menu_entry_index] == "Exit":
            self.exit()
        else:
            self.exit()

        ##########################################################################################################

    def handle_report_item(self):
        self.clear_screen()
        print(blue("Select a suitable option: /n"))
        options = [
            "Lost an Item",
            "Found an Item",
            "Return to the main-menu",
        ]
        terminal_sub_menu = TerminalMenu(options)
        sub_menu_entry_index = terminal_sub_menu.show()
        if options[sub_menu_entry_index] == "Lost an Item":
            result = handle_lost_item()
            print(red("Your request is added to the system."))
        elif options[sub_menu_entry_index] == "Found an Item":
            self.handle_found_item()
        elif options[sub_menu_entry_index] == "Return to the main-menu":
            self.start()
        else:
            self.exit()

        ##########################################################################################################

    def handle_all_item_list(self):
        print(blue("Select a suitable option: /n"))
        self.clear_screen()
        options = [
            "All lost Items",
            "All found Items",
            "All claimed Items",
            "Find by Item Name",
            "Return to the main-menu",
        ]
        terminal_sub_menu = TerminalMenu(options)
        sub_menu_entry_index = terminal_sub_menu.show()
        if options[sub_menu_entry_index] == "All lost Items":
            result = lost_item_list(status="Lost")
            print(result)
        elif options[sub_menu_entry_index] == "All found Items":
            result = found_item_list(status="Found")
            print(result)
        elif options[sub_menu_entry_index] == "All claimed Items":
            result = claimed_item_list(final_status="Resolved")
            print(result)
        elif options[sub_menu_entry_index] == "Find by Item Name":
            self.find_by_item_name()

        elif options[sub_menu_entry_index] == "Return to the main-menu":
            self.start()
        else:
            self.exit()

    ####################################CLEAR SCREEN FUNCTION#################################################
    def clear_screen(self, lines=44):
        print("\n" * lines)

    ######################################EXIT TO CLOSE THE PROGRAM###########################################
    def exit(self):
        print("\n" * 30)
        print(green("Thank you for visiting, Goodbye!"))

    def find_by_item_name(self):
        self.clear_screen()
        item_name_text = input("item_name:")
        query = session.query(Item).filter(Item.item_name.like(f"%{item_name_text}"))
        print(query.all())


##########################################################################################################
app = Cli()
app.start()
