#!/usr/bin/env python3

# Generate some fake temperature data for us to use for plotting
# in jupyter using pandas and matplotlib
# CTB Fri Jul 20 09:34:57 SAST 2018
# TODO: Add headers to the CSV before importing into numpy

from datetime import datetime, timedelta
import csv
import random

start = datetime(2016, 11, 11, 0, 0, 0)
t = start

with open("data.csv", "w") as csvfile:
    datawriter = csv.writer(csvfile)
    for i in range(0, 100000):
        t = t  + timedelta(seconds=600)
        datawriter.writerow([t, random.randint(0, 45)])
