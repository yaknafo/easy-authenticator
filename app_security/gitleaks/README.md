# GitLeaks 
Gitleaks is a SAST tool for detecting and preventing hardcoded secrets like passwords, 
api keys, and tokens in git repos. Gitleaks is an easy-to-use, 
all-in-one solution for detecting secrets, past or present, in your code.

### commands
this commands is for using git-leaks throw docker
```commandline
docker pull ghcr.io/gitleaks/gitleaks:latest

docker run --rm -v <LOCAL_PATH_TO_YOUR_PROJECT_FOLDER>>/path ghcr.io/gitleaks/gitleaks:latest detect -s /path
```

The output should look like this"
```text

    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

10:07AM INF 42 commits scanned.
10:07AM INF scan completed in 12.9s
10:07AM INF no leaks found
```