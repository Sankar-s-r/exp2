import os

# ==========================================
# VERSION 1: THE BOOLEAN MODULE
# ==========================================
def module_test_runner(run_test: bool):
    """Handles the RUN_TEST logic (Boolean Parameter)"""
    print("\n--- Version 1: Logic (Test Runner) ---")
    print("[Task 1] Checking out code from GitHub...")
    
    if run_test:
        print("[Task 3] Result: Running Test (Simulating BAT command)")
    else:
        print("[Task 3] Result: Test execution skipped.")
    print("-" * 30)

# ==========================================
# VERSION 2: THE CHOICE MODULE
# ==========================================
def module_env_manager(environment: str):
    """Handles ENVIRONMENT selection (Choice Parameter)"""
    print("\n--- Version 2: Logic (Env Manager) ---")
    print("[Task 1] Checking out updated repository...")
    
    valid_envs = ['DEV', 'TEST', 'PROD']
    if environment.upper() in valid_envs:
        print(f"[Task 3] Selected Environment: {environment.upper()}")
    else:
        print(f"[Task 3] Error: {environment} is not a valid choice.")
    print("-" * 30)

# ==========================================
# MAIN EXECUTION (The "Jenkins" Trigger)
# ==========================================
if __name__ == "__main__":
    # Simulating Jenkins Parameter Inputs
    # In a real Jenkins job, these would come from the UI
    jenkins_params = {
        "RUN_TEST": True,           # Boolean Parameter
        "ENVIRONMENT": "TEST",      # Choice Parameter
        "BUILD_NAME": "Build_v2.0"  # String Parameter
    }

    print(f"--- STARTING PIPELINE: {jenkins_params['BUILD_NAME']} ---")
    
    # Execute Version 1 logic
    module_test_runner(jenkins_params["RUN_TEST"])
    
    # Execute Version 2 logic
    module_env_manager(jenkins_params["ENVIRONMENT"])

    print("\n--- PIPELINE FINISHED SUCCESSFULLY ---")
