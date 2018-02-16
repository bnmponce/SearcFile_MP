from src.com.jalasoft.search_files.menu.menu_operations import *
from prettytable import PrettyTable

menu = Menu()
valid_input = ValidateInput()
print_menu = PrintMenu()
args = print_menu.print_menu()
search = SearchFiles()
table = PrettyTable()
menu_operations = MenuOperations()

"""
This is the main class to calls menu, validator ad search classes to perform the search based on user's inputs.
:param args: args.arguments returns the value given as input.
"""
if args.search:
    logger.info('Starting search by -s argument...')
    if args.name:
        menu_operations.name_operation(args.name)
    if args.path:
        menu_operations.path_operation(args.path)
    if args.type:
        menu_operations.type_operation(args.type)
    if args.casesensitive:
        menu_operations.case_sensitive_operation(args.casesensitive)

    print("Searching.....")
    results = search.file_all_results(args.path, args.name, int(args.type), args.casesensitive)

    if args.extension:
        results = menu_operations.extension_filter(args.extension, results)

    if args.size:
        results = menu_operations.size_filter(args.size, args.operator, results)

    if args.date or args.opdate or args.controldate:
        results = menu_operations.date_filter(args.date, args.opdate, args.controldate, results)

    if args.owner:
        results = menu_operations.owner_filter(args.owner, results)

    if args.content:
        results = menu_operations.content_filter(args.content, results)

    if args.namefind:
        results = menu_operations.name_find_filter(args.namefind, args.name, results)

    menu_operations.print_results(results)
    logger.info('Search completed...')


else:
    print("You need to introduce the -s argument to search your files/folders")