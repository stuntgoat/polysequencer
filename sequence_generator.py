from math import floor

class Sequence(object):
    """If instantiated with a parent sequence, bpm will be none and 
    a relation_dict will be in the format: {'parent': 4, 'self': 5}

    If parent == None, self is a root parent; bpm must
    be > 0; relation_dict must == None
    """
    
    def __init__(self, parent, relation_dict, bpm, duration, file_name):
        """duration is the total times the sequence will pulse"""
        self.parent = parent
        self.bpm = bpm
        self.relation = relation_dict
        self.duration = duration 
        self.interval = 0 # calculate interval between each pulse
        self.timing_list = [0]
        self.filename = file_name

    def calculate_duration(self):
        """ Root parents caclulate duration from self.bpm; 
        children calculate duration based on relationship to parent"""
        if parent == None:
            self.interval = 60.0/bpm
            return self.interval
        else:
            # duration is (self.relation["parent"] * self.parent.duration) / self.relation["self"]
            self.interval = ((self.relation["parent"] * self.parent.interval) / self.relation["self"])
            return self.interval

    def calculate_duration(self):
        """If duration == None, play until the end of the parents sequence; otherwise, play for
        duration pulses"""
        if duration == None: # instance has a parent
            parent_total_time = self.parent.interval * self.parent.duration
            self.duration = int(floor(parent_total_time / self.interval))
        else:
            return self.duration

    def calculate_timing_list(self):
        """Calculate timing as list of incrementing sum of durations"""
        duration_sum = 0
        for pulse in xrange(duration):
            duration_sum += self.interval
            self.timing_list.append(duration_sum)
        return self.timing_list
