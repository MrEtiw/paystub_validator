from dataclasses import dataclass
from datetime import datetime, time
from decimal import Decimal
from typing import List

@dataclass
class Shift:
    start_time: datetime
    end_time: datetime
    base_rate: Decimal
    is_weekend: bool
    is_night: bool
    is_critical_care: bool
    
    @property
    def duration_hours(self) -> Decimal:
        """Calculate the duration of the shift in hours."""
        duration = self.end_time - self.start_time
        return Decimal(str(duration.total_seconds() / 3600))
    
    @property
    def night_hours(self) -> Decimal:
        """Calculate the number of hours worked during night shift."""
        if not self.is_night:
            return Decimal('0')
        return self.duration_hours
    
    @property
    def weekend_hours(self) -> Decimal:
        """Calculate the number of hours worked during weekend."""
        if not self.is_weekend:
            return Decimal('0')
        return self.duration_hours
    
    @property
    def critical_care_hours(self) -> Decimal:
        """Calculate the number of hours worked in critical care."""
        if not self.is_critical_care:
            return Decimal('0')
        return self.duration_hours
    
    def calculate_total_pay(self, 
                          night_premium_rate: Decimal,
                          weekend_premium_rate: Decimal,
                          critical_care_premium_rate: Decimal) -> Decimal:
        """Calculate total pay including all premiums."""
        base_pay = self.base_rate * self.duration_hours
        night_premium = self.night_hours * night_premium_rate
        weekend_premium = self.weekend_hours * weekend_premium_rate
        critical_care_premium = self.critical_care_hours * critical_care_premium_rate
        
        return base_pay + night_premium + weekend_premium + critical_care_premium 