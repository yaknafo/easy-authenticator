# Bandit 
Bandit is a tool designed to find common security issues in Python code. 
To do this Bandit processes each file, builds an AST from it, 
and runs appropriate plugins against the AST nodes. 
Once Bandit has finished scanning all the files it generates a report.

### commands
for one specific file
```commandline
bandit .\service\authentication_service.py
```

for multiple files
```commandline
bandit -r ~/your_repos/project
```

Run Bandit YAML
```commandline
bandit -c bandit.yaml -r .

bandit -c .\app_security\bandit\bandit.yaml -r .
```