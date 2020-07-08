from datetime import datetime
from typing import Dict
import json

class Data:
    string: str
    numeric: float
    datetime: datetime

   

class Response:
    source: str
    timestamp: datetime
    data: Dict
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


