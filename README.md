# input-normalizer

The input normalizer normalizes input that is POSTed to the `/input` endpoint.

The following must always be present in the payload:
```
source: string
timestamp: ISO date
```
Plus any additional number of fields.

The endpoint will return the source string, data timestamp (as milliseconds from UNIX epoch), and any additional data fields submitted. It will attempt to parse each input value in the following three waysL
* String: a string representation of the input value
* Numeric: a float representation of the input value (or null if it cannot be parsed). 
* DateTime: if the input value is an ISO datetime string, the output is milliseconds from the UNIX epoch for that datetime. If the input value is numeric (integer or float), this is interpreted as UNIX time in seconds and the value returned is UNIX time in milliseconds. Otherwise, the value is null.

## Running the input normalizer

Prerequisites:
* Python 3
* flask module

Run the application with `python -m flask run` from the `/app` directory.