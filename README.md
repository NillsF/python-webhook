# python-webhook


You should create a cert and key, and configure that as a secret. Cert should be created for domain  test-mutations.default.svc

```bash
openssl req -x509 -sha256 -newkey rsa:2048 -keyout certificate.key -out certificate.crt -days 1024 -nodes
cat certificate.key | base64 -w 0
cat certificate.crt | base64 -w 0
```


```yaml

apiVersion: v1
kind: Secret
metadata:
  name: python-admission-cert
type: Opaque
data:
  tls.crt: [[base64 tlscrt]]
  tls.key: [[base64 tlskey]]
```