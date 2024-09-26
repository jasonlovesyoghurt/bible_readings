import webbrowser
from datetime import datetime, timedelta
import json

sunday_readings = {
    "2024-01-07": ("Psalm 33",),
    "2024-01-14": ("Psalm 55",),
    "2024-01-21": ("Psalm 88",),
    "2024-01-28": ("Psalm 137", "Romans 12:14-21"),
    "2024-02-04": ("Psalm 139",),
    "2024-02-11": ("John 7:1-24", "Leviticus 23:33-44"),
    "2024-02-18": ("John 7:25-36",),
    "2024-02-25": ("John 7:37-52",),
    "2024-03-03": ("John 8:12-30",),
    "2024-03-10": ("John 8:31-59", "Genesis 18:1-8"),
    "2024-03-17": ("John 9",),
    "2024-03-24": ("John 10:1-21",),
    "2024-03-29": ("John 19",),  # Friday
    "2024-03-31": ("John 20:1-18",),
    "2024-04-07": ("John 20:19-31",),
    "2024-04-14": ("1 Kings 16:29-17:7", "James 5:13-18"),
    "2024-04-21": ("1 Kings 17:8-24", "Luke 7:11-17"),
    "2024-04-28": ("1 Kings 18", "1 Thessalonians 1:1-10"),
    "2024-05-05": ("1 Kings 19:1-18", "Romans 11:1-6"),
    "2024-05-12": ("2 Kings 1",),
    "2024-05-19": ("2 Kings 2", "2 Timothy 2:1-7"),
    "2024-05-26": ("1 Kings 17:1-7", "James 5:13-20"),
    "2024-06-02": ("Psalm 110", "Hebrews 4:14-16"),
    "2024-06-09": ("Numbers 11:1-9", "Luke 11:1-13"),
    "2024-06-16": ("Psalm 72:1-20", "John 14:12-14"),
    "2024-06-23": ("Isaiah 51:1-16", "Romans 8:12-30"),
    "2024-06-30": ("Isaiah 59:1-20", "Ephesians 6:10-20"),
    "2024-07-07": ("John 1:1-13", "1 John 1:1-2:6"),
    "2024-07-14": ("John 13:31-35", "1 John 2:7-27"),
    "2024-07-21": ("John 15:1-19", "1 John 2:28-3:18"),
    "2024-07-28": ("John 15:20-16:4a", "1 John 3:19-4:6"),
    "2024-08-04": ("John 16:4b-11", "1 John 4:7-5:5"),
    "2024-08-11": ("John 16:12-15", "1 John 5:6-21"),
    "2024-08-18": ("Exodus 19:1-6", "1 Peter 2:4-10"),
    "2024-08-25": ("Romans 15:1-7", "Philippians 2:1-18"),
    "2024-09-01": ("1 Thessalonians 4:9-16", "Hebrews 10:24-25"),
    "2024-09-08": ("Romans 12:9-21", "1 Corinthians 13"),
    "2024-09-15": ("Psalm 68:1-19", "Ephesians 4:1-16"),
    "2024-09-22": ("Acts 2:42-47", "Romans 12:9-21"),
    "2024-09-29": ("Psalm 53", "Romans 3:9-21"),
    "2024-10-06": ("Psalm 32", "Romans 3:21-26"),
    "2024-10-13": ("Psalm 33", "Romans 5:1-11"),
    "2024-10-20": ("Isaiah 40:12-26", "Romans 11:33-36"),
    "2024-10-27": ("Psalm 27", "Romans 12:1-3"),
    "2024-11-03": ("Leviticus 16:6-19", "Hebrews 9:6-10"),
    "2024-11-10": ("1 Kings 8:22-30", "John 4:16-26"),
    "2024-11-17": ("Revelation 5:1-14",),
    "2024-11-24": ("Luke 1:1-4",),
    "2024-12-01": ("Luke 1:5-25",),
    "2024-12-08": ("Luke 1:26-38",),
    "2024-12-15": ("Luke 1:39-56",),
    "2024-12-22": ("Luke 1:57-80",),
    "2024-12-24": ("Luke 2:1-21",),  # Tuesday
    "2024-12-25": ("Luke 2:22-38",),  # Wednesday
    "2024-12-29": ("Luke 2:39-52",),
}

def search_passage(passage):
    passage_conv1 = passage.replace(" ","%20")
    passage_conv2 = passage_conv1.replace(":","%3A")
    url = f"https://www.biblegateway.com/passage/?search={passage_conv2}"
    webbrowser.open(url)
    return passage, url

def get_next_sunday_readings():
    today = datetime.now()
    next_sunday = today + timedelta((6 - today.weekday()) % 7)
    next_sunday_str = next_sunday.strftime("%Y-%m-%d")
    return sunday_readings.get(next_sunday_str, ("No reading found",))

if __name__ == "__main__":
    readings = get_next_sunday_readings()
    urls = [search_passage(reading)[1] for reading in readings]
    print("Copy the below text to share with your growth group. If any errors please shoot me a message \n")
    print("________________________________________________")
    print("Here's next Sunday's Bible Reading(s) for your Quiet Times :)")
    for i, (reading, url) in enumerate(zip(readings, urls), 1):
        print(f"\n Passage {i}: {reading} {url}")
    print("________________________________________________")
    # print("All Sunday Readings in JSON format:")
    # print(json.dumps(sunday_readings, indent=4))
    input("\nPress Enter to exit...")