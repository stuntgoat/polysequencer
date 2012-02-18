from sequence_generator import Sequence

class BatchSequenceParser(object):
    """Accepts a list of dicts and return a list of Sequence objects that 
    are have calculated their sequence intervals based on their relationships
    with eachother."""
    def __init__(self, object_list):
        self.object_list = object_list
        self.sequence_list = []
        self.processed_sequence = []
        self.sorted_merged_intervals = []
        self.conjoined_sequence = []

    def create_sequence_objects(self):
        for item in self.object_list:
            seq = Sequence(parent_name=item['parent'], 
                           relation=item['relation'],
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
                if not seq.parent_name: # root parent
                    seq.process_relationship(None) # determines interval and duration from passed variables
                    seq.generate_sequence()
                    return self.sequence_list.index(seq)
            # TODO: raise exception??? there is no root parent
            return None
                
        def parse_child(child):
            for item in completed_sequence_list:
                if child.parent_name == item.alias:
                    child.parent_object = item
                    child.process_relationship(item)
                    child.generate_sequence()
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
                    if not processed_child:
                        self.sequence_list.append(next_child)
                    else:
                        completed_sequence_list.append(processed_child)
            return None

        root_parent_index = index_of_root_parent()
        completed_sequence_list.append(self.sequence_list.pop(root_parent_index))
        process_children()
        self.processed_sequence = completed_sequence_list
        return None

    def merge_sequence_lists(self):
        """merges each Sequence objects interval_filename_tuple_list and 
        sorts by intervals of each pulse from beginning of sequence;
        Returns: self.sorted_merged_intervals."""
        placeholder_list = []
        # join all lists in the sequence
        for seq in self.processed_sequence:
            # print("processed a sequence object: %s" % seq.filename)
            placeholder_list.extend(seq.interval_list)
        # sort by interval
        self.sorted_merged_intervals = sorted(placeholder_list)
        return self.sorted_merged_intervals

    def _conjoin_tuples(self, candidate_tuple, tuple_list, finished_list):
        """recursively iterate through tuple_list to compare the difference
        of the candidate_tuple's first element(the interval). If the interval difference 
        is < .00035, extend the file list in the second element of the candidate_tuple
        to include the filename of the next element. After conjoining all elements, return
        finished_list"""
        if not tuple_list:
            return finished_list
        next_element = tuple_list.pop(0)
        # if next 2 intervals' difference is less than .00035
        threshold = abs(candidate_tuple[0] - next_element[0])
        if ((threshold < .00035) or (threshold == 0)):
            # conjoin tuples and call conjoin_tuples
            candidate_tuple[1].extend(next_element[1])
            return self._conjoin_tuples(candidate_tuple, tuple_list, finished_list)

        finished_list.append(candidate_tuple)
        # call conjoin_tuples
        return self._conjoin_tuples(next_element, tuple_list, finished_list)
        

    def conjoin_close_intervals(self):
        """conjoin tuples within merged list such that all adjancent tuples with intervals < .00035 seconds
        are merged into a single pulse tuple that contains a list of file_name strings to 'play' at
        the same pulse event.
        A tuple within a_list: (1.2, 'filename')
        Returns: a list of conjoined tuples; a tuple within this returned list: (1.2, ('filename', 'filename2'))
        """
        tuple_list_with_pathname_inside_list = [(x, [y]) for x, y in self.sorted_merged_intervals]
        # print(tuple_list_with_pathname_inside_list)
        first_tuple = tuple_list_with_pathname_inside_list.pop(0)
        # create attribute for conjoined list
        self.conjoined_sequence = self._conjoin_tuples(first_tuple, tuple_list_with_pathname_inside_list, [])
        return self.conjoined_sequence

