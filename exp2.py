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
    env_upper = environment.upper()
    if env_upper in valid_envs:
        print(f"[Task 3] Selected Environment: {env_upper}")
    else:
        print(f"[Task 3] Error: {environment} is not a valid choice.")
    print("-" * 30)

# ==========================================
# VERSION 3: THE FILE MODULE
# ==========================================
def module_file_handler(build_name: str):
    """Handles BUILD_NAME input (String Parameter)"""
    print("\n--- Version 3: Logic (File Handler) ---")
    print("[Task 1] Checking out repository...")
    
    # Task 3: Create a file with BUILD_NAME as content
    filename = "build_info.txt"
    try:
        with open(filename, "w") as f:
            f.write(build_name)
        print(f"[Task 3] Created '{filename}' with content: {build_name}")
    except Exception as e:
        print(f"[Task 3] Failed to create file: {e}")
    print("-" * 30)

# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    # Simulating the parameters usually passed by the Jenkins UI
    jenkins_params = {
        "RUN_TEST": True,
        "ENVIRONMENT": "PROD",
        "BUILD_NAME": "Production_Release_v3.0"
    }

    print(f"--- STARTING PIPELINE EXECUTION ---")
    
    # Step 1: Run Boolean Logic
    module_test_runner(jenkins_params["RUN_TEST"])
    
    # Step 2: Run Choice Logic
    module_env_manager(jenkins_params["ENVIRONMENT"])
    
    # Step 3: Run String/File Logic
    module_file_handler(jenkins_params["BUILD_NAME"])

    print("\n--- PIPELINE FINISHED SUCCESSFULLY ---")
