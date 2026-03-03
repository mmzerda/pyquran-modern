"""Package entry point for pyquran_modern.

This module exposes the convenience functions defined in
:mod:`pyquran_modern.core` and does not execute any code at import time.
The previous demo code caused a circular import which prevented the
package from being imported correctly.
"""

from .core import get_word_root, get_verse_text

__all__ = ["get_word_root", "get_verse_text"]

