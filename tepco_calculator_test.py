"""
This is unit testing for calculator for Tepco electricity charges in Japan.
"""
import unittest
from decimal import Decimal
import tepco_calculator

class TestTepcoCalculator(unittest.TestCase):
    """Test Tepco Calculator"""
    def test_scenarios(self):
        """Test scenarios"""
        self.assertEqual(tepco_calculator.total_calc(5, 100), 0)
        self.assertEqual(tepco_calculator.total_calc(40, -10), 0)

    def test_basic_charge_calc(self):
        """Test basic charge calculation"""
        self.assertEqual(tepco_calculator.basic_charge_calc(10), 286.00)
        self.assertEqual(tepco_calculator.basic_charge_calc(15), 429.00)
        self.assertEqual(tepco_calculator.basic_charge_calc(20), 572.00)
        self.assertEqual(tepco_calculator.basic_charge_calc(30), 858.00)
        self.assertEqual(tepco_calculator.basic_charge_calc(40), 1144.00)
        self.assertEqual(tepco_calculator.basic_charge_calc(50), 1430.00)
        self.assertEqual(tepco_calculator.basic_charge_calc(60), 1716.00)

    def test_power_charge_calc(self):
        """Test electricity charges calculation"""
        self.assertEqual(tepco_calculator.power_charge_calc(100), Decimal('1988.00'))
        self.assertEqual(tepco_calculator.power_charge_calc(120), Decimal('2385.60'))
        self.assertEqual(tepco_calculator.power_charge_calc(150), Decimal('3180.00'))
        self.assertEqual(tepco_calculator.power_charge_calc(300), Decimal('7152.00'))

    def test_fuel_cost_calc(self):
        """Test fuel cost adjustment calculation"""
        self.assertEqual(tepco_calculator.fuel_cost_calc(100), Decimal('-485.00'))
        self.assertEqual(tepco_calculator.fuel_cost_calc(120), Decimal('-582.00'))
        self.assertEqual(tepco_calculator.fuel_cost_calc(300), Decimal('-1455.00'))

    def test_renewable_energy_calc(self):
        """Test renewable energy surcharge calculation"""
        self.assertEqual(tepco_calculator.renewable_energy_calc(100), Decimal('298.00'))
        self.assertEqual(tepco_calculator.renewable_energy_calc(120), Decimal('357.60'))

    def test_total_calc(self):
        """Test total charges calculation"""
        self.assertEqual(tepco_calculator.total_calc(40, 360), 9457)
        self.assertEqual(tepco_calculator.total_calc(40, 120), 3306)
        self.assertEqual(tepco_calculator.total_calc(40, 300), 7735)
        self.assertEqual(tepco_calculator.total_calc(40, 301), 7764)

if __name__ == '__main__':
    unittest.main()
