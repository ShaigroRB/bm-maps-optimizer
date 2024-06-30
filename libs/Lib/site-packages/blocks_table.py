class BlocksTable():
    def __init__(self, type: str, sound: str, table: list[list[int]] = None):
        if table is None:
            table = []
        self.type = type
        self.sound = sound
        self.table = list(table)

    def __getitem__(self, item: int):
        return self.table[item]

    def __setitem__(self, key: int, value: int):
        self.table[key] = value

    def __repr__(self):
        return f'Type: {self.type}\n Sound: {self.sound}\n Table: {str(self.table)}\n'
