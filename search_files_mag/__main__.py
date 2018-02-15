from src.com.jalasoft.search_files.menu.menu_options import *
from src.com.jalasoft.search_files.search.search_all_files import *
from src.com.jalasoft.search_files.utils.validate_input import *
from prettytable import PrettyTable

menu = Menu()
valid_input = ValidateInput()
print_menu = PrintMenu()
args = print_menu.print_menu()
search = SearchFiles()
table = PrettyTable()

"""
This is the main class to calls menu, validator ad search classes to perform the search based on user's inputs.
:param args: args.arguments returns the value given as input.
"""
if args.search:
    logger.info('Starting search by -s argument...')
    if args.name:
        validator = valid_input.is_valid_name(args.name)
        if validator:
            menu.set_name(args.name)
        else:
            print("Please, enter a valid name, the following characters are not valid: :/\?*|<> ")
            exit()
    if args.path:
        validator = valid_input.is_valid_path(args.path)
        if validator:
            menu.set_path(args.path)
        else:
            print("The path you enter does not exist. Please enter a valid path")
            exit()
    if args.type:
        validator = valid_input.is_valid_type(args.type)
        if validator:
            menu.set_type_search(args.type)
        else:
            print("Please, enter a valid type: 1=file, 2=folder, 3=both")
            exit()
    if args.casesensitive:
        validator = valid_input.is_valid_flag_of_sensitivecase(args.casesensitive)
        if validator:
            menu.set_case_sensitive(args.casesensitive)
        else:
            print("Please enter a valid parameter: c=case sensitive or n=non case sensitive")
            exit()
    print("Searching.....")
    results = search.file_all_results(args.path, args.name, int(args.type), args.casesensitive)

    if args.extension:
        results = search.filter_by_extension(args.extension, results)

    if args.size:
        validator = valid_input.is_valid_size(args.size)
        if validator:
            operator = valid_input.is_valid_operators(args.operator)
            if operator:
                if args.operator == 'l':
                    results = search.filter_by_size('l', float(args.size), results)
                if args.operator == 'g':
                    results = search.filter_by_size('g', float(args.size), results)
                if args.operator == 'e':
                    results = search.filter_by_size('e', float(args.size), results)
            else:
                print("Please enter a valid operator: l = less than, g= greater than or e = equal")
                exit()
        else:
            print("please enter a valid number as size, negative numbers or characters are not allowed")
            exit()

    if args.date or args.opdate or args.controldate:
        if args.date and args.opdate and args.controldate:
            validator = valid_input.is_valid_date(args.date)
            if validator:
                validator = valid_input.is_valid_operators(args.opdate)
                if validator:
                    validator = valid_input.is_valid_controldate(args.controldate)
                    if validator:
                        if args.controldate == 'c':
                            results = search.filter_by_date_created(results, args.date, args.opdate)
                        elif args.controldate == 'm':
                            results = search.filter_by_date_modified(results, args.date, args.opdate)
                        elif args.controldate == 'a':
                            results = search.filter_by_date_last_access(results, args.date, args.opdate)
                        else:
                            print("invalid control date entered")
                    else:
                        print("Please, enter a valid control date parameter: c, m or a")
                        exit()
                else:
                    print("Please enter a valid operator date: l = less than, g= greater than or e = equal")
                    exit()
            else:
                print("Please enter a valid date in the following format 'MM-DD-YYYY' un numeral format")
                exit()
        else:
            print("You must to enter three parameters to search by date: -d, -op, -cd")
            exit()

    if args.owner:
        validator = True
        if validator:
            results = search.filter_by_owner(results, args.owner)
        else:
            print("please enter a owner")
            exit()

    if args.content:
        validator = True
        if validator:
            results = search.content_searcher(results, args.content)
        else:
            print("Please enter the content you are looking for")
            exit()

    if args.namefind:
        validator = valid_input.is_valid_operator_to_exact_search(args.namefind)
        if validator:
            if args.namefind == 'e':
                results = search.search_exactly_equal(results, args.name)
        else:
            print("please enter a valid value 'e' for the argument nf")
            exit()

    table.field_names = ["Path", "Type", "Size", "Owner", "Created Date", "Modified Date", "Accessed Date"]
    table.align["Path"] = "l"
    table.align["Type"] = "r"
    table.align["Size"] = "r"
    table.align["Owner"] = "r"
    table.align["Create Date"] = "r"
    table.align["Modified Date"] = "r"
    table.align["Accessed Date"] = "r"

    for item in results:
        if item.get_is_file():
            return_type = 'File'
        else:
            return_type = 'Folder'

        table.add_row([item.get_path(),
                       return_type,
                       item.get_size(),
                       item.get_owner(),
                       item.get_date_created(),
                       item.get_date_modified(),
                       item.get_date_last_access()])
    print(table)
    logger.info('Search completed...')


else:
    print("You need to introduce the -s argument to search your files/folders")