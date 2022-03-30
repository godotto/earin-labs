import user_interface as ui

def main():
    ui.clear_console()
    params = ui.select_parameters()
    print("Chosen parameters are \n A:", params['A'], "\n", "b:", params['b'], "\n", "c:", params['c'], "\n" ,"d:", params['d'] )

if __name__ == '__main__':
    main()