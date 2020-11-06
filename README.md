# python-webhook


You should create a cert and key, and configure that as a secret. 

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