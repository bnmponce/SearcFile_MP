from src.com.jalasoft.search_files.menu.menu_options import *
from src.com.jalasoft.search_files.search.search_all_files import *
from src.com.jalasoft.search_files.utils.validate_input import *

menu = Menu()
valid_input = ValidateInput()
print_menu = PrintMenu()
args = print_menu.print_menu()
search = SearchFiles()

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
        #validator = True
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
        # validator = valid_input.is_valid_extention(args.path, args.extension)# #Add method to validate extension
        if validator:
            menu.set_extension(args.extension)
        else:
            print("please, enter a valid extension: .* .doc, etc")
            exit()
        result_ext = search.filter_by_extension(args.extension, results)

    if args.size:
        validator = True
        #validator = valid_input.is_valid_size(args.size)
        if validator:
            menu.set_size(args.size)
            if args.operator == 'l':
                results = search.filter_by_size('l', int(args.size), results)
            if args.operator == 'g':
                results = search.filter_by_size('g', int(args.size), results)
            if args.operator == 'e':
                result_size = search.filter_by_size('e', int(args.size), results)
        else:
            print("please enter a valid number as size, negative numbers or characters are not allowed")
            exit()

    if args.date:
        validator = True #valid date validation
        if validator:
            menu.set_date(args.date)
            results_date = search.filter_by_date(results, args.date)
        else:
            print("please enter a valid date in the following format 'DD-MM-YYYY'")
            exit()


    for item in results:
        print(item)

else:
    print("You need to introduce the -s argument to search your files/folders")