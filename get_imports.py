import glob
from pathlib import Path


def get_imports(path):
    fid = Path(path).read_text().split("\n")
    for line in fid:
        if line.__contains__("import "):
            print(line)


dir_path = r"C:\Users\Vadim\Documents\GitHub\Python\Pandas-Numpy-Notebooks\*.ipynb"
for f_path in glob.glob(dir_path):
    # print(f_path)
    get_imports(f_path)

    """    
    "import numpy as np"
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
    "import zipfile\n",
    "from pandarallel import pandarallel\n",
    "import swifter"
    "import dask"
    "from numba import jit"
    "import zipfile\n",
    "import zipfile\n",
    "import great_expectations as ge\n",
    "kag_ge = ge.from_pandas(kag)"
    "import json\n",
    "import calendar\n",
    """
