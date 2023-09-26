import datetime

def create_text_file_with_timestamp():
    
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    
    
    file_name = f"textfile_{current_timestamp}.txt"
    
    
    with open(file_name, "w") as file:
        file.write("This is a text file created with the current timestamp.")
    
    print(f"Text file '{file_name}' created successfully!")



