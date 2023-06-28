# template_tfdc
1. Go to your designated parent folder.
2. Run the following command in terminal, note this will only works in windows. (copy-paste will do)
```bash
git clone --depth=1 --branch=main https://github.com/Lawytel/template_tfdc.git your_project_name && cd your_project_name && rd /s /q .git && cd ..
```
3. Open the project inside PyCharm.
4. Set your environment, be sure to use python version 3.8.*, then activate your environment.
5. In the terminal, run the following command, then wait until it finish downloading all the packages
```bash
pip install -r requirements.txt
```
6. Run the environment_test.py. If there's an error, be sure you have the correct package versions.
