# GitLeaks 
Gitleaks is a SAST tool for detecting and preventing hardcoded secrets like passwords, 
api keys, and tokens in git repos. Gitleaks is an easy-to-use, 
all-in-one solution for detecting secrets, past or present, in your code.

### commands
this commands is for using git-leaks throw docker
```commandline
docker pull ghcr.io/gitleaks/gitleaks:latest
```

Run the following command to find if there are secrets committed in your git repository

```commandline
docker run --rm -v <LOCAL_PATH_TO_YOUR_PROJECT_FOLDER>>/path ghcr.io/gitleaks/gitleaks:latest detect -s /path
```

make sure that I don’t commit any secret in my git source code repository

```commandline
docker run --rm -v <LOCAL_PATH_TO_YOUR_PROJECT_FOLDER>>/path ghcr.io/gitleaks/gitleaks:latest protect -s /path
```

The output should look like this
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