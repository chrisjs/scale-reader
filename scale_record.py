class ScaleRecord:
    scales = {1 : 5.15,
              2 : 5.43,
              3 : 4.97,
              4 : 5.18}

    def __init__(self, scale_id, high_byte, low_byte):
        self.scale_id = scale_id
        self.high_byte = high_byte
        self.low_byte = low_byte

    def getWeight(self):
        weight = ((ord(chr(self.high_byte)) * 256 + ord(chr(self.low_byte))) / 10.0)
        weight = weight / self.scales[self.scale_id]
        weight = weight * 2.204623

        return format(weight, '.1f')

