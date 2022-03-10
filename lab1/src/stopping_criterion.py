from enum import Enum


class StoppingMode(Enum):
    """
    Represents all possible stopping criterions.
    """
    MAX_ITERATION = 1
    MAX_TIME = 2
    DESIRED_VAL = 3


class StoppingCriterion:
    """
    Contains three methods for different stopping criterions. Method can be
    selected by providing proper enum value to the constructor.

    Private fields:
    __counter: iteration counter for maximal number of iterations method
    __max_iteration: maximal iteration set by user for maximal number of iterations method
    __desired_val: desired value to be reached for desired value method

    Public fields:
    stopping_criterion: field holding selected function responsible for stopping
    """
    def __init__(self, mode: StoppingMode, max_value):
        """
        Class constructor. Sets proper fields and selects stopping function.

        Parameters:
        mode: stopping mode given as StoppingMode enum.
        max_value: maximal number of iterations, time or desired value (depends on selected mode)
        """
        if mode == StoppingMode.MAX_ITERATION:
            self.__counter = 0
            self.__max_iteration = max_value
            self.stopping_criterion = self.__max_iteration_mode
        elif mode == StoppingMode.MAX_TIME:
            self.__timer = 0
            self.__max_time = max_value
            self.stopping_criterion = self.__max_time_mode
        else:
            self.__desired_val = max_value
            self.stopping_criterion = self.__desired_val_mode
    

    def __max_iteration_mode(self):
        """
        Stops further operation of an optimization method when number of iterations
        reaches maximal number of iterations.
        """
        if self.__counter < self.__max_iteration:
            self.__counter += 1
            return False
        else:
            return True

    # TODO: maybe some kind of asynchronous function?
    def __max_time_mode(self):
        pass

    def __desired_val_mode(self, current_value):
        """
        Stops further operation of an optimization method when the desired value is reached by
        function after optimization process.

        Parameters:
        current_value: value yielded during optimization process which is compared
                       to the desired value.
        """
        if (current_value >= self.__desired_val):
            return True
        else:
            return False
