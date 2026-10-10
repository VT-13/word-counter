# Word counter

Count lines, words, unique words, and characters in a UTF-8 text file. Also shows the most common words, ignoring capitalization.

Requires Python 3. No packages to install.

```sh
python3 count.py sample.txt
python3 count.py sample.txt --top 3
```

Words contain letters and can include apostrophes. Numbers and punctuation are skipped. Spaces and newlines count as characters.
