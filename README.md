create env
```bash
conda create -n winq python -y
```

activate env
```bash
conda activate winq
```

created requirement.txt file
installing the requirements
```bash
pip install -r requirements.txt
```

```bash
git init
dvc init
dvc add data_given/winequality_red.csv
```

```bash
git add .
git commit -m "this is my first commit"
```

online update for Readme
```bash 
git add . && git commit -m "update Readme.md"
```

```bash
git remote set-url origin https://github.com/kuntianth14082000/simple_dvc_demo.git
git branch -M main
git push origin main
```

tox command .
```bash
tox
```

for rebuidling .
```bash
tox -r 
```

pytest command
```bash
pytest -v
```

setup command
```bash
pip install -e .
```

build your own packages
```bash
python setyup.py sdist bdist wheel
```