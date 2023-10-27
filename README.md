# easy-authenticator
Easy-Authenticator: Streamlined Kubernetes RBAC with Endpoint Control, 
Rate-Limiting, and More. Seamlessly integrates with Nginx Ingress and 
Tyk-OSS for quick and hassle-free role-based access control, endpoint management, 
rate-limiting, and fine-grained privileges in your Kubernetes infrastructure.

### HL Diagram


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
 kubectl create secret generic basic-auth --from-file=auth
 kubectl apply -f .\easy-auth-config-map.yaml
 kubectl apply -f .\easy-auth-secrets.yaml
 kubectl apply -f .\postgres-secret.yaml
 kubectl apply -f .\postgres-deployment.yaml
 kubectl apply -f .\postgres-service.yaml
 kubectl apply -f .\easy-auth-deployment.yaml
 kubectl apply -f .\easy-auth-service.yaml
 kubectl apply -f .\redis-easy-auth.yaml
 kubectl apply -f .\bridge_service.yaml
 kubectl apply -f .\ingress.yaml
  kubectl apply -f .\ingress-nginx.yaml
 kubectl apply -f .\ingress-nginx-auth-url.yaml
```

#### Run Tyk-oss
```commandline
export NAMESPACE:"tyk-oss"
export APISecret:foo

helm upgrade tyk-redis oci://registry-1.docker.io/bitnamicharts/redis -n $NAMESPACE --create-namespace --install --set image.tag=6.2.13
helm upgrade tyk-oss tyk-helm/tyk-oss -n $NAMESPACE --create-namespace --install   --set global.secrets.APISecret="$APISecret" --set global.redis.addrs="{tyk-redis-master.$NAMESPACE.svc.cluster.local:6379}" --set global.redis.passSecret.name=tyk-redis --set global.redis.passSecret.keyName=redis-password
 
helm repo add tyk-helm https://helm.tyk.io/public/helm/charts/
helm repo update
helm show values tyk-helm/tyk-oss > values-oss.yaml 

helm install tyk-oss tyk-helm/tyk-oss -n tyk --create-namespace -f values-oss.yaml

```

##### check that pods are up and running
```commandline
kubectl get pods
```

##### open tunnel
```commandline
 minikube tunnel
```

#### Domains:
```text
http://login-local-easy-auth.com/api/auth/ --> for Login No Auth
http://local-easy-auth.com/api/(.*) --> Bearer Token
http://admin-easy-auth.com/api/(.*) --> Basic Auto
```

#### Initial basic auth:
```text
Username: foo
Password: bla

change file auth to change the Initial credentials
```

#### tyk details:
```text
 tyk url: gateway-svc-tyk-oss-tyk-gateway.tyk-oss.svc.cluster.local
```

###### useful commands:

ingress logs:
```commandline
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx
```

Find internal DNS (inside k8s cluster):
```commandline
apt update && apt-get -y install dnsutils
nslookup <service_name>
```

### Start Guide
the starting flow:
Use admin-local-easy-auth.local domain:

##### 1. Create Role  (Auth - basic auth)
```commandline
curl --location 'http://admin-local-easy-auth.com/api/user' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic Zm9vOmJsYQ==' \
--data '{
    "name" : "admin",
    "token": "admin"
}'
```

##### 2. Create User (Auth - basic auth)
```commandline
curl --location 'http://admin-local-easy-auth.com/api/user' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic Zm9vOmJsYQ==' \
--data '{
    "user_name" : "joe",
    "password": "joe_pass",
    "role_id":1
}'
```

##### 3. Create Endpoint (Auth - basic auth)
```commandline
curl --location 'http://admin-local-easy-auth.com/api/endpoint' 
--header 'Content-Type: application/json' 
--header 'Authorization: Basic Zm9vOmJsYQ==' \
--data '{
    "endpoint_name" : "endpoint_name_example",
    "listen_path": <PATH>",
    "target_url":"http://<INTERNAL_CLUSTER_PATH>/api/<PATH>"
}'
```

##### 4. Assign Endpoint to a Role (Auth - basic auth)
```commandline
curl --location 'http://admin-local-easy-auth.com/api/role/endpoint' \
--header 'Content-Type: application/json' \
--header Authorization: Basic Zm9vOmJsYQ==
--data '{
    "api_id" : "endpoint_name_example",
    "role_id": 1
}'
```

##### 4. Login and save the token from the response (Auth - basic auth)
```commandline
curl --location 'http://login-local-easy-auth.com/api/auth/' \
--header 'Content-Type: application/json' \
--data '{
    "user_name" : "joe",
    "password": "joe_pass"
}'
```

##### 5. Try your endpoint :) (Auth - Bearer token)
```commandline
curl --location --request GET 'http://local-easy-auth.com/api/<YOUR_ENDPOINT_PATH>' 
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <TOKEN>' \
```