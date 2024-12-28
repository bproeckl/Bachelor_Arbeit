import subprocess
import sys
import argparse

def parse():
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('-c', '--cleanup',
                    action='store_true',
                    help = "cleans workdir")  # on/off flag
    return parser.parse_args()

def run_nextflow_workflow(workflow_path, cleanup):
    if cleanup:
        command = ["nextflow", "run", workflow_path, "--cleanup"]
    else:
        command = ["nextflow", "run", workflow_path]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

args = parse()
workflow_path = "/mnt/c/Users/proec/Desktop/Spachelor/Bachelor_Arbeit/workflow.nf"
output = run_nextflow_workflow(workflow_path, args.cleanup)
print(output)
