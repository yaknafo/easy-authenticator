# easy-authenticator
easy out-of-the-box authentication for prototype project

## Run locally
```
pip install -r .\requirements.txt  
uvicorn main:app --host 127.0.0.1 --port 9110
```

## Docker
```
docker compose up --build
```


## Kubectl
#### To access the gateway run
```
kubectl port-forward svc/tyk-svc 8080:8080

minikube service easy-auth --url
```
