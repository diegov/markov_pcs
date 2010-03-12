from collections import defaultdict

class Pcs(defaultdict):
    def __init__(self):
        defaultdict.__init__(self, int)

    def is_superset_of(self, other_pcs):
        #unfold dict
        for k in other_pcs.keys():
            if not self.has_key(k): return False
            if self[k] < other_pcs[k]: return False

        return True

    def __hash__(self):
        if len(self) == 0: return 0

        val = 0
        keys = []
        keys.extend(self.keys())
        keys.sort()
        for k in keys:
            val = (hash(k) + hash(self[k])) + (37 * val)
        return val

#    def __eq__(self, other):
#        return defaultdict.__eq__(self, other)

#    def __ne__(self, other):
#        return defaultdict.__ne__(self, other)

    def __sub__(self, other):
        new_val = Pcs()
        for k in self.keys():
            new_val[k] = self[k]
        
        for k2 in other.keys():
            new_val[k2] = new_val[k2] - other[k2] 
            if new_val[k2] == 0: del(new_val[k2])

        return new_val

    #TODO: Override set method to automatically remove keys if 
    #the value is 0
                
    
    
