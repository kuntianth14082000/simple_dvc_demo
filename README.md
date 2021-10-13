create env
'''bash
conda create -n winq python -y
'''

activate env
'''bash
conda activate winq
'''

created requirement.txt file
installing the requirements
'''bash
pip install -r requirements.txt
'''

git init
dvc init
dvc add data_given/winequality_red.csv