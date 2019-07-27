class ScaleRecord:
    scales = {1 : 5.15,
              2 : 4.88,
              3 : 5.28,
              4 : 4.88}

    def __init__(self, scale_id, high_byte, low_byte):
        self.scale_id = scale_id
        self.high_byte = high_byte
        self.low_byte = low_byte

    def getWeight(self):
        weight = ((ord(chr(self.high_byte)) * 256 + ord(chr(self.low_byte))) / 10.0)
        weight = weight / self.scales[self.scale_id]

        return format(weight, '.1f')

