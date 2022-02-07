""" this is a function that can be used to evaluate the
magnitude cvr factors for active power in a grid"""

import numpy as np

class CVREvaluator():
    
    def __init__(self, voltages, power, window=0, tap_duration=0):
        self.voltages = voltages
        self.power = power
        self.window
        self.tap_duration
        
    # evaluate the percentage change in voltages
    def voltage_change(self, time_of_day):
        gap = time_of_day + tap_duration
        start = time_of_day - window
        finish = gap + window
        
        # get the averaging interval using a known point and
        # specified interval
        before_index = self.voltages[start:self.time_of_day]
        after_index = self.voltages[gap:finish]
        
        change_before = np.mean(before_index)
        change_after = np.mean(after_index)
        percentage_voltage_change = ((change_before - change_after)/change_before)*100
        
        return percentage_voltage_change
    
    # evaluate the percentage change in power
    def power_change(self, time_of_day):
        gap = time_of_day * self.tap_duration
        start = time_of_day - window
        finish = gap + window
        
        # get the averaging interval using a known point and
        # specified interval
        before_index = self.power[start:self.time_of_day]
        after_index = self.power[gap:finish]
        
        change_before = np.mean(before_index)
        change_after = np.mean(after_index)
        power_change = change_before - change_after
        if change_before < 0:
            percentage_power_change = (power_change/abs(change_before))*100
        else:
            percentage_power_change = (power_change/change_before)*100
        
        return percentage_power_change
        
    # estimating CVR factor for power using the direct method.
    # other methods can also be applied
    def cvr_factor(self, time_of_day):
        volt = voltage_change(time_of_day)
        power = power_change(time_of_day)
        
        cvr = power/volt
        return cvr
    
    # gather the cvr factors estimated from percentage voltage change
    # and percentage power change
    def cvr_evaluator(self, time_group):
        cvr_value = []
        for i in time_group:
            cvr = cvr_factor(i)
            cvr_value.append(round(cvr, 4))
        return cvr_value
        
    # apply a first stage filter to remove ouliers from the list
    def first_filter(self, cvr_factors, max=0, min=0):
        filter_values = []
        for j in cvr_factors:
            if j > min and j < max:
                filter_values.append(j)
        return filter_values
        