class Player:
    def __init__(self, uid, name):
        self._uid = str(uid)
        self._name = name

    def __str__(self):
        return f"location: {id(self)}, uid: {self._uid}, name: {self._name}"

    def display(self):
        return f"Player '{self._uid}': {self._name}"

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name
    
    @classmethod
    def hash(cls, key: str) -> int:
        key = str(key)
        hash_val = 5381  # DJB2 initial value
        for char in key:
            hash_val = (hash_val * 33) + ord(char)
        return hash_val
    
    def __hash__(self):
        return self.hash(self.uid)

    def __eq__(self, other):
        return self.uid == other.uid