import argparse

def main():

    banner = '''
    \n<-> ETL Express <->
    \n[*] Fast ETL, like an espresso\n
    \n[*] Program to facilitate the ETL process via command line\n
    \n[@] Felipe Santos -> https://github.com/FelipeSantos-cco/
    '''

    parser = argparse.ArgumentParser(prog="ETL Express",
                                    description=banner)

    parser.add_argument('-el', '--extract-local'
                        , type=str
                        , help='Extract the files and turn them into a DF'
                        , action = 'store'
                        , dest = 'file')

    args = parser.parse_args()

    if getattr(args, "extract-local"):
        print(args.extract_local)
    
    else:
        print("Teste")
        print(args.extract_local)


if __name__ == "__main__":
    main()