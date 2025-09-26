POWER_OPTIMIZED_W = {
    "awg_fan": 80,          # high-efficiency DC fan
    "water_pumps": 120,     # optimized low-flow pumps
    "control_system": 15,   # SBC sleep modes
    "sensors": 10           # intermittent sampling
}

DUTY_CYCLE = {
    "awg_fan": 0.5,         # 12h/day average
    "water_pumps": 0.4,     # on-demand adaptive
    "control_system": 0.7,  # mostly idle + bursts
    "sensors": 0.33         # 20 min/hour
}

def daily_aux_kwh(budget=POWER_OPTIMIZED_W, duty=DUTY_CYCLE) -> float:
    wh = sum(budget[k] * 24 * duty.get(k, 1.0) for k in budget)
    return round(wh / 1000.0, 2)


if __name__ == "__main__":
    print("Daily aux energy (kWh):", daily_aux_kwh())
