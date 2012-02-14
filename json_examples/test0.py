
"""
A polyrhythmic sample sequencer.

   The sequencer accepts JSON objects that determine the following:
   - the parent sequence thread to synchronize with: 
     "parent": ( "<sequence alias name>" || "root" )

     (if this sequence does not have a parent sequence, it is the root and no other sequence
     can be root)

   - the pathname of the sample audio on disk to play: "audio_filename": "./relative/or/absolute/path.aiff"

   - an alais for the sequence: 
     "alias": "snare"

   - the ratio of the number of pulses to play in relation to the number parent pulses: 
     "relation": {"parent": 3, "self": 5} # play 5 pulses for every 3 pulses of the parent
"""


json_data = """
[
{
    "parent": null,
    "audio_filename": "root_parent_file_name",
    "alias": "one",
    "relation": null,
    "bpm": 60,
    "duration":25
},
{
    "parent": "one",
    "audio_filename": "child_file_name",
    "alias": "two",
    "relation": 
    {
	"parent":4,
	"self": 5
    },
    "duration": null,
    "bpm": null
},
{
    "parent": "two",
    "audio_filename": "grand_child_file_name",
    "alias": "three",
    "relation": 
    {
	"parent":4,
	"self": 5
    },
    "duration": null,
    "bpm": null
}
]"""
