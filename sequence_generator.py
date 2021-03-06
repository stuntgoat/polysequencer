
class Sequence(object):
    """If instantiated with a parent sequence, bpm will be none and 
    a relation_dict will be in the format: {'parent': 4, 'self': 5};
    duration is the total count of pulses
    interval is the duration between pulses
    alias is a string name for this sequence

    If parent == None, self is a root parent; bpm must
    be > 0; relation must == None
    """
    
    def __init__(self, parent_name=None, relation={}, bpm=0, duration=0, file_name='', alias=""):
        """duration is the total times the sequence will pulse"""
        self.parent_name = parent_name
        self.bpm = bpm
        self.relation = relation
        self.duration = duration 
        self.interval = 0 # calculate interval between each pulse
        self.timing_list = [0]
        self.filename = file_name
        self.parent_object = None
        self.alias = alias
        self.interval_list = []

    def calculate_interval(self):
        """ Root parents caclulate duration from self.bpm; 
        children calculate duration based on relationship to parent"""
        if not self.parent_object:
            self.interval = 60.0/self.bpm
            return self.interval
        # interval is (self.relation["parent"] * self.parent.duration) / self.relation["self"]
        self.interval = ((self.relation["parent"] * self.parent_object.interval) / self.relation["self"])
        return self.interval

    def calculate_duration(self):
        """If not duration, play until the end of the parents sequence; otherwise, play for
        duration pulses"""
        if self.parent_object: # instance has a parent
            parent_total_time = self.parent_object.interval * self.parent_object.duration
            self.duration = int(parent_total_time / self.interval)
        return self.duration

    def calculate_timing_list(self):
        """Calculate timing as list of incrementing sum of durations"""
        duration_sum = 0
        # Try: if not duration, raise exception
        for pulse in xrange(self.duration):
            duration_sum += self.interval
            self.timing_list.append(duration_sum)
        return self.timing_list
    
    def process_relationship(self, parent_object): 
        """after the self.parent_object is set, determine the interval and duration for
        self.timing_list; if no parent is assigned calculate interval from self.bpm; if
        self.bpm is given, self.duration must also be set"""
        self.parent_object = parent_object
        self.calculate_interval()
        self.calculate_duration()
        self.calculate_timing_list()
        return None

    def generate_sequence(self):
        """creates a tuple for each Sequence object's timing_list, containing the 
        interval and the filename to play"""
        self.interval_list = [(interval, self.filename) for interval in self.timing_list]
        return self.interval_list


        
