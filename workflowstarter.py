import subprocess
import sys

def run_nextflow_workflow(workflow_path):
    if len(sys.argv) > 1:
        if sys.argv[1] == "--cleanup":
            command = ["nextflow", "run", workflow_path, "--cleanup"]
    else:
        command = ["nextflow", "run", workflow_path]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


workflow_path = "/mnt/c/Users/proec/Desktop/Spachelor/Bachelor_Arbeit/workflow.nf"
output = run_nextflow_workflow(workflow_path)
print(output)