#!/bin/bash

mosquitto_sub -t 'scale/records' | mongoimport -d scale -c records

