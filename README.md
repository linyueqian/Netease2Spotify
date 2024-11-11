# NetEase Music to Spotify Playlist Converter

Convert your NetEase Music (网易云音乐) playlists to Spotify format with proper artist name handling and formatting. This tool helps bridge the gap between Chinese and Western music platforms by:

- Converting Chinese artist names to their English equivalents
- Reformatting song entries for Spotify's import tool
- Handling multiple artists and special characters
- Providing pinyin transliteration for non-mapped artists

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/netease-to-spotify
cd netease-to-spotify

# Install dependencies
pip install -r requirements.txt

# Run the converter
python song_formatter.py
```

## 📋 Prerequisites

- Python 3.6+
- `pypinyin` package
- Input text file (`paste.txt`) containing your NetEase Music playlist

## 🔧 Installation

1. Ensure you have Python 3.6+ installed
2. Install required packages:
```bash
pip install pypinyin
```

## 📖 How to Use

### Step 1: Extract NetEase Playlist
1. Visit [NetEase2Text](https://music.unmeta.cn/)
2. Input your NetEase Music playlist URL
3. Copy the extracted song list
4. Save it to `paste.txt` in the project directory

### Step 2: Convert Format
```bash
python song_formatter.py
```
The formatted list will be saved to `formatted_songs.txt`

### Step 3: Import to Spotify
1. Go to [Spotlistr](https://www.spotlistr.com/search/textbox)
2. Paste the contents of `formatted_songs.txt`
3. Click "Search for Songs"

## 🎵 Example

Input (`paste.txt`):
```text
晚婚 (Live) - 谭维维
Young And Beautiful - Lana Del Rey
纤维 - 林忆莲
```

Output (`formatted_songs.txt`):
```text
Lana Del Rey - Young And Beautiful
Sandy Lam - 纤维
谭维维 (Tan Weiwei) - 晚婚 (Live)
```

## ⚙️ Configuration

### Artist Name Mappings
Add or modify artist name mappings in `song_formatter.py`:

```python
self.artist_mapping = {
    "方大同": "Khalil Fong",
    "王力宏": "Leehom Wang",
    "林俊杰": "JJ Lin",
    # Add more mappings here
}
```

## 🛠️ Technical Details

### Key Features
- Chinese-English artist name mapping
- Pinyin conversion for unmapped Chinese names
- Multiple artist handling
- Special character cleanup
- Error handling for malformed entries

### Class Structure
```python
class SongFormatter:
    def __init__(self)              # Initialize mappings
    def is_chinese(self, text)      # Detect Chinese characters
    def is_english(self, text)      # Check for English text
    def get_artist_name(self, artist) # Process artist names
    def parse_song_line(self, line)  # Parse individual entries
    def format_songs(self, text_input) # Main processing function
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit (`git commit -am 'Add new feature'`)
5. Push (`git push origin feature/improvement`)
6. Create a Pull Request

### Areas for Improvement
- Add more artist name mappings
- Improve special character handling
- Add direct Spotify API integration
- Support more input formats
- Add batch processing capability

## 🐛 Known Issues

- Some Chinese songs might not be available on Spotify
- Artist name matches might need manual verification
- Special characters in song titles may affect matching

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [NetEase2Text](https://music.unmeta.cn/) for playlist extraction
- [Spotlistr](https://www.spotlistr.com/) for Spotify import functionality
- [pypinyin](https://github.com/mozillazg/python-pinyin) for Chinese character conversion

## 📬 Contact

- Create an issue for bug reports or feature requests
- Pull requests are welcome

---

*Note: This tool is not affiliated with NetEase Music or Spotify. Use responsibly and in accordance with the platforms' terms of service.*
