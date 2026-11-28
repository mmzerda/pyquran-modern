# PyQuran Modern — experimental verse retrieval wrapper

An independent Python wrapper around [PyQuran](https://github.com/hci-lab/PyQuran). This project is under validation; compatibility with Python 3.13 is a target, not a verified release claim.

## Scope and limitations

- Retrieve verses by chapter and verse number using upstream PyQuran.
- A corrected mapping of all 114 surah names is available in the core module.
- Invalid or unavailable verse requests raise an error rather than returning an error message as Quranic text.
- Root extraction is not implemented. The legacy get_word_root function explicitly raises NotImplementedError.
- The earlier fake audioop implementation has been removed; installation declares the audioop-lts backport for Python 3.13 and later.

## Development installation

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
```

Installation and upstream integration must be verified in a clean environment before distribution. Unit tests with a simulated upstream API do not establish Quranic text accuracy.

## Upstream and licensing

The upstream repository's LICENSE identifies GNU GPL version 2. Its text and dependencies must be respected. This repository's earlier MIT metadata is not a determination of license compatibility; distribution and license review remain pending.

Do not rely on this wrapper as a verified Quranic text source until the returned texts have been checked against an authoritative reference.
