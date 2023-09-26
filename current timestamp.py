import datetime

def write_timestamp_to_file(filename):
    
    current_time = datetime.datetime.now()
    
    
    timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    
    with open(filename, 'w') as file:
        file.write(timestamp_str)

