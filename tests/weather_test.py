import importlib
import re
import weather

def test_import():
    assert 'pandas' in importlib.sys.modules

def test_weather_aggs(capsys):
    outputs = [
        r"(?=.*rain)(?=.*[\\d.]+)",
        r"(?=.*temp)(?=.*[\\d.]+)",
    ]
    weather.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_weather_avgs(capsys):
    outputs = [
        r"(?=.*pressure)(?=.*[\\d.]+)",
        r"(?=.*wind)(?=.*[\\d.]+)",
        r"(?=.*humidity)(?=.*[\\d.]+)",
    ]
    weather.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)

def test_weather_latest(capsys):
    outputs = [
        r"(?=.*AirTemp)(?=.*[\\d.]+)",
        r"(?=.*BaroPressure)(?=.*[\\d.]+)",
        r"(?=.*DistLightning)(?=.*[\\d.]+)",
        r"(?=.*LightningStrikes)(?=.*[\\d.]+)",
        r"(?=.*MaxWindSpeed)(?=.*[\\d.]+)",
        r"(?=.*Rain)(?=.*[\\d.]+)",
        r"(?=.*RelHumid)(?=.*[\\d.]+)",
        r"(?=.*RelHumidTemp)(?=.*[\\d.]+)",
        r"(?=.*SolarFlux)(?=.*[\\d.]+)",
        r"(?=.*VaporPressur)(?=.*[\\d.]+)",
        r"(?=.*WindDir)(?=.*[\\d.]+)",
        r"(?=.*WindSpeed)(?=.*[\\d.]+)",
    ]
    weather.main()
    captured = capsys.readouterr()
    for output in outputs:
        assert re.search(output, captured.out, re.IGNORECASE)