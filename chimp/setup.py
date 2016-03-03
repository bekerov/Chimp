import os
import subprocess
import numpy

np_path = numpy.__file__
source_path = os.path.dirname(os.path.realpath("setup.py"))

np_split = np_path.split("/")
target_path = '/'.join(np_split[:-2]) + "/chimp"

# symlink to the site packages dir
cmd = "ln -s " + source_path + " " + target_path

subprocess.call([cmd], shell=True)


