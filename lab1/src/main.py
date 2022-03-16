from time import sleep

import user_interface as ui
import user_input as uin

def main():
    ui.clear_console()
    mode = 0
    while mode != 1 and mode != 2:
        print("Select mode:")
        print("1. Normal mode")
        print("2. Batch mode")
        mode = uin.integer_input("Choose mode: ")

        if mode != 1 and mode != 2:
            print("Wrong option")
            sleep(1)
            ui.clear_console()
    
    if mode == 1:
        x, y = ui.normal_mode()
        ui.clear_console()
        print(f"The optimal value is {y} and it is value for argument {x}")
    else:
        ui.clear_console()
        number_of_iterations = 0
        while number_of_iterations < 1 or not number_of_iterations:
            print("Provide number of iterations:")
            number_of_iterations = uin.integer_input()

            if number_of_iterations < 1 or not number_of_iterations:
                print("It has to be a positive integer")
                sleep(1)
                ui.clear_console()

        mean, standard_deviation = ui.batch_mode(number_of_iterations)
        print(f"Obtained mean value is {mean} having standard deviation of {standard_deviation}")

if __name__ == '__main__':
    main()
