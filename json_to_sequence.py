from sequence_generator import Sequence
import json
from json_examples import test0

# de-serialize json_data
sequence_list = json.loads(test0.json_data)

# print(sequence_list)

class BatchSequenceParser(object):
    """Accepts a list of dicts and return a list of Sequence objects that 
    are have calculated their sequence intervals based on their relationships
    with eachother."""
    
    def __init__(self, object_list):
        self.object_list = object_list
        



# def sequence_objects_from_sequence_dicts(list_of_sequence_dicts):
#     sequence_object_list = []

#     for item in list_of_sequence_dicts:
        
#         seq = Sequence(
    





