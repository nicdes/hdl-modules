# --------------------------------------------------------------------------------------------------
# Copyright (c) Lukas Vik. All rights reserved.
#
# This file is part of the hdl_modules project.
# https://hdl-modules.com
# https://gitlab.com/tsfpga/hdl_modules
# --------------------------------------------------------------------------------------------------

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).parent.parent.resolve()
HDL_MODULES_DIRECTORY = REPO_ROOT / "modules"

HDL_MODULES_DOC = REPO_ROOT / "doc"
HDL_MODULES_GENERATED = REPO_ROOT / "generated"

# Do PYTHONPATH insert() instead of append() to prefer any local repo checkout over any pip install
PATH_TO_TSFPGA = REPO_ROOT.parent.resolve() / "tsfpga"
sys.path.insert(0, str(PATH_TO_TSFPGA))
PATH_TO_HDL_REGISTERS = REPO_ROOT.parent.resolve() / "hdl_registers"
sys.path.insert(0, str(PATH_TO_HDL_REGISTERS))
PATH_TO_VUNIT = REPO_ROOT.parent.parent.resolve() / "vunit" / "vunit"
sys.path.insert(0, str(PATH_TO_VUNIT))
