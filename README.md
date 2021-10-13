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

git add .
git commit -m "this is my first commit"

online update for Readme 
git add . && git commit -m "update Readme.md"

git remote set-url origin https://github.com/kuntianth14082000/simple_dvc_demo.git
git branch -M main
git push origin main



