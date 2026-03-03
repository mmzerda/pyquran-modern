# PyQuran Modern 📖

A modern, Python 3.13+ compatible wrapper for the `pyquran` library. 
حل مشكلة التوافق مع إصدارات بايثون الحديثة لمكتبة pyquran.

## Features | المميزات
* **Python 3.13 Compatible**: Fixes the `audioop` removal issue.
* **Easy to use**: Simple functions for Quranic text and roots.

## Installation | التثبيت
```bash
pip install pyquran-modern
```

## Usage examples | أمثلة

```python
from pyquran_modern import get_word_root, get_verse_text

# root of a word
print(get_word_root("الحمد"))

# text of chapter 1, verse 1
print(get_verse_text(1, 1))
```
