# kics by checkmarx 
Find security vulnerabilities, compliance issues, and infrastructure misconfigurations 
early in the development cycle of your infrastructure-as-code with KICS by Checkmarx.

KICS stands for Keeping Infrastructure as Code Secure, it is open source and is a must-have for any cloud native project.
[Github](https://github.com/Checkmarx/kics)

### commands
this commands  for using kics throw docker
```
docker run -t -v "{$PWD}:/path" checkmarx/kics:latest scan -p /path -o "/path/"
```

output
```text
┌──────────────┐
│ Scan Summary │
└──────────────┘
Some files were skipped or only partially analyzed.
  Scan was limited to files tracked by git.

Ran 1101 rules on 75 files: 13 findings.
```