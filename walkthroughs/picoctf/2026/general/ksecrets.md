# URL
https://learn.cylabacademy.org/library/732
# Concept
* interacting with a Kubernetes cluster
* using the kubectl tool
# Method of Solve
Once we have the kubeconfig file downloaded, we can setup our environment to use it:
```
export KUBECONFIG=./kubeconfig
```
And then replace the host and port in the kubeconfig file with the one we are provided by the challenge:
```
sed -i 's|127.0.0.1:6443|green-hill.picoctf.net:51182|g' kubeconfig
```
Then we can list out all the namespaces in the cluster
```
kubectl get nodes --insecure-skip-tls-verify
```
Nothing here. Let's get the secret objects and output to a file
```
kubectl get secrets --all-namespaces --insecure-skip-tls-verify > secrets.txt
```
With the name of the secret and the namespace, we can access it directly:
```
kubectl get secret ctf-secret -n picoctf -o yaml --insecure-skip-tls-verify
```
It's base64 encoded
```
echo -n 'encoded_data' | base64 -d
```

