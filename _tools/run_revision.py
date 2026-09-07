from pathlib import Path
import re

_original_subn = re.subn

def _literal_subn(pattern, repl, string, count=0, flags=0):
    if isinstance(repl, str):
        return _original_subn(pattern, lambda _m: repl, string, count=count, flags=flags)
    return _original_subn(pattern, repl, string, count=count, flags=flags)

re.subn = _literal_subn
code = Path('_tools/revise_older_articles.py').read_text(encoding='utf-8')
exec(compile(code, '_tools/revise_older_articles.py', 'exec'), {'__name__': '__main__'})
