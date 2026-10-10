import argparse
import re
from collections import Counter
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Count words in a text file.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()
    if args.top < 1:
        parser.error("--top must be at least 1.")

    try:
        text = args.file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        parser.exit(1, f"Could not read file: {error}\n")

    words = re.findall(r"[^\W\d_]+(?:['’][^\W\d_]+)*", text.lower())
    counts = Counter(words)
    print(f"Lines: {len(text.splitlines())}")
    print(f"Words: {len(words)}")
    print(f"Unique words: {len(counts)}")
    print(f"Characters: {len(text)}")
    if counts:
        print("\nMost common words:")
        for word, count in counts.most_common(args.top):
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
