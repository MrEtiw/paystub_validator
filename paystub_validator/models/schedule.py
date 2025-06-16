from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict
from decimal import Decimal

from .shift import Shift

@dataclass
class Schedule:
    shifts: List[Shift]
    
    def get_shifts_for_period(self, start_date: datetime, end_date: datetime) -> List[Shift]:
        """Get all shifts within a specific date range."""
        return [
            shift for shift in self.shifts
            if start_date <= shift.start_time <= end_date
        ]
    
    def get_total_hours(self) -> Decimal:
        """Calculate total hours worked in the schedule."""
        return sum(shift.duration_hours for shift in self.shifts)
    
    def get_hours_by_type(self) -> Dict[str, Decimal]:
        """Get total hours broken down by shift type."""
        return {
            "regular": sum(shift.duration_hours for shift in self.shifts 
                         if not any([shift.is_night, shift.is_weekend, shift.is_critical_care])),
            "night": sum(shift.night_hours for shift in self.shifts),
            "weekend": sum(shift.weekend_hours for shift in self.shifts),
            "critical_care": sum(shift.critical_care_hours for shift in self.shifts)
        } 