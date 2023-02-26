"""Test module for tepco_calculator.py"""
from decimal import Decimal
import tepco_calculator

def test_scenarios():
    """Test scenarios"""
    assert tepco_calculator.total_calc(5, 100) == 0
    assert tepco_calculator.total_calc(40, -10) == 0

def test_basic_charge_calc():
    """Test basic charge calculation"""
    assert tepco_calculator.basic_charge_calc(10) == 286.00
    assert tepco_calculator.basic_charge_calc(15) == 429.00
    assert tepco_calculator.basic_charge_calc(20) == 572.00
    assert tepco_calculator.basic_charge_calc(30) == 858.00
    assert tepco_calculator.basic_charge_calc(40) == 1144.00
    assert tepco_calculator.basic_charge_calc(50) == 1430.00
    assert tepco_calculator.basic_charge_calc(60) == 1716.00

def test_power_charge_calc():
    """Test electricity charges calculation"""
    assert tepco_calculator.power_charge_calc(100) == Decimal('1988.00')
    assert tepco_calculator.power_charge_calc(120) == Decimal('2385.60')
    assert tepco_calculator.power_charge_calc(150) == Decimal('3180.00')
    assert tepco_calculator.power_charge_calc(300) == Decimal('7152.00')

def test_fuel_cost_calc():
    """Test fuel cost adjustment calculation"""
    assert tepco_calculator.fuel_cost_calc(100) == Decimal('-485.00')
    assert tepco_calculator.fuel_cost_calc(120) == Decimal('-582.00')
    assert tepco_calculator.fuel_cost_calc(300) == Decimal('-1455.00')

def test_renewable_energy_calc():
    """Test renewable energy surcharge calculation"""
    assert tepco_calculator.renewable_energy_calc(100) == Decimal('298.00')
    assert tepco_calculator.renewable_energy_calc(120) == Decimal('357.60')

def test_total_calc():
    """Test total charges calculation"""
    assert tepco_calculator.total_calc(40, 360) == 9457
    assert tepco_calculator.total_calc(40, 120) == 3306
    assert tepco_calculator.total_calc(40, 300) == 7735
    assert tepco_calculator.total_calc(40, 301) == 7764
