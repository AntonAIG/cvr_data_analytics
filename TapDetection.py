"""
This is a script that contains all the neccessary functions in the CVR project:
tap change detection
CVR factor computation.
See the repo description"""

import numpy as np
import datetime as datetime

class TapDetection():
    def __init__ (self, voltages, nominal_voltage, perc_treshold=0, average_interval=0):
        self.voltages = voltages    # a list of voltage measurements
        self.perc_treshold  # value of percentage voltage limit
        self.nominal_voltage = nominal_voltage
        self.average_interval
    
    # estimating the voltage limits
    def threshold_violation(self):
        violation_index = [] # list of indices from the voltage list
        for i in range(len(self.voltages)):
            if self.voltages[i] < (self.nominal_voltage - (self.nominal_voltage*self.perc_treshold)): # percentage change
                violation_index.append(i)
            else:
                i+=1
        return violation_index
    
    # estimating the hour value in a datetime using the timestamp column from a dataframe
    # correspoding to the selected indices of the tap positions
    def datetime_to_hour(self, voltage_index):
        time_of_day = datetime.datetime(voltage_index)
        
        return time_of_day.hour
    
    # calculating voltage change of a given dataset
    def delta_u_index(self, tap_duration=None, min_delta=None):
        
        #stores the indices of the tap changes
        delta_index = []
        for u in range(len(self.voltages) - tap_duration):
            a = abs(self.voltages[u] - self.voltages[u+(tap_duration-1)])   # tap change magnitude 1
            b = abs(self.voltages[u+1] - self.voltages[self.voltages + (tap_duration+1)])   # tap change magnitude 2
            
            #compare with the neighbouring points to see which is bigger
            if a > min_delta or b > min_delta:
                if a > b:
                    delta_index.append(u)
                else:
                    delta_index.append(u+1)
            else:
                u+=1
        return delta_index
    
    
    """ in cases where there are multiple phases with similar load
    tap changes are expected to occure simultaneously on all the phases.
    Let's check for this condition here. And if there is, let's select that index position"""
    def combined_index(self, alist, blist, clist):
    
        # collects the three voltage phases
        a = set(alist)
        b = set(blist)
        c = set(clist)
        merged_list = a + b + c # merge all phases together
        remove_index = []
        
        for i in range(len(merged_list) -1):
            if merged_list[i] == merged_list[i+1]:  # checks for duplicates
            remove_index.append(i+1)
            else:
                i+=1
        # checks the back and forward indices for duplicates
        for k in range(len(merged_list) -1):
            ch = abs(merged_index[k] - merged_index[k+1]
            if ch < self.average_interval:
                remove_index.append(k+1)
            else:
                k+=1
        for j in sorted(remove_index, reverse=True):
            del merged_index[j]
            
        return merged_index
    
    """ grouping the indices with respect to their time of day
    the datetime_to_hour() fuction will collect the time measurements and group them.
    """
    def time_groups(self):
        delta_u = delta_u_index(self.voltages[[merged_index]]):
        grouped_index = sorted(combined_index(delta_u), reverse=False)
        tg1 = []
        tg2 = []
        tg3 = []
        tg4 = []
        for d in grouped_index:
        h = datetime_to_hour(d)
            if h > 22 or h < 4:
                tg2.append(d)
            elif h > 4 and h < 10:
                tg3.append(d)
            elif h > 10 and h < 16:
                tg4.append(d)
            else:
                tg1.append(d)
        return np.array(tg1, tg2, tg3, tg4)