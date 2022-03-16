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

#get from user:
# 1.choose optimization method 
# 2.choose function to be optimized (F(x)/G(x))
# 3.function parameters :
#F(x): a,b,c,d - scalar
#G(x): c - scalar, b- d-dimensional vector, d-dimensions, A - positive-definite matrix
# 4. define starting point:
# 4.1. initial vector / scalar number from user
# 4.2. range of numbers
# 5.stopping conditions
# 5.1. max number of iterations
# 5.2. desired value F(x) or G(x) (so the process is finished when F(x)>=value_to_reach/ G(x)>=value_to_reach )
# 5.3. maximum computation time

#checking if A is a positive-definite matrix

if __name__ == '__main__':
    main()

#print results
#normal mode: x*, F(x*), G(x*)
#batch mode: mean values of x*, F(x*), G(x*), standard deviation