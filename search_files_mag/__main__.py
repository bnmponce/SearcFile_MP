from src.com.jalasoft.search_files.menu.input import *
from src.com.jalasoft.search_files.search.search_all_files import *
from src.com.jalasoft.search_files.utils.Validate_Input import *

menu = Menu()

parser = argparse.ArgumentParser(
        description='DEV FUNDAMENTALS II - SEARCH FILES AND FOLDERS.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
parser.add_argument(
    '-s',
    dest='search',
    action='store_true',
    help='perform search with criteria given.',
)
parser.add_argument(
    '--name',
    '-n',
    default=menu.get_name(),
    help='Configure the name of the file or folder to search.',
)
parser.add_argument(
    '--path',
    '-p',
    default=menu.get_path(),
    help='Configure the path in order to search a file or folder.',
)
parser.add_argument(
    '--type',
    '-t',
    default=menu.get_type_search(),
    help='Configure the type of search file or folder to search.',
)

args = parser.parse_args()
valid_name = ValidateInput()

if args.search:
    # print("call name validator")
    print(args.name)
    if args.name:
        validator = valid_name.is_valid_name(args.name) #Add method to validate name
        if validator:
            menu.set_name(args.name)
        else:
            print("Please, enter a valid name, the following characters are not valid: :/\?*|<> ")
            exit()
    if args.path:
        validator = valid_name.is_valid_path(args.path) #Add method to validate path
        if validator:
            menu.set_path(args.path)
        else:
            print("The path you enter does not exist. Please enter a valid path")
            exit()
    if args.type:
        validator = True #Add method to validate file type
        if validator:
            menu.set_type_search(args.type)
        else:
            print("Please, enter a valid type: 1=file, 2=folder, 3=both")
            exit()
    # Add method to search
    print("Searching.....")

    search = SearchFiles()
    results = search.file_all_results(args.path, args.name, int(args.type))
    for item in results:
        result_list = []
        result_list.append(item.get_path())
        result_list.append(item.get_size())
        result_list.append(item.get_extension())
        result_list.append(item.get_is_file())
        print(result_list)



else:
    print("You need to introduce the -s argument to search your files/folders")

