def convert_length(value, from_unit, to_unit):
    length_units = {
        "m": 1,
        "cm": 100,
        "mm": 1000,
        "km": 0.001,
        "ft": 3.28084,
        "in": 39.3701
    }
    return value * length_units[to_unit] / length_units[from_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "kg": 1,
        "g": 1000,
        "mg": 1_000_000,
        "lb": 2.20462,
        "oz": 35.274
    }
    return value * weight_units[to_unit] / weight_units[from_unit]
