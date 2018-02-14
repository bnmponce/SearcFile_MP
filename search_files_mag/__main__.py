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
        validator = True  # Add validator for values c or n
        if validator:
            menu.set_case_sensitive(args.casesensitive)
        else:
            print("Please enter a valid parameter: c=case sensitive or n=non case sensitive")
            exit()
    print("Searching.....")
    results = search.file_all_results(args.path, args.name, int(args.type), args.casesensitive)

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
            if args.operator == 'l':
                results = search.filter_by_size('l', float(args.size), results)
            if args.operator == 'g':
                results = search.filter_by_size('g', float(args.size), results)
            if args.operator == 'e':
                results = search.filter_by_size('e', float(args.size), results)
        else:
            print("please enter a valid number as size, negative numbers or characters are not allowed")
            exit()

    if args.date or args.opdate or args.controldate:
        if args.date and args.opdate and args.controldate:
            validator = valid_input.is_valid_date(args.date)
            if validator:
                validator = valid_input.is_valid_opdate(args.opdate)
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
                    print("Please enter a valid operator date valid: l, g, e")
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
            results = search.content_seacher(results, args.content)
        else:
            print("Please enter the content you are looking for")
            exit()

    if args.namefind:
        validator = True #Add validator to just receive e
        if validator:
            if args.namefind == 'e':
                results = search.search_exactly_equal(results, args.name)
        else:
            print("please enter a valid value 'e' for the argument nf")
            exit()

    # if args.contentfind:
    #     validator = True #Add validator to just receive e
    #     if validator:
    #         if args.operator == 'e':
    #             results = search.content_seacher(results, args.content)
    #     else:
    #         print("please enter a valid value 'e' for the argument cf/content find")
    #         exit()


    for item in results:
        if type(item) == tuple or type(item) == str:
            print(item)

        else:
            print(item.get_path())


else:
    print("You need to introduce the -s argument to search your files/folders")