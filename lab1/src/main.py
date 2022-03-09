
# usermenu

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

# run_optimization (run chosen method n-times) - when batch mode n>=2, normal n=1

#print results
#normal mode: x*, F(x*), G(x*)
#batch mode: mean values of x*, F(x*), G(x*), standard deviation