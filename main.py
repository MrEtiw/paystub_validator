from datetime import datetime, timedelta
from decimal import Decimal

from paystub_validator.models import Shift, Paystub, Schedule

def main():
    # Example usage
    # Create some sample shifts
    shifts = [
        Shift(
            start_time=datetime(2024, 3, 1, 8, 0),  # 8 AM
            end_time=datetime(2024, 3, 1, 16, 0),   # 4 PM
            base_rate=Decimal('25.00'),
            is_weekend=False,
            is_night=False,
            is_critical_care=False
        ),
        Shift(
            start_time=datetime(2024, 3, 2, 23, 0),  # 11 PM
            end_time=datetime(2024, 3, 3, 7, 0),    # 7 AM
            base_rate=Decimal('25.00'),
            is_weekend=True,
            is_night=True,
            is_critical_care=True
        )
    ]
    
    # Create a schedule
    schedule = Schedule(shifts=shifts)
    
    # Create a paystub
    paystub = Paystub(
        pay_period_start=datetime(2024, 3, 1),
        pay_period_end=datetime(2024, 3, 3),
        base_rate=Decimal('25.00'),
        night_premium_rate=Decimal('2.50'),
        weekend_premium_rate=Decimal('3.00'),
        critical_care_premium_rate=Decimal('5.00'),
        total_hours=Decimal('16.00'),
        total_pay=Decimal('500.00'),
        shifts=shifts
    )
    
    # Validate the paystub
    validation_result = paystub.validate()
    print("Validation Results:")
    print(f"Pay matches: {validation_result['pay_matches']}")
    print(f"Hours match: {validation_result['hours_match']}")
    print(f"Expected pay: ${validation_result['expected_pay']}")
    print(f"Expected hours: {validation_result['expected_hours']}")

if __name__ == "__main__":
    main()
