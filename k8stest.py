from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
nodes = v1.list_node(watch=False)
for node in nodes.items:
    print (node)