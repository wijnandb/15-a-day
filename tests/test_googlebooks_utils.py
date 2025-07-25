import importlib.util
import sys
import types
from pathlib import Path


def load_googlebooks():
    path = Path(__file__).resolve().parents[1] / "python" / "googlebooks.py"
    spec = importlib.util.spec_from_file_location("googlebooks", path)
    module = importlib.util.module_from_spec(spec)
    # Stub external dependencies
    sys.modules.setdefault("requests", types.ModuleType("requests"))
    slugify_mod = types.ModuleType("slugify")
    slugify_mod.slugify = lambda x: x
    sys.modules.setdefault("slugify", slugify_mod)
    sys.modules.setdefault("yaml", types.ModuleType("yaml"))
    spec.loader.exec_module(module)
    return module

googlebooks = load_googlebooks()


def test_format_author_name_comma():
    assert googlebooks.format_author_name("Doe, John") == "John Doe"


def test_format_author_name_single():
    assert googlebooks.format_author_name("Plato") == "Plato"


def test_normalize_authors_colon_string():
    result = googlebooks.normalize_authors(["Smith, John:Brown, Bob:"])
    assert result == ["Smith, John", "Brown, Bob"]


def test_normalize_authors_simple_list():
    assert googlebooks.normalize_authors(["Alice"]) == ["Alice"]
