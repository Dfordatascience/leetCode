# Question - you have the following log_files get the latest modified date time

log_files = {
    "log1_20240612.txt": "12-12-2024 10:15:00",
    "log2_20240614.txt": "12-12-2024 10:15:00",
    "log3_20240613.txt": "28-11-2024 12:45:00"
}

#########################################
# data = {"a": 10, "b": 25, "c": 15}
# Get the Maximum Value
# max_value = max(data.values())
# print(max_value)


# max_key = max(data, key=data.get)
# print(max_key)  # Output: "b"


##########################################


#Answert

from datetime import datetime

log_files = {
    "log1_20240612.txt": "12-12-2024 10:15:00",
    "log2_20240614.txt": "12-11-2024 10:15:00",
    "log3_20240613.txt": "28-11-2024 12:45:00"
}

# Convert string timestamps to datetime objects
log_files_datetime = {k: datetime.strptime(v, "%d-%m-%Y %H:%M:%S") for k, v in log_files.items()}

# Get the log file with the latest modification time
latest_log = max(log_files_datetime, key=log_files_datetime.get)

print("Latest modified log file:", latest_log)
