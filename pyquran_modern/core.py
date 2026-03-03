import sys
from types import ModuleType

# خدعة التوافق
if 'audioop' not in sys.modules:
    mock = ModuleType('audioop')
    mock.reverse = lambda data, width: data
    sys.modules['audioop'] = mock

# استيراد المكتبة الأصلية
from pyquran import quran

def get_word_root(word):
    return quran.get_root(quran.strip_tashkeel(word))

def get_verse_text(s, a, with_tashkeel=True):
    return quran.get_verse(s, a, with_tashkeel=with_tashkeel)