from pypinyin import lazy_pinyin, Style
import re

class SongFormatter:
    def __init__(self):
        # Define artist name mappings (English translations)
        self.artist_mapping = {
            "方大同": "Khalil Fong",
            "王力宏": "Leehom Wang",
            "林俊杰": "JJ Lin",
            "林忆莲": "Sandy Lam",
            "张惠妹": "A-mei",
            "陈奕迅": "Eason Chan",
            "陶喆": "David Tao",
            "汪苏泷": "Silence Wang",
            "王菲": "Faye Wong",
            "李宗盛": "Jonathan Lee",
            "张学友": "Jacky Cheung",
            "周杰伦": "Jay Chou",
            "周笔畅": "Bibi Zhou",
            "周传雄": "Steve Chou",
            "薛之谦": "Joker Xue",
            "孙燕姿": "Stefanie Sun",
            "莫文蔚": "Karen Mok",
            "邓紫棋": "G.E.M.",
            "蔡依林": "Jolin Tsai",
            "蔡健雅": "Tanya Chua",
            "萧敬腾": "Jam Hsiao",
            "Kevin": "JJ Lin",
            "G.E.M.邓紫棋": "G.E.M."
            # add more if needed
        }

    def is_chinese(self, text):
        """Check if the text contains Chinese characters."""
        return bool(re.search('[\u4e00-\u9fff]', text))

    def is_english(self, text):
        """Check if the text is primarily English."""
        # Consider text as English if it contains mostly ASCII characters
        return len([c for c in text if ord(c) < 128]) / len(text) > 0.9

    def get_artist_name(self, artist):
        """
        Convert artist name to appropriate format:
        - Use predefined English name if available
        - Keep as is if already in English
        - Convert to pinyin with original Chinese if contains Chinese
        """
        # Remove any leading/trailing whitespace and common artifacts
        artist = artist.strip().replace('/', '&')

        # If multiple artists, process each one
        if '&' in artist or ',' in artist:
            artists = re.split('[&,]', artist)
            return ' & '.join(self.get_artist_name(a.strip()) for a in artists)

        # Check mapping first
        if artist in self.artist_mapping:
            return self.artist_mapping[artist]

        # If already English or contains no Chinese, return as is
        if self.is_english(artist):
            return artist

        # If contains Chinese, convert to pinyin
        if self.is_chinese(artist):
            # Convert to title case pinyin
            pinyin_name = ' '.join([
                word.capitalize() 
                for word in lazy_pinyin(artist, style=Style.NORMAL)
            ])
            return f"{artist} ({pinyin_name})"

        return artist

    def parse_song_line(self, line):
        """Parse a single line into title and artist."""
        try:
            # Skip empty lines
            if not line.strip():
                return None
                
            # Split on first occurrence of " - "
            parts = line.strip().split(" - ", 1)
            if len(parts) != 2:
                print(f"Warning: Skipping malformed line: {line}")
                return None

            title, artist = parts
            return title.strip(), artist.strip()
        except Exception as e:
            print(f"Error processing line: {line}")
            print(f"Error details: {str(e)}")
            return None

    def format_songs(self, text_input, output_file="formatted_songs.txt"):
        """Format the entire song list and save to file."""
        formatted_songs = []
        
        for line in text_input.strip().splitlines():
            result = self.parse_song_line(line)
            if result:
                title, artist = result
                formatted_artist = self.get_artist_name(artist)
                formatted_songs.append(f"{formatted_artist} - {title}")

        # Sort alphabetically by artist name
        formatted_songs.sort()
        
        # Write to file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(formatted_songs))
        
        print(f"Formatted songs have been saved to '{output_file}'")
        return formatted_songs

def main():
    # Create formatter instance
    formatter = SongFormatter()
    
    try:
        # Read input from file
        with open("paste.txt", "r", encoding="utf-8") as file:
            text_input = file.read()
        
        # Format and save songs
        formatter.format_songs(text_input)
        
    except FileNotFoundError:
        print("Error: Input file 'paste.txt' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
