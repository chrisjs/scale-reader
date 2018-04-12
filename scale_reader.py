#!/usr/bin/python

import os
import json
import time
import serial
import struct

from scale_record import ScaleRecord

BAUD=115200
PORT='/dev/ttyUSB0'

class ScaleReader: 
    def connect(self):
        self.ser = serial.Serial(PORT, BAUD)
        self.__log_debug("Connected to: " + self.ser.name)

    def read_as_json(self):
        while True:
            wakeup = self.__get_wakeup()

            while wakeup is False:
                wakeup = self.__get_wakeup()

            self.__ack_wakeup()
            self.__to_json(self.__get_scale_records())

    def close(self):
        self.ser.close()
        self.__log_debug("Connection to: " + self.ser.name + " closed.")

    def __get_wakeup(self):
        wakeup = self.ser.read(2)

        if wakeup == "SZ":
            self.__log_debug("GOT WAKEUP: " + wakeup)
            return True

        self.__log_debug("WAITING ON WAKEUP..")

        return False 

    def __ack_wakeup(self):
        self.ser.write( b'J' )
        self.__log_debug("ACK SENT")

    def __get_scale_records(self):
        data = self.ser.read(16)
        self.__log_debug("SCALE DATA: " + data + " SIZE: " + str(len(data)))

        format = '1c 1B 1B 1B 1c 1B 1B 1B 1c 1B 1B 1B 1c 1B 1B 1B'
        unpacked = struct.unpack(format, data)

        return [ScaleRecord(unpacked[1], unpacked[2], unpacked[3]),
            ScaleRecord(unpacked[5], unpacked[6], unpacked[7]),
            ScaleRecord(unpacked[9], unpacked[10], unpacked[11]),
            ScaleRecord(unpacked[13], unpacked[14], unpacked[15])]

    def __to_json(self, scale_records):
        json_data = {}
        json_data['timestamp'] = int(time.time()) 

        for scale_record in scale_records:
            scale_id = scale_record.scale_id
            json_data[scale_id] ={}
            json_data[scale_id]['high_byte'] = scale_record.high_byte 
            json_data[scale_id]['low_byte'] = scale_record.low_byte 
            json_data[scale_id]['weight'] = scale_record.getWeight()
    
        print json.dumps(json_data)

    def __log_debug(self, msg):
        if os.environ.get('DEBUG') is not None:
            print msg

if __name__ == '__main__':
    try:
        scale_reader = ScaleReader()
        scale_reader.connect()
        scale_reader.read_as_json()
    finally:
        scale_reader.close()

