from tests.utils import load_module


control_logic = load_module(
    "control_logic",
    "02-integrated-systems/TriSource/control_logic.py",
)

adaptive_pump_speed = control_logic.adaptive_pump_speed
salt_accumulation_detect = control_logic.salt_accumulation_detect


def test_adaptive_pump_bounds():
    assert 0.0 <= adaptive_pump_speed(100, 1.6) <= 1.0
    assert 0.0 <= adaptive_pump_speed(1000, 1.6) <= 1.0


def test_salt_detection_triggers():
    assert salt_accumulation_detect(0.4, 0.8) is True  # too low feed
    assert salt_accumulation_detect(1.4, 0.8) is True  # too high feed
    assert salt_accumulation_detect(0.9, 0.8) is False
