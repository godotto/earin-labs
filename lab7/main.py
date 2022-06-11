import user_interface as ui
import bayessian_network as bn

def main():
    # ui.get_program_parameters()
    b_net = bn.BayessianNetwork()

    print(b_net.mcmc({"test": False}, ["cancer"], 10))

if __name__ == '__main__':
    main()
