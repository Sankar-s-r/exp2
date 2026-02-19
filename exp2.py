import os

# ==========================================
# VERSION 1: THE BOOLEAN MODULE
# ==========================================

def module_test_runner(run_test: bool):
    """Handles the RUN_TEST logic (Boolean Parameter)"""
    print("\n--- Version 1: Logic ---")
    print("[Task 1] Checking out code from GitHub...")
    
    if run_test:
        # Task 3: Execute command to display 'Running Test'
        print("[Task 3] Result: Running Test (Simulating BAT command)")
    else:
        print("[Task 3] Result: Test execution skipped.")
    print("-" * 30)

if __name__ == "__main__":
    # Simulating Jenkins Parameter Inputs
    jenkins_params = {
        "RUN_TEST": True,
        "ENVIRONMENT": "TEST",
        "BUILD_NAME": "Production_Build_v1.0"
    }

    print("--- STARTING JENKINS-STYLE PIPELINE ---")
    
    # Use the parameter from our dictionary to drive the logic
    # This ensures your 'run_test' logic is actually tied to your inputs
    module_test_runner(jenkins_params["RUN_TEST"])
