from pyquran import quran

# 3. القائمة الكاملة لـ 114 سورة (الخريطة الذكية)
SURAH_MAP = {
    "الفاتحة": 1, "البقرة": 2, "آل عمران": 3, "النساء": 4, "المائدة": 5, "الأنعام": 6,
    "الأعراف": 7, "الأنفال": 8, "التوبة": 9, "يونس": 10, "هود": 11, "يوسف": 12,
    "الرعد": 13, "إبراهيم": 14, "الحجر": 15, "النحل": 16, "الإسراء": 17, "الكهف": 18,
    "مريم": 19, "طه": 20, "الأنبياء": 21, "الحج": 22, "المؤمنون": 23, "النور": 24,
    "الفرقان": 25, "الشعراء": 26, "النمل": 27, "القصص": 28, "العنكبوت": 29, "الروم": 30,
    "لقمان": 31, "السجدة": 32, "الأحزاب": 33, "سبأ": 34, "فاطر": 35, "يس": 36,
    "الصافات": 37, "ص": 38, "الزمر": 39, "غافر": 40, "فصلت": 41, "الشورى": 42,
    "الزخرف": 43, "الدخان": 44, "الجاثية": 45, "الأحقاف": 46, "محمد": 47, "الفتح": 48,
    "الحجرات": 49, "ق": 50, "الذاريات": 51, "الطور": 52, "النجم": 53, "القمر": 54,
    "الرحمن": 55, "الواقعة": 56, "الحديد": 57, "المجادلة": 58, "الحشر": 59, "الممتحنة": 60,
    "الصف": 61, "الجمعة": 62, "المنافقون": 63, "التغابن": 64, "الطلاق": 65, "التحريم": 66,
    "الملك": 67, "القلم": 68, "الحاقة": 69, "المعارج": 70, "نوح": 71, "الجن": 72,
    "المزمل": 73, "المدثر": 74, "القيامة": 75, "الإنسان": 76, "المرسلات": 77, "النبأ": 78,
    "النازعات": 79, "عبس": 80, "التكوير": 81, "الانفطار": 82, "المطففين": 83, "الانشقاق": 84,
    "البروج": 85, "الطارق": 86, "الأعلى": 87, "الغاشية": 88, "الفجر": 89, "البلد": 90,
    "الشمس": 91, "الليل": 92, "الضحى": 93, "الشرح": 94, "التين": 95, "العلق": 96,
    "القدر": 97, "البينة": 98, "الزلزلة": 99, "العاديات": 100, "القارعة": 101, "التكاثر": 102,
    "العصر": 103, "الهمزة": 104, "الفيل": 105, "قريش": 106, "الماعون": 107, "الكوثر": 108,
    "الكافرون": 109, "النصر": 110, "المسد": 111, "الإخلاص": 112, "الفلق": 113, "الناس": 114,
}

# 4. الدوال الأساسية
def get_word_root(word):
    """Root analysis is not implemented by this wrapper."""
    raise NotImplementedError("Root analysis is not supported by this wrapper.")


def get_verse_text(surah_num, verse_num, with_tashkeel=True):
    """Retrieve verse text; reject invalid indices rather than return an error as text."""
    if type(surah_num) is not int or not 1 <= surah_num <= 114:
        raise ValueError("Surah number must be an integer from 1 to 114.")
    if type(verse_num) is not int or verse_num < 1:
        raise ValueError("Verse number must be a positive integer.")
    verse = quran.get_verse(surah_num, verse_num, with_tashkeel=with_tashkeel)
    if not isinstance(verse, str) or not verse.strip():
        raise ValueError("Verse unavailable for the supplied indices.")
    return verse


def get_verse_by_name(surah_name, verse_num, with_tashkeel=True):
    """الميزة الاحترافية: جلب الآية باسم السورة"""
    surah_id = SURAH_MAP.get(surah_name)
    if surah_id:
        return get_verse_text(surah_id, verse_num, with_tashkeel=with_tashkeel)
    raise ValueError(f"Unknown surah name: {surah_name}")

def list_surahs():
    """قائمة بكافة السور المتاحة"""
    return list(SURAH_MAP.keys())