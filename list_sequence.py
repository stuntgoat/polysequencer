from time import time
from time import sleep
import batch_parser as bp

def calculate_sleep(beginning_of_sequence, next_event):
    """Accepts: a Python time.time() value from the the starting point and
    next_event, which is the time for the next event.
    This function adds the next_event to the beginning_beginning of sequence and
    subtracts time.time(), which is now to the time in seconds until the next event
    
    Returns: a time value until the next event in relation to now 
    """
    if next_event == 0:
        return 0
    else:
        nowish = time()
        return (beginning_of_sequence + next_event) - nowish
    
def print_char_in_sequence(seq_list):
    """
    Accepts a list of tuples in the format: (1.2, 'sample_name'), wherein the first
    element is a duration from the beginning of the sequence to print the next file name, ie the second element in the list;
    Accepts: a sorted sequence list, seq_list
    Returns: None"""

    beginning_time = time()
    for item in seq_list:
        # sleep until the next event
        interval = calculate_sleep(beginning_time, item[0])
        sleep(interval)
        # print(interval)
        for filename in item[1]: # print all files at this interval
            print(filename)

    return None
            

if __name__ == "__main__":
    # acquire data structure of relationships
    seq = bp.sequence_list
    # batch parse data structure
    b = bp.BatchSequenceParser(seq)
    # create Sequence objects and process relationships
    b.create_sequence_objects()
    b.determine_relationships()
    b.merge_sequence_lists()
    b.conjoin_close_intervals()
    # print(b.conjoined_sequence_list)

    print_char_in_sequence(b.conjoined_sequence_list)
