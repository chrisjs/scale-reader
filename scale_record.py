class ScaleRecord:
    scales = {1 : 2.69,
              2 : 2.69,
              3 : 2.52,
              4 : 2.71}

    def __init__(self, scale_id, high_byte, low_byte):
        self.scale_id = scale_id
        self.high_byte = high_byte
        self.low_byte = low_byte

    def getWeight(self):
        weight = ((ord(chr(self.high_byte)) * 256 + ord(chr(self.low_byte))) / 10.0)
        weight = weight / self.scales[self.scale_id]

        return format(weight, '.1f')

