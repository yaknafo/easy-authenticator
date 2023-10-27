# safety 
Safety checks Python dependencies for known security vulnerabilities and suggests the proper remediations for vulnerabilities detected. Safety can be run on developer machines, in CI/CD pipelines and on production systems.

By default it uses the open Python vulnerability database Safety DB, which is licensed for non-commercial use only.
For all commercial projects, Safely must be upgraded to use a PyUp API using the --key option.
[Github](https://github.com/pyupio/safety)

### commands
install safety
```commandline
pip install safety
```
Run safety
```commandline
safety check
```



output
```text
+============================================================================================================================+
 VULNERABILITIES FOUND
+============================================================================================================================+

-> Vulnerability found in certifi version 2022.12.7
   Vulnerability ID: 59956
   Affected spec: >=2015.04.28,<2023.07.22
   ADVISORY: Certifi 2023.07.22 includes a fix for CVE-2023-37920: Certifi prior to version 2023.07.22 recognizes
   "e-Tugra" root certificates. e-Tugra's root certificates were subject to an investigation prompted by reporting of...
   CVE-2023-37920
   For more information, please visit https://pyup.io/v/59956/f17
```