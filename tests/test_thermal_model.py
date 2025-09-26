from tests.utils import load_module


thermal_model = load_module(
    "thermal_model",
    "05-technical-resources/simulations/thermal_model.py",
)

EvapParams = thermal_model.EvapParams
field_flux_lmh = thermal_model.field_flux_lmh
daily_output_L = thermal_model.daily_output_L


def test_derate_capped_by_lab():
    p = EvapParams(environmental_factor=1.0, stages=1)
    assert field_flux_lmh(p) <= 3.4


def test_field_flux_derates():
    p = EvapParams(environmental_factor=0.5, stages=3, stage_efficiency=0.85)
    f = field_flux_lmh(p)
    assert 1.4 <= f <= 1.9  # ~1.6–1.7 typical


def test_daily_output_reasonable():
    p = EvapParams(environmental_factor=0.5, stages=3, sun_hours=5.5, area_m2=6.0)
    d = daily_output_L(p)
    assert 50 <= d <= 60
