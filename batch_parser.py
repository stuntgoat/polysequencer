from sequence_generator import Sequence
import json
from json_examples import test0

## remove!!!
# de-serialize json_data
sequence_list = json.loads(test0.json_data)
###


class BatchSequenceParser(object):
    """Accepts a list of dicts and return a list of Sequence objects that 
    are have calculated their sequence intervals based on their relationships
    with eachother."""
    
    def __init__(self, object_list):
        self.object_list = object_list
        self.sequence_list = []
        self.processed_sequence_list = []

    def create_sequence_objects(self):
        for item in self.object_list:
            seq = Sequence(parent_name=item['parent'], 
                           relation_dict=item['relation'],
                           bpm=item['bpm'],
                           duration=item['duration'],
                           file_name=item['audio_filename'],
                           alias=item['alias'])
            self.sequence_list.append(seq)
        return self.sequence_list

    def determine_relationships(self):
        # acquire root parent sequence
        completed_sequence_list = []        

        def index_of_root_parent():
            for seq in self.sequence_list:
                if seq.parent_name == None: # root parent
                    seq.process(None) # determines interval and duration from passed variables
                    return self.sequence_list.index(seq)
                
        def parse_child(child):
            for item in completed_sequence_list:
                if child.parent_name == item.alias:
                    child.parent_object = item
                    child.process(item)
                    return child
            return None
            
        def process_children():
            """TODO: iterate over range(pow(self.sequence_list, 2)) to check
            that there was no unassigned parent; also, if self.sequence_list is
            empty, return, since the list is empty"""
            

            for count in range(len(self.sequence_list)):
                if not self.sequence_list:
                    return completed_sequence_list
                for item in self.sequence_list:
                    next_child = self.sequence_list.pop(0)
                    processed_child = parse_child(next_child)
                    if processed_child == None:
                        self.sequence_list.append(next_child)
                    else:
                        completed_sequence_list.append(processed_child)
                
                
            # while len(self.sequence_list) != 0:
            #     for item in self.sequence_list:
            #         next_child = self.sequence_list.pop(0)
            #         processed_child = parse_child(next_child)
            #         if processed_child == None:
            #             self.sequence_list.append(next_child)
            #         else:
            #             completed_sequence_list.append(processed_child)

            return completed_sequence_list
        root_parent_index = index_of_root_parent()
        completed_sequence_list.append(self.sequence_list.pop(root_parent_index))
        process_children()
        self.processed_sequence_list = completed_sequence_list
        return None

    
    
    # return a list of all lists merged and sorted by duration from beginning of sequence
    # def merge_lists(self)


if __name__ == "__main__":
    b = BatchSequenceParser(sequence_list)
    b.create_sequence_objects()
    b.determine_relationships()
    for seq in b.processed_sequence_list:
        print(seq.timing_list)
