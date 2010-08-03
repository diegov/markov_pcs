class Bucket:
    """
    A class that can hold counts of occurrences for each key. 
    It will then return normalised weights of each key.
    """

    def __init__(self):
        self._values = {}
        self._weights = None
      
    def __getitem__(self, key):
        return self._values[key]
    
    def __setitem__(self, key, value):
        #We do this to avoid invalidating the 
        #calculated weights
        if self._values.has_key(key):
            curr = self._values[key]
            if curr == value:
                return value
        
        self._values[key] = value
        self._weights = None
        return value

    def keys(self):
        return self._values.keys

    def has_key(self, key):
        return self._values.has_key(key)

    @property
    def weights(self):
        if self._weights == None:
            self._weights = self._calculate_weights()
        return self._weights

    def _calculate_weights(self):
        total = 0.0
        for v in self._values.keys():
            total += self._values[v]

        result = {}
        for v in self._values.keys():
            result[v] = self._values[v] / total

        return result

    def __repr__(self):
        return "Bucket: " + str(self._values)
