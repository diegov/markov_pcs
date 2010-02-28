class ModalGroup:
    def __init__(self, octave_division):
        self._octave_division = octave_division
        self._intval_table = []
        self._notes = []
        self._note_group = None
        self._initd = False
        self._intval_override = False

