# author: j bates

I downloaded 1Q2016 device event data from openFDA.
These are zipped json files.
After extracting, I ran the python code extract_device_event_data.py
to read part of one of the json files, keep some of the metadata and text
and write this to a pickle file.  To get extract_device_event_data.py to 
work on your machine, you need to modify the DIR variable in extract_device_event_data.py
to the directory you want to use.
As an example for reading the data in the pickle file, 
see test_lda.py.  Again, you will need to modify DIR variable.