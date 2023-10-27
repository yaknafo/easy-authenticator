# Semgrep 
Semgrep is a fast, open-source, static analysis engine for finding bugs, 
detecting vulnerabilities in third-party dependencies, and enforcing code standards. 
Semgrep analyzes code locally on your computer or in your build environment:
[Github](https://github.com/returntocorp/semgrep#option-1-getting-started-from-the-cli)

### commands
this commands is for usingSemgrep throw docker
```commandline
docker run --rm -v "${PWD}:/src" returntocorp/semgrep semgrep scan 
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