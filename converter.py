import os
import re
import json
import xml.etree.ElementTree as ET

# --------------------------------------------------
# Configuration: folder paths
# --------------------------------------------------
base_dir = os.path.dirname(__file__)
books_dir = os.path.join(base_dir, "osis", "OSHB-v.2.2")
ns = {'osis': 'http://www.bibletechnologies.net/2003/OSIS/namespace'}

# --------------------------------------------------
# Clean verse text
# --------------------------------------------------
def clean_verse(verse_elem):
    """
    Extracts all text from a <verse> element, skips <note>,
    removes markup (slashes, pipes, maqaf), collapses whitespace.
    Returns a cleaned single-line string with full niqqud.
    """
    parts = []
    for node in verse_elem.iter():
        if node.tag == f"{{{ns['osis']}}}note":
            continue
        if node.text:
            parts.append(node.text)
        if node.tail:
            parts.append(node.tail)
    raw = "".join(parts)
    # remove unwanted markup
    txt = raw.replace('\n', ' ')
    txt = txt.replace('/', '')
    txt = txt.replace('׀', ' ')
    txt = txt.replace('\u05BE', ' ')
    # collapse whitespace
    return re.sub(r'\s+', ' ', txt).strip()

# --------------------------------------------------
# Main conversion logic: output verses as lists of words
# --------------------------------------------------
hebrew = {}
for fname in sorted(os.listdir(books_dir)):
    if not fname.lower().endswith('.xml'):
        continue

    # parse each book XML
    path = os.path.join(books_dir, fname)
    tree = ET.parse(path)
    root = tree.getroot()
    book_div = root.find('.//osis:div[@type="book"]', ns)
    if book_div is None:
        print(f"Skipping {fname}: no book div.")
        continue

    book_id = book_div.get('osisID')
    chapters = []

    # iterate chapters and verses
    for chap in book_div.findall('osis:chapter', ns):
        verses = []
        for verse in chap.findall('osis:verse', ns):
            cleaned = clean_verse(verse)
            # split cleaned verse into words (preserving nikkud)
            words = cleaned.split()
            verses.append(words)
        chapters.append(verses)

    hebrew[book_id] = chapters
    print(f"Parsed {book_id}: {len(chapters)} chapters.")

# write JSON file
out_path = os.path.join(base_dir, "hebrew_bible_with_nikkud.json")
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(hebrew, f, ensure_ascii=False, indent=2)
print(f"✅ Wrote JSON with {len(hebrew)} books to {out_path}")
