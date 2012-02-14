from time import time
from time import sleep

sequence =  [('sample_1', 0), ('sample_2', 0),
             ('sample_1', .8), ('sample_2', 1.2),
             ('sample_1', 1.6), ('sample_2', 2.4), 
             ('sample_1', 2.4), ('sample_2', 3.6),
             ('sample_1', 3.2), ('sample_2', 4.8),
             ('sample_1', 4), ('sample_2', 6)]

def calculate_sleep(beginning_of_sequence, next_event):
    """Accepts: a Python time.time() value from the the starting point and
    next_event, which is the time for the next event.
    This function adds the next_event to the beginning_beginning of sequence and
    subtracts time.time(), which is now to the time in seconds until the next event
    
    Returns: a time value until the next event in relation to now 
    """
    time_to_next_event_from_beginning = beginning_of_sequence + next_event
    return time_to_next_event_from_beginning - time()
    
def print_char_in_sequence(seq_list):
    """
    Accepts a list of tuples in the format: ('sample_name', 1.2), wherein the first
    element is a name of a file and the second element is a duration to print the 
    file name
    """
    beginning_time = time()
    seq_list.sort(key=lambda x: x[1])
    for index, item in enumerate(seq_list):
        # sleep until the next event
        if calculate_sleep(beginning_time, item[1]) < 0:
            sleep(0)
        else: sleep(calculate_sleep(beginning_time, item[1]))
        print item[0]
    

