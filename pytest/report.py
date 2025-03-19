import json

def generate_report():
    #generate report data
    dt = {
        "timestamp": "2023-4-27 12-37-9",
        "status": "PASSERD",
        "summary": "module.py::test_case"
    }
    #open json
    #in writing mode
    with open("report.json", "w") as file:
        #write data to json file
        json.dump(dt, file)