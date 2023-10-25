import importlib
import re
import validate_sudoku

def test_import():
    assert 'numpy' in importlib.sys.modules

def test_validate_sudoku(capsys):
    output = r"^[^in]*valid[^\n]*\n[^\n]*invalid[^\n]*\n[^in]*valid[^\n]*\n[^\n]*invalid[^\n]*"
    validate_sudoku.main()
    captured = capsys.readouterr()
    assert re.search(output, captured.out, re.IGNORECASE)
