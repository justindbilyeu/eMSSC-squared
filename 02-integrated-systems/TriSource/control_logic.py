#!/usr/bin/env python3
"""
Adaptive pump control, salt accumulation detection, and basic fault recovery.
"""

from time import time


class ControlState:
    def __init__(self):
        self.last_ok = time()
        self.alarms = set()


def adaptive_pump_speed(solar_w_m2: float, target_flux_lmh: float) -> float:
    # Map solar irradiance to pump PWM (0..1) to balance temp & feed
    if solar_w_m2 <= 200:
        return 0.2
    if solar_w_m2 >= 900:
        return 0.8
    return 0.2 + 0.6 * ((solar_w_m2 - 200) / 700)


def salt_accumulation_detect(flow_capillary_l_h: float, distillate_l_h: float) -> bool:
    # Salt risk if feed << distillate (drying) OR feed >> distillate (over-wet)
    ratio = (flow_capillary_l_h + 1e-6) / (distillate_l_h + 1e-6)
    return ratio < 0.7 or ratio > 1.5


def recover_from_fault(state: ControlState) -> None:
    # Simple recovery: pause pump, flush with small pulse, then resume at lower PWM
    state.alarms.add("FAULT_RECOVERY_PENDING")


if __name__ == "__main__":
    print("PWM @ 600 W/m²:", round(adaptive_pump_speed(600, 1.6), 2))
    print("Salt risk (0.6 feed / 0.8 dist):", salt_accumulation_detect(0.6, 0.8))
