# Music Metadata Formatter

This Python code consists of two scripts, "Formatter.py" and "categorize.py", which take a JSON file containing music metadata and transform it into a specific format with modified keys and values, and split the data into new key-values.

## Features

### Formatter.py

The Formatter.py script does the following:

- Converts all keys to lowercase.
- Removes spaces and "#" characters from keys.
- Modifies certain keys to fit the desired format.
- Modifies certain values to fit the desired format.
- Saves the modified data to a new JSON file.

### Categorize.py

The categorize.py script does the following:

- Rearranges the data to have new keys named metadata, info, genre, key, relatedartist, mood, arrangement, instruments, sample, creator, and exclusive.
- Splits certain keys to create nested values.
- Converts the exclusive key's value to boolean.
- Saves the modified data to a new JSON file.

## Requirements

- .csv in specific format
- csvjson
- Python 3.x
- JSON module

## Usage

1. Save the music metadata in a JSON file.
2. Run the "Formatter.py" script by typing python Formatter.py in the terminal or command prompt.
3. The modified data will be saved in a new JSON file named "output.json".
4. Run the "categorize.py" script by typing python categorize.py in the terminal or command prompt.
5. The final modified data will be saved in a new JSON file named "output2.json".

## Spreadsheet to JSON

Before running our code, you'll need to have Node.js and npm installed on your computer. You'll also need to install the csvjson and prettier npm packages by running the following commands in your terminal:

- Copy code
- npm install csvjson
- npm install prettier
- Once you have those packages installed, you can follow these steps to convert your Spreadsheet data into a formatted JSON file:
- Export your Spreadsheet data as a CSV file.
- Install csvjson npm package by running the command mentioned above.
- Convert the CSV file into JSON using csvjson by running the following command

## Example Input

```
  {
    "Notes": null,
    "Catalog": "CRB001",
    "ISRC": "QZK6Q2167820 ",
    "ISWC": "T-930.805.700-3",
    "Title": "Enemy",
    "Release": "6/1/2018",
    "Album": "Cashrollie Beats, Vol. 1",
    "Track #": 1.0,
    "Producer": "Meekah",
    "Duration": "0:03:25",
    "BPM": 75.0,
    "Note": "E",
    "Scale": "minor",
    "Genre 1": "Hiphop",
    "Subgenre 1": null,
    "Genre 2": null,
    "Subgenre 2": null,
    "Related Artist 1": "Drake",
    "Related Artist 2": "Blocboy JB",
    "Related Artist 3": null,
    "Mood 1": "Dirty",
    "Mood 2": "Energetic",
    "Mood 3": "Evil",
    "Energy": null,
    "Color": null,
    "Character": null,
    "Section 1": "Intro",
    "Time": "0:00:00",
    "Section 2": "Chorus 1",
    "Time_2": "0:00:13",
    "Section 3": "Verse 1",
    "Time_3": "0:00:40",
    "Section 4": "Pre-Chorus 1",
    "Time_4": "0:00:56",
    "Section 5": "Chorus 2",
    "Time_5": "0:01:08",
    "Section 6": "Verse 2",
    "Time_6": "0:01:36",
    "Section 7": "Pre-Chorus 2",
    "Time_7": "0:02:03",
    "Section 8": "Chorus 2",
    "Time_8": "0:02:30",
    "Section 9": "Outro",
    "Time_9": "0:02:58",
    "Section 10": null,
    "Time_10": null,
    "Chord Progression": null,
    "Instrument 1": "Drum",
    "Sub Category 1": "Analog",
    "Instrument 2": "Percussion",
    "Sub Category 2": "Analog",
    "Instrument 3": "Keyboard",
    "Sub Category 3": "Rhodes",
    "Instrument 4": "Synth",
    "Sub Category 4": null,
    "Instrument 5": null,
    "Sub Category 5": null,
    "Sample File": "BPM070TrapMan_Em_Piano / Bedroom Beats & Lofi Hip-Hop Vol. 2",
    "Sample Pack": "Bedroom Beats & Lofi Hip-Hop Vol. 2 / Dirty South Wars 2",
    "Author": "Prime Loops",
    "Clearance": "royalty-free",
    "Collaborator": true,
    "Name 1": "AHN ABRAHAM JOONGWHAN",
    "Producer_2": true,
    "Songwriter": true,
    "IPI": 789929253.0,
    "Splits": 100.0,
    "Name 2": null,
    "Producer_3": null,
    "Songwriter_2": null,
    "IPI_2": null,
    "Splits_2": null,
    "Publisher": "Songtrust",
    "Exclusive": "Available",
    "Artist Name": null,
    "Email": null,
    "Phone": null,
    "Address": null,
    "Management": null
  }
```

## Example Output

    {
        "id": 1,
        "file": "CRB001_Enemy_Tag.mp3",
        "metadata": {
            "catalog": "CRB001",
            "isrc": "QZK6Q2167820 ",
            "iswc": "T-930.805.700-3",
            "title": "Enemy",
            "release": "6/1/2018",
            "album": "Cashrollie Beats, Vol. 1",
            "track#": "1",
            "producer": "Meekah"
        },
        "info": {
            "duration": "0:03:25",
            "bpm": "75",
            "key": {
                "note": "E",
                "scale": "minor"
            },
            "genre": {
                "1": {
                    "maingenre": "Hiphop",
                    "subgenre": ""
                },
                "2": {
                    "maingenre": "",
                    "subgenre": ""
                }
            },
            "relatedartist": {
                "1": "Drake",
                "2": "Blocboy JB",
                "3": ""
            },
            "mood": {
                "mood1": "Dirty",
                "mood2": "Energetic",
                "mood3": "Evil",
                "energy": "",
                "color": "",
                "character": ""
            }
        },
        "arrangement": {
            "1": {
                "time1": "0:00:00",
                "section1": "Intro"
            },
            "2": {
                "time2": "0:00:13",
                "section2": "Chorus 1"
            },
            "3": {
                "time3": "0:00:40",
                "section3": "Verse 1"
            },
            "4": {
                "time4": "0:00:56",
                "section4": "Pre-Chorus 1"
            },
            "5": {
                "time5": "0:01:08",
                "section5": "Chorus 2"
            },
            "6": {
                "time6": "0:01:36",
                "section6": "Verse 2"
            },
            "7": {
                "time7": "0:02:03",
                "section7": "Pre-Chorus 2"
            },
            "8": {
                "time8": "0:02:30",
                "section8": "Chorus 2"
            },
            "9": {
                "time9": "0:02:58",
                "section9": "Outro"
            },
            "10": {
                "time10": "",
                "section10": ""
            }
        },
        "instruments": {
            "1": {
                "main-category": "Drum",
                "sub-category": "Analog"
            },
            "2": {
                "main-category": "Percussion",
                "sub-category": "Analog"
            },
            "3": {
                "main-category": "Keyboard",
                "sub-category": "Rhodes"
            },
            "4": {
                "main-category": "Synth",
                "sub-category": ""
            },
            "5": {
                "main-category": "",
                "sub-category": ""
            }
        },
        "sample": {
            "file": "BPM070TrapMan_Em_Piano / Bedroom Beats & Lofi Hip-Hop Vol. 2",
            "samplepack": "Bedroom Beats & Lofi Hip-Hop Vol. 2 / Dirty South Wars 2",
            "author": "Prime Loops",
            "clearance": "royalty-free"
        },
        "creator": {
            "1": {
                "name": "AHN ABRAHAM JOONGWHAN",
                "producer": true,
                "songwriter": true,
                "ipi": "789929253",
                "splits": "100"
            },
            "2": {
                "name": "",
                "producer": "",
                "songwriter": "",
                "ipi": "",
                "splits": ""
            }
        },
        "exclusive": {
            "artistname": "",
            "email": "",
            "phone": "",
            "address": "",
            "management": ""
        }
    }
```
