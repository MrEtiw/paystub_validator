from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import List, Dict

from .shift import Shift

@dataclass
class Paystub:
    pay_period_start: datetime
    pay_period_end: datetime
    base_rate: Decimal
    night_premium_rate: Decimal
    weekend_premium_rate: Decimal
    critical_care_premium_rate: Decimal
    total_hours: Decimal
    total_pay: Decimal
    shifts: List[Shift]
    
    def calculate_expected_pay(self) -> Decimal:
        """Calculate the expected pay based on all shifts and their premiums."""
        return sum(
            shift.calculate_total_pay(
                self.night_premium_rate,
                self.weekend_premium_rate,
                self.critical_care_premium_rate
            )
            for shift in self.shifts
        )
    
    def validate(self) -> Dict[str, bool]:
        """Validate the paystub against the calculated expected pay."""
        expected_pay = self.calculate_expected_pay()
        expected_hours = sum(shift.duration_hours for shift in self.shifts)
        
        return {
            "pay_matches": abs(expected_pay - self.total_pay) < Decimal('0.01'),
            "hours_match": abs(expected_hours - self.total_hours) < Decimal('0.01'),
            "expected_pay": expected_pay,
            "expected_hours": expected_hours
        } 