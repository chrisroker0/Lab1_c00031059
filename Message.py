from datetime import datetime as dt
import json
import csv


class Message:
    incoming_message = ""
    dtm_created = dt.now()

    def __init__(self, message, dtm_created):
        self.incoming_message = message
        self.DtmCreated = dtm_created

    def convert_to_json(self):
        json_message = {
            "message": self.incoming_message,
            "dtm_created": self.dtm_created
        }
        loaded_message = json.dumps(json_message, indent=4, sort_keys=True, default=str)
        return loaded_message


