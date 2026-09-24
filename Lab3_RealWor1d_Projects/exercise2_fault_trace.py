# Student-specific inputs
LAST_NAME = "TOJOT"
SEED_NUM = 5
FAVORITE_ARTIST = "NFRealMusic"

# Global call counter
recursion_count = 0

def generate_fault_code():
    # Generate unique fault code using student-specific inputs
    prefix = LAST_NAME[:3].upper()
    artist_code = len(FAVORITE_ARTIST)
    base_code = (SEED_NUM * 100) + artist_code
    return f"{prefix}-{base_code}"

def recursive_fault_tracer(code_value, depth):
    global recursion_count
    recursion_count += 1
    
    # Base condition: Stop when depth reaches 0 or below
    if depth <= 0:
        print(f"  [Base Condition Reached] Trace depth zero. Finalizing code segment.")
        return [code_value]
    
    # Recursive step: modify code value and decrease depth
    print(f"  [Trace Step {recursion_count}] Processing value: {code_value} at depth {depth}")
    next_value = f"{code_value}-X{depth}"
    
    return [code_value] + recursive_fault_tracer(next_value, depth - 1)

def run_fault_trace_program():
    print(f"--- Recursive Fault Trace Program ---")
    initial_code = generate_fault_code()
    print(f"Generated Fault Code: {initial_code}")
    
    # Run recursion with a depth mapped to SEED_NUM (max 5 for manageability)
    depth = min(SEED_NUM, 5)
    print(f"Starting recursive fault trace with depth: {depth}\n")
    
    trace_results = recursive_fault_tracer(initial_code, depth)
    
    print("\n--- Final Diagnostic Trace Report ---")
    print(f"Generated Fault Code: {initial_code}")
    print(f"Recursive Trace Sequence: {trace_results}")
    print(f"Number of Recursive Calls: {recursion_count}")

if __name__ == "__main__":
    run_fault_trace_program()