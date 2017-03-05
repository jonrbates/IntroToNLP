# -*- coding: utf-8 -*-
"""
First, get json file of device adverse events https://open.fda.gov/device/
e.g. http://download.open.fda.gov/device/event/2016q1/device-event-0001-of-0002.json.zip
Second, run the following.
"""

import os
DIR = r'C:\Users\Jonathan\Desktop\Projects\IntroToNLP\device_events'

import json
fname = os.path.join(DIR,r'device-event-0001-of-0002.json\device-event-0001-of-0002.json')
d = json.load(open(fname))
    
nmax = 10000
data = list()
for x in d['results']:  
    try:
        device_category = x.get('device')[0].get('generic_name')
    except IndexError:
        device_category = None
    data.extend({'adverse_event_flag': x.get('adverse_event_flag'),
                 'device_generic_name': device_category,
                 'event_type': x.get('event_type'),
                 'narrative': k.get('text')}
                     for k in x.get('mdr_text') 
                     if k.get('text_type_code') 
                     == 'Description of Event or Problem')
    if len(data)>nmax:
        break

import pickle
pkl_name = os.path.join(DIR, r'open_fda_device_event_data.pkl')
pickle.dump(data, open(pkl_name, "wb"))




