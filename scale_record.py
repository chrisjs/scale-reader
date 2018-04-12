class ScaleRecord:
    def __init__(self, scale_id, high_byte, low_byte):
        self.scale_id = scale_id
        self.high_byte = high_byte
        self.low_byte = low_byte

    def getWeight(self):
        return ord(chr(self.high_byte)) * 256 + ord(chr(self.low_byte))
