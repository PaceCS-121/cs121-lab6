import importlib
import re
import population

def test_import():
    assert 'pandas' in importlib.sys.modules

def test_population_growth(capsys):
    outputs = [
        r"(?=.*Average growth)(?=.*8.8)",
        r"(?=.*Max growth)(?=.*[38.6|38.7])",
        r"(?=.*Min growth)(?=.*-10.4)",
        r"(?=.*Standard deviation)(?=.*[12.7|12.8])"
    ]
    population.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_population_changes(capsys):
    outputs = [
        r"8804190",
        r"(?=.*change)(?=.*3184142)",
        r"(?=.*[percent|%])(?=.*[56.6|56.7])",
    ]
    population.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_population_predictions(capsys):
    outputs = [
        r"(?=.*2030)(?=.*9579326)",
        r"(?=.*2100)(?=.*17292338)",
    ]
    population.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)