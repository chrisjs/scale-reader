#!/bin/bash

./scale_reader.py | mosquitto_pub -t scale/records -l 

