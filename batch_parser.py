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
        self.sorted_merged_interval_filename_list = []

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
                    seq.process_relationship(None) # determines interval and duration from passed variables
                    seq.create_interval_filename_tuple_list()
                    return self.sequence_list.index(seq)
            # TODO: raise exception??? there is no root parent
            return None
                
        def parse_child(child):
            for item in completed_sequence_list:
                if child.parent_name == item.alias:
                    child.parent_object = item
                    child.process_relationship(item)
                    child.create_interval_filename_tuple_list()
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

            return None

        root_parent_index = index_of_root_parent()
        completed_sequence_list.append(self.sequence_list.pop(root_parent_index))
        process_children()
        self.processed_sequence_list = completed_sequence_list

        return None

    def merge_sequence_lists(self):
        """merges each Sequence objects interval_filename_tuple_list and 
        sorts by intervals of each pulse from beginning of sequence;
        Returns: self.sorted_merged_interval_filename_list."""
        placeholder_list = []
        # join all lists in the sequence
        for seq in self.processed_sequence_list:
            print("processed a sequence object: %s" % seq.filename)
            placeholder_list.extend(seq.interval_filename_tuple_list)
        # sort by interval
        self.sorted_merged_interval_filename_list = sorted(placeholder_list)
        return self.sorted_merged_interval_filename_list
        


    # return a list of all lists merged and sorted by duration from beginning of sequence
    # def merge_lists(self)


if __name__ == "__main__":
    b = BatchSequenceParser(sequence_list)
    b.create_sequence_objects()
    b.determine_relationships()
    b.merge_sequence_lists()
    print(b.sorted_merged_interval_filename_list)
