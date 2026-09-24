import functools

# Student-specific inputs
LAST_NAME = "TOJOT"
SEED_NUM = 5
FAVORITE_ARTIST = "NFRealMusic"

# Decorator to record the diagnostic process
def diagnostic_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOGGER] Starting diagnostic process for: {FAVORITE_ARTIST}")
        result = func(*args, **kwargs)
        print("[LOGGER] Diagnostic process completed successfully.")
        return result
    return wrapper

# Reusable function for validation
def validate_reading(reading):
    try:
        val = float(reading)
        if val < 0:
            raise ValueError("Reading cannot be negative.")
        return val
    except (ValueError, TypeError) as e:
        print(f"  [Error] Invalid input '{reading}': {e}. Setting value to 0.0.")
        return 0.0

# Reusable function for calculation
def calculate_metrics(readings):
    valid_readings = [validate_reading(r) for r in readings]
    total = sum(valid_readings)
    average = total / len(valid_readings) if valid_readings else 0
    return valid_readings, average

# Reusable function for classification
def classify_condition(average):
    threshold = SEED_NUM * 10
    if average > threshold:
        return "CRITICAL / ABNORMAL"
    elif average > (threshold / 2):
        return "MODERATE / WARNING"
    else:
        return "NORMAL / STABLE"

@diagnostic_logger
def run_diagnostic_system():
    print(f"--- Equipment Diagnostic System ---")
    print(f"Operator: {LAST_NAME} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}")
    
    # Sample raw operating readings (including some invalid ones to test exception handling)
    raw_readings = [45.5, "invalid_val", 82.1, -12.4, 60.0]
    print(f"Raw Input Readings: {raw_readings}")
    
    valid_readings, avg = calculate_metrics(raw_readings)
    status = classify_condition(avg)
    
    print("\n--- Diagnostic Summary Report ---")
    print(f"Processed Readings: {valid_readings}")
    print(f"Calculated Average: {avg:.2f}")
    print(f"Equipment Status: {status}")

if __name__ == "__main__":
    run_diagnostic_system()