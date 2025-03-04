class Player:
    def __init__(self, uid, name):
        self._uid = uid
        self._name = name

    def __str__(self):
        return f"location: {id(self)}, uid: {self._uid}, name: {self._name}"

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name
