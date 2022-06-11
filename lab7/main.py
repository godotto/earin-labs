import user_interface as ui
import bayessian_network as bn

def main():

    query_list, evidence_dict, steps_num = ui.get_program_parameters()
  
    if len(query_list) == 0:
        print("You dumb shumck, what did you expect? No simulation for you!")
    else:
        b_net = bn.BayessianNetwork()
        print(b_net.mcmc(evidence=evidence_dict, query = query_list, steps = steps_num))

if __name__ == '__main__':
    main()
