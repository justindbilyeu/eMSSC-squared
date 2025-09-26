from tests.utils import load_module


system_integration = load_module(
    "system_integration",
    "02-integrated-systems/TriSource/system_integration.py",
)

daily_aux_kwh = system_integration.daily_aux_kwh


def test_daily_aux_under_9kwh():
    kwh = daily_aux_kwh()
    assert kwh <= 9.0
