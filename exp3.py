import os
import shutil
from datetime import datetime

def run_version_1():
    print("\n--- Version 1: Simple Build ---")
    print("[Task 1] Checkout code from GitHub (Handled by Jenkins)")
    # Task 2: Simulate compilation
    print("[Task 2] Compiling...")
    # Task 3: Display success
    print("[Task 3] BUILD SUCCESSFUL")
    print("-" * 30)

def run_version_2():
    print("\n--- Version 2: Workspace Management ---")
    print("[Task 1] Checkout updated code...")
    # Task 2: Create a folder named build
    if not os.path.exists('build'):
        os.makedirs('build')
        print("[Task 2] Created 'build' folder.")
    
    # Task 3: Copy files into build folder (Simulating copying this script)
    source = 'exp3_simulation.py'
    if os.path.exists(source):
        shutil.copy(source, 'build/')
        print(f"[Task 3] Copied {source} into 'build' folder.")
    print("-" * 30)

def run_version_3():
    print("\n--- Version 3: Diagnostics ---")
    print("[Task 1] Checkout repository...")
    # Task 2: List all files in workspace
    print("[Task 2] Listing files in workspace (dir):")
    for file in os.listdir('.'):
        print(f" - {file}")
    
    # Task 3: Print current build timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[Task 3] Current Build Timestamp: {timestamp}")
    print("-" * 30)

def run_version_4():
    print("\n--- Version 4: Artifact Generation ---")
    print("[Task 1] Checkout repository...")
    # Task 2: Create artifact.txt file
    with open("artifact.txt", "w") as f:
        f.write(f"Artifact created on {datetime.now()}\nBuild Simulation Version 4")
    print("[Task 2] Created 'artifact.txt'")
    
    # Task 3: Archive logic (Note: Jenkins archives the file, Python just confirms it exists)
    if os.path.exists("artifact.txt"):
        print("[Task 3] 'artifact.txt' is ready for archiving.")
    print("-" * 30)

if __name__ == "__main__":
    # You can trigger specific versions or all at once
    run_version_1()
    run_version_2()
    run_version_3()
    run_version_4()
