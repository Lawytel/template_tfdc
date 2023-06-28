def test_env():
    import sys
    if sys.base_prefix == sys.prefix:
        print("You are probably not using virtual environment on this project.")
    assert sys.version_info[:2] == (3, 8), "Use python 3.8"
    print("You are currently using Python", sys.version)
    print('version & environment are all good')

def test_packages():
    import tensorflow as tf
    import tensorflow_datasets as tfds
    import PIL
    import pandas as pd
    import numpy as np
    import scipy
    assert tf.__version__ == '2.9.0', f"Tensorflow version isn't 2.9.0, yours currently in {tf.__version__}"
    assert tfds.__version__ == '4.6.0', f"Tensorflow dataset version isn't 4.6.0, yours currently in {tfds.__version__}"
    assert PIL.__version__ == '9.1.1', f"Pillow version isn't 9.1.1, yours currently in {PIL.__version__}"
    assert pd.__version__ == '1.4.2', f"pandas version isn't 1.4.2, yours currently in {pd.__version__}"
    assert np.__version__ == '1.22.4', f"numpy version isn't 1.22.4, yours currently in {np.__version__}"
    assert scipy.__version__ == '1.7.3', f"scipy version isn't 1.7.3, yours currently in {scipy.__version__}"
    print('Packages are all good')

if __name__ == '__main__':
    test_env()
    test_packages()
    print('All good. You are ready to go.')

