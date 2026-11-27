# PyQuran Modern 📖

An experimental wrapper for the `pyquran` library targeting Python 3.13+. 
حل مشكلة التوافق مع إصدارات بايثون الحديثة لمكتبة pyquran.

## Features | المميزات
* **Python 3.13 target**: Uses `audioop-lts` rather than a simulated audio module. Full upstream compatibility still requires testing.
* **Easy to use**: Simple functions for Quranic text and roots.

## Installation | التثبيت
```bash
pip install .  # from the repository checkout
```

## Usage examples | أمثلة

```python
from pyquran_modern import get_word_root, get_verse_text

# root of a word
print(get_word_root("الحمد"))

# text of chapter 1, verse 1
print(get_verse_text(1, 1))
```
