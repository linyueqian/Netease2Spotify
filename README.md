## Introduction

Have you ever wanted to migrate your carefully curated NetEase Music (网易云音乐) playlist to Spotify? In this README, I'll walk you through a Python solution that helps bridge these two platforms, making your music migration seamless and efficient.

## The Challenge

When migrating playlists between NetEase Music and Spotify, we face several challenges:

1. **Different Text Formats**: NetEase Music exports songs in "Title - Artist" format, while Spotify's bulk import tool expects "Artist - Title"
2. **Chinese Artist Names**: Many Chinese artists have both Chinese and English names, making matching difficult
3. **Encoding Issues**: Handling Chinese characters correctly in text processing
4. **Multiple Artists**: Proper handling of songs with multiple artists

## The Solution Pipeline

Here's our three-step solution:

1. Extract playlist from NetEase Music using [NetEase2Text](https://music.unmeta.cn/)
2. Process the text using our Python script
3. Import the processed list into Spotify using [Spotlistr](https://www.spotlistr.com/search/textbox)

## The Code

Let's break down our Python solution that handles the text processing step:

```python
from pypinyin import lazy_pinyin, Style
import re

class SongFormatter:
    def __init__(self):
        # Artist name mappings (Chinese to English)
        self.artist_mapping = {
            "方大同": "Khalil Fong",
            "王力宏": "Leehom Wang",
            "林俊杰": "JJ Lin",
            # ... more mappings ...
        }
```

### Key Components

1. **Artist Name Mapping**
   - We maintain a dictionary of Chinese artist names and their English equivalents
   - This helps Spotify better match the artists

```python
def get_artist_name(self, artist):
    """Convert artist name to appropriate format"""
    artist = artist.strip().replace('/', '&')
    
    # Handle multiple artists
    if '&' in artist or ',' in artist:
        artists = re.split('[&,]', artist)
        return ' & '.join(self.get_artist_name(a.strip()) for a in artists)
    
    # Use predefined English name if available
    if artist in self.artist_mapping:
        return self.artist_mapping[artist]
        
    # Keep English names as is
    if self.is_english(artist):
        return artist
        
    # Convert Chinese to pinyin with original text
    if self.is_chinese(artist):
        pinyin_name = ' '.join([
            word.capitalize() 
            for word in lazy_pinyin(artist, style=Style.NORMAL)
        ])
        return f"{artist} ({pinyin_name})"
```

2. **Format Detection**
   - Detect whether text contains Chinese characters
   - Handle mixed language content appropriately

```python
def is_chinese(self, text):
    """Check if the text contains Chinese characters"""
    return bool(re.search('[\u4e00-\u9fff]', text))

def is_english(self, text):
    """Check if the text is primarily English"""
    return len([c for c in text if ord(c) < 128]) / len(text) > 0.9
```

3. **Line Processing**
   - Parse each song entry
   - Handle potential formatting errors

```python
def parse_song_line(self, line):
    """Parse a single line into title and artist"""
    try:
        if not line.strip():
            return None
        parts = line.strip().split(" - ", 1)
        if len(parts) != 2:
            print(f"Warning: Skipping malformed line: {line}")
            return None
        return parts[0].strip(), parts[1].strip()
    except Exception as e:
        print(f"Error processing line: {line}")
        return None
```

## How to Use

1. **Extract Your Playlist**
   - Go to [NetEase2Text](https://music.unmeta.cn/)
   - Input your NetEase Music playlist URL
   - Copy the extracted song list

2. **Process the List**
   - Save the copied list to `paste.txt`
   - Run the Python script:
   ```bash
   python song_formatter.py
   ```
   - Find the processed list in `formatted_songs.txt`

3. **Import to Spotify**
   - Go to [Spotlistr](https://www.spotlistr.com/search/textbox)
   - Paste the contents of `formatted_songs.txt`
   - Click "Search for Songs"

## Example Results

Before:
```text
晚婚 (Live) - 谭维维
Young And Beautiful - Lana Del Rey
纤维 - 林忆莲
```

After:
```text
Lana Del Rey - Young And Beautiful
Sandy Lam - 纤维
谭维维 (Tan Weiwei) - 晚婚 (Live)
```

## Tips for Better Results

1. **Expand Artist Mappings**: Add more Chinese-English artist name mappings to improve match rates
2. **Handle Special Cases**: Watch for live versions, remixes, and featuring artists
3. **Review Results**: Check Spotify's matches and adjust manually if needed

## Limitations and Future Improvements

- Not all Chinese songs are available on Spotify
- Some artist names might need manual adjustment
- Could add support for more input formats
- Potential to add direct Spotify API integration

## Conclusion

This solution significantly streamlines the process of migrating playlists from NetEase Music to Spotify. While it may not be perfect due to platform differences and availability issues, it automates much of the tedious work involved in playlist migration.

Feel free to contribute to the project or suggest improvements!

---

*Note: Remember to handle your music platform credentials securely and respect platform-specific terms of service when migrating content.*
