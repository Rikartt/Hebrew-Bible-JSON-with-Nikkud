# Hebrew-Bible-JSON-with-Nikkud
A single, hebrew bible json with nikkud. 


# Explanation

converter.py is written almost in entirety by ChatGPT, due to this being a side project and a very simple task. Feel free to use the json file in your own bible projects! To summarize, the project contains:
 - A Python script named 'converter.py' that parses thee Westminster-Leningrad Codex OSIS XML files and converts them into a nested JSON structure.
 - The generated JSON file containing the full Hebrew Bible with vowels and trope, organized as Book → Chapter → Verse → [Words…].

## Prerequisites

- **Python 3.8+** (no external dependencies; uses only the Python standard library).
- A copy of the OSHB XML files from the Open Scriptures MorphHB project:
  1. Download **OSHB-v.2.2.zip** from the MorphHB releases: [https://github.com/openscriptures/morphhb/releases](https://github.com/openscriptures/morphhb/releases)
  2. Extract into an `osis/OSHB-v.2.2/` directory alongside `converter.py`.

# JSON structure

JSON structure is as follows: JSON is a dictionary of all the books in the tanakh, eg "1 Chr". Each dictionary entry contains a list of chapters, and each chapter is in turn a list of verses, which is a list of words.

# License

MIT License 