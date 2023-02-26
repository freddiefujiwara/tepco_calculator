"""
This is calculator for Tepco electricity charges in Japan.
"""

from decimal import Decimal
import math

# Fuel cost adjustment and renewable energy surcharge are prices as of March 2021
fuel_cost = Decimal("-4.85") # JPY/kWh
renewable_energy = Decimal("2.98") # JPY/kWh

# Basic rate table (per contracted capacity)
basic_charge = {10: Decimal("286.00"),
15: Decimal("429.00"),
 20: Decimal("572.00"),
 30: Decimal("858.00"),
 40: Decimal("1144.00"),
 50: Decimal("1430.00"),
 60: Decimal("1716.00")}
basic_charge.setdefault(0,0)

# Table of electricity charges (per usage)
power_charge = {120: Decimal("19.88"), 300: Decimal("26.48")}

def basic_charge_calc(capacity):
    """Calculate basic charge (per month)"""
    return basic_charge.get(capacity, 0)

def power_charge_calc(usage):
    """Calculate electricity charges (per month)"""
    if usage <= 120:
        return usage * power_charge[120]
    if usage <= 300:
        return 120 * power_charge[120] + (usage - 120) * power_charge[300]
    return 120 * power_charge[120] + 180 * power_charge[300] + (usage - 300) * Decimal("30.57")

def fuel_cost_calc(usage):
    """Calculate fuel cost adjustment (per month)"""
    return usage * fuel_cost

def renewable_energy_calc(usage):
    """Calculate renewable energy surcharge (per month)"""
    return usage * renewable_energy

def total_calc(capacity, usage):
    """Calculate total charges (per month)"""
    basic_cost = basic_charge_calc(capacity)
    if basic_cost == 0:
        return 0
    if usage <= 0:
        return 0

    return math.ceil(basic_cost
     + power_charge_calc(usage)
     + fuel_cost_calc(usage)
     + renewable_energy_calc(usage))
