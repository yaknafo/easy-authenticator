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


#### MiniKube With Ingress

Before starting:
```commandline
 minikube addons enable ingress
```

```commandline
 kubectl apply -f .\easy-auth-config-map.yaml
 kubectl apply -f .\easy-auth-secrets.yaml
 kubectl apply -f .\postgres-secret.yaml
 kubectl apply -f .\postgres-deployment.yaml
 kubectl apply -f .\postgres-service.yaml
 kubectl apply -f .\easy-auth-deployment.yaml
 kubectl apply -f .\easy-auth-service.yaml
 kubectl apply -f .\ingress.yaml
```

##### check that pods are up and running
```commandline
kubectl get pods
```

##### open tunnel
```commandline
 minikube tunnel
```