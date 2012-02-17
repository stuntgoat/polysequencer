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
        print(interval)
        for filename in item[1]: # print all files at this interval
            print(filename)

    return None
            

if __name__ == "__main__":
    # acquire data structure of relationships
    seq = bp.sequence_list
    # print seq
    # batch parse data structure
    b = bp.BatchSequenceParser(seq)
    # create Sequence objects and process relationships
    b.create_sequence_objects()
    b.determine_relationships()
    b.merge_sequence_lists()
    b.conjoin_close_intervals()
    # tuple_list_to_print = conjoin_close_intervals(b.sorted_merged_interval_filename_list)
    print(b.conjoined_sequence_list)

    print_char_in_sequence(b.conjoined_sequence_list)

# def conjoin_tuples(candidate_tuple, tuple_list, finished_list):
#     """recursively iterate through tuple_list to compare the difference
#     of the candidate_tuple's first element. after conjoining all elements, return
#     finished_list"""
#     if not tuple_list:
#         return finished_list
#     next_element = tuple_list.pop(0)
#     # if next 2 intervals' difference is less than .00035
#     threshold = abs(candidate_tuple[0] - next_element[0])
#     if ((threshold < .00035) or (threshold == 0)):
#         # conjoin tuples and call conjoin_tuples
#         candidate_tuple[1].extend(next_element[1])
#         return conjoin_tuples(candidate_tuple, tuple_list, finished_list)
#     else: # append candidate_tuple to finished_list
#         finished_list.append(candidate_tuple)
#         # call conjoin_tuples
#         return conjoin_tuples(next_element, tuple_list, finished_list)
#     return None

# def conjoin_close_intervals(tuple_list):
#     """conjoin tuples within merged list such that all adjancent tuples with intervals < .00035 seconds
#     are merged into a single pulse tuple that contains a list of file_name strings to 'play'.
#     A tuple within a_list: (1.2, 'filename')
#     Returns: a list of conjoined tuples; a tuple within this returned list: (1.2, ('filename', 'filename2'))
#     """
#     tuple_list_with_pathname_inside_list = [(x, [y]) for x, y in tuple_list]
#     # print(tuple_list_with_pathname_inside_list)
#     first_tuple = tuple_list_with_pathname_inside_list.pop(0)
#     return conjoin_tuples(first_tuple, tuple_list_with_pathname_inside_list, [])
