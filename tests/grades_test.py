import importlib
import re
import grades

def test_import():
    assert 'pandas' in importlib.sys.modules

def test_grades_simple(capsys):
    outputs = [
        '18', 
        '94.6' 
    ]
    grades.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_grades_lows(capsys):
    outputs = [ 
        '88.8', 
        r'(?=.*DB10)(?=.*[77.78|77.8])' 
    ]
    grades.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_grades_lookups(capsys):
    outputs = [ 
        r'[86.28|86.3]', 
        '104.5'
    ]
    grades.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)