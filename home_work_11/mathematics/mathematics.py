def temperature_f_to_c(f: float) -> float:
    celsius = (f - 32) / 1.8
    return celsius


def temperature_c_to_f(c: float) -> float:
    fahrenheit = c * 1.8 + 32
    return fahrenheit
