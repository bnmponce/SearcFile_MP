from src.com.jalasoft.search_files.menu.menu_options import *
from src.com.jalasoft.search_files.search.search_all_files import *
from src.com.jalasoft.search_files.utils.validate_input import *

menu = Menu()
valid_input = ValidateInput()
print_menu = PrintMenu()
args = print_menu.print_menu()
search = SearchFiles()

"""
This is the main class to calls menu, validator ad search classes to perform the search based on user's inputs.
:param args: args.arguments returns the value given as input.
"""
if args.search:
    #print(args.name)
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
    print("Searching.....")
    results = search.file_all_results(args.path, args.name, int(args.type))

    if args.extension:
        validator = True
        if validator:
            menu.set_extension(args.extension)
        else:
            print("please, enter a valid extension: .* .doc, etc")
            exit()
        results = search.filter_by_extension(args.extension, results)

    if args.size:
        validator = valid_input.is_valid_size(args.size)
        if validator:
            menu.set_size(args.size)
            if args.operator == 'l':
                results = search.filter_by_size('l', float(args.size), results)
            if args.operator == 'g':
                results = search.filter_by_size('g', float(args.size), results)
            if args.operator == 'e':
                results = search.filter_by_size('e', float(args.size), results)
        else:
            print("please enter a valid number as size, negative numbers or characters are not allowed")
            exit()

    if args.date and args.opdate and args.controldate:
        validator = True #valid date validation
        # validator = valid_input.is_valid_date(args.date)
        if validator:
            validator = True #valid_input.is_valid_opdate(args.opdate)
            if validator:
                validator = True #valid_input.is_valid_controldate(args.controldate)
                if validator:
                    #menu.set_date(args.date)
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
                print("Please enter a valid operator date valid: l, g, e")
                exit()
        else:
            print("Please enter a valid date in the following format 'MM-DD-YYYY' un numeral format")
            exit()
    # else:
    #     print("You must to enter three parameters to search by date: -d, -op, -cd")
    #     exit()

    for item in results:
        print(item.get_path())
        #print(item)

else:
    print("You need to introduce the -s argument to search your files/folders")