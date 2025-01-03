import subprocess
import argparse
import os

def parse():
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('-c', '--cleanup',
                        action='store_true',
                        help="cleans workdir")
    parser.add_argument('-nc', '--nocleanup',
                        action='store_true',
                        help="all the temporary data of the workflow is saved")
    return parser.parse_args()

def run_nextflow_workflow(workflow_path, cleanup, nocleanup):
    if cleanup:
        command = ["nextflow", "run", workflow_path, "--cleanup"]
    if nocleanup:
        command = ["nextflow", "run", workflow_path]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

args = parse()
os.curdir
workflow_path = "workflow.nf"
output = run_nextflow_workflow(workflow_path, args.cleanup, args.nocleanup)

if os.path.exists(".nextflow.log"):
    with open(".nextflow.log", "r") as logfile:
        log = logfile.read()
        print(log)
    os.remove(".nextflow.log")

print(output)
