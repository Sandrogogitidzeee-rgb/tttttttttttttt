from pathlib import Path


def test_solver_is_disabled_by_default():
    source = Path('main.py').read_text(encoding='utf-8')
    assert '"solver": {\n    "enabled": false' in source
    assert 'return None, None' in source
