import os
import json

FILE_PATH = "/tmp/drive_data.json"

def save_drive_data(drive_data):
    with open(FILE_PATH, 'w') as f:
        json.dump(drive_data, f, indent=4)

def get_drive_data(status):
    if not os.path.exists(FILE_PATH):
        return {"message": f"No drives found with status '{status}'", "data": []}

    with open(FILE_PATH, 'r') as f:
        drive_data = json.load(f)

    filtered_drives = []
    for drive, details in drive_data.items():
        details_dict = {kv.split()[0]: kv.split()[1] for kv in details.split(",")}
        if details_dict.get("status", "").lower() == status.lower():
            disk_list = details_dict["disks"].split(" ")
            details_dict["disks"] = disk_list
            details_dict["size"] += " MB"
            details_dict["free"] += " MB"
            details_dict["log"] += " MB"
            details_dict["port"] = int(details_dict["port"])
            details_dict["dare"] = int(details_dict["dare"])
            filtered_drives.append(details_dict)

    if not filtered_drives:
        return {"message": f"No drives found with status '{status}'", "data": []}

    return {"message": f"Found {len(filtered_drives)} {status} drives", "data": filtered_drives}

get_drive_data("Online")
