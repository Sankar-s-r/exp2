import os

# ==========================================
# VERSION 1: THE BOOLEAN MODULE
# ==========================================
def module_test_runner(run_test: bool):
    """Handles the RUN_TEST logic (Boolean Parameter)"""
    print("--- Version 1: Logic ---")
    print("[Task 1] Checking out code from GitHub...")
    
    if run_test:
        # Task 3: Execute command to display 'Running Test'
        print("[Task 3] Result: Running Test (Simulating BAT command)")
    else:
        print("[Task 3] Result: Test execution skipped.")
    print("-" * 30)


# ==========================================
# VERSION 2: THE CHOICE MODULE
# ==========================================
def module_env_manager(environment: str):
    """Handles ENVIRONMENT selection (Choice Parameter)"""
    print("--- Version 2: Logic ---")
    print("[Task 1] Checking out updated repository...")
    
    # Task 3: Print selected environment
    valid_envs = ['DEV', 'TEST', 'PROD']
    if environment in valid_envs:
        print(f"[Task 3] Selected Environment: {environment}")
    else:
        print(f"[Task 3] Error: {environment} is not a valid choice.")
    print("-" * 30)


# ==========================================
# VERSION 3: THE FILE MODULE
# ==========================================
def module_file_handler(build_name: str):
    """Handles BUILD_NAME input (String Parameter)"""
    print("--- Version 3: Logic ---")
    print("[Task 1] Checking out repository...")
    
    # Task 3: Create a file with BUILD_NAME as content
    filename = "build_info.txt"
    with open(filename, "w") as f:
        f.write(build_name)
    
    print(f"[Task 3] Created '{filename}' with content: {build_name}")
    print("-" * 30)


# ==========================================
# VERSION 4: THE SYSTEM MODULE
# ==========================================
def module_system_diagnostics(all_params: dict):
    """Handles Workspace and Parameter display (Env Variables)"""
    print("--- Version 4: Logic ---")
    print("[Task 1] Checking out repository...")
    
    # Task 2: Display workspace path (Simulating Jenkins WORKSPACE)
    workspace_path = os.getcwd()
    print(f"[Task 2] Jenkins Workspace Path: {workspace_path}")
    
    # Task 3: Print all parameter values
    print("[Task 3] All Parameter Values:")
    for key, value in all_params.items():
        print(f"  - {key}: {value}")
    print("-" * 30)


# ==========================================
# MAIN EXECUTION (The Jenkins 'Pipeline')
# ==========================================
if __name__ == "__main__":
    # Simulating Jenkins Parameter Inputs
    jenkins_params = {
        "RUN_TEST": True,
        "ENVIRONMENT": "TEST",
        "BUILD_NAME": "Production_Build_v1.0"
    }

    print("--- STARTING JENKINS-STYLE PIPELINE ---")
    
    # Run Version 1
    module_test_runner(jenkins_params["RUN_TEST"])
    
    # Run Version 2
    module_env_manager(jenkins_params["ENVIRONMENT"])
    
    # Run Version 3
    module_file_handler(jenkins_params["BUILD_NAME"])
    
    # Run Version 4
    module_system_diagnostics(jenkins_params)
    
    print("--- PIPELINE SUCCESSFUL ---")
