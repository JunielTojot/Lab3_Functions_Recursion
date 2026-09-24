from telemetry_utils import telemetry_generator, monitor_pipeline, analyze_anomaly

# Student-specific inputs
LAST_NAME = "TOJOT"
SEED_NUM = 5
FAVORITE_ARTIST = "NFRealMusic"

@monitor_pipeline
def process_monitoring_pipeline():
    print(f"--- Intelligent Equipment Monitoring Pipeline ---")
    print(f"Operator: {LAST_NAME} | Seed: {SEED_NUM} | Artist: {FAVORITE_ARTIST}")
    
    valid_count = 0
    invalid_count = 0
    abnormal_count = 0
    processed_results = []
    
    # Using generator to fetch stream items
    raw_stream = telemetry_generator(SEED_NUM, count=8)
    
    # Lambda function to filter/transform values (e.g., keep values above a baseline or scale them)
    filter_fn = lambda val: val * 1.1 if val > 10 else 0.0
    
    for raw_val in raw_stream:
        try:
            # Exception handling for telemetry validation
            if raw_val is None or raw_val < 0:
                raise ValueError("Negative or null telemetry reading detected.")
            
            # Apply lambda transformation
            transformed_val = filter_fn(raw_val)
            valid_count += 1
            
            # Check for abnormal readings
            status_report = analyze_anomaly(transformed_val, threshold=40.0)
            if "Abnormal" in status_report:
                abnormal_count += 1
                
            processed_results.append({
                "raw": raw_val,
                "transformed": transformed_val,
                "status": status_report
            })
            
        except Exception as e:
            print(f"  [Exception Caught]: {e} for value: {raw_val}")
            invalid_count += 1

    # Final summary display
    print("\n--- Final Monitoring Summary Report ---")
    print(f"Total Processed Readings: {valid_count + invalid_count}")
    print(f"Valid Readings: {valid_count}")
    print(f"Invalid Readings: {invalid_count}")
    print(f"Detected Abnormal Conditions: {abnormal_count}")
    print(f"Overall Equipment Status: {'ALERT' if abnormal_count > 0 else 'OPTIMAL'}")
    
    return processed_results

if __name__ == "__main__":
    process_monitoring_pipeline()