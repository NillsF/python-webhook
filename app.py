from flask import Flask, request, jsonify
from kubernetes import client, config

import base64
import logging
import jsonpatch
admission_controller = Flask(__name__)
@admission_controller.route('/mutate/pods', methods=['POST'])
def deployment_webhook_mutate():
    request_info = request.get_json()
    logging.warning("Got request")
    
    # Get OS from Pod
    
    try:
        os_in_pod = request_info["request"]["object"]["spec"]["nodeSelector"]["kubernetes.io/os"]
    except KeyError as e:
        logging.warning("OS not set in node selector. Assuming default Linux.")
        os_in_pod = 'linux'
    logging.warning("OS in pod is {}".format(os_in_pod))

    # Get request from Pod
    logging.warning(request_info["request"]["object"]["spec"])        

    return admission_response_patch(True, "Adding allow label", json_patch = jsonpatch.JsonPatch([{"op": "add", "path": "/metadata/labels/allow", "value": "yes"}]))
def admission_response_patch(allowed, message, json_patch):
    base64_patch = base64.b64encode(json_patch.to_string().encode("utf-8")).decode("utf-8")
    return jsonify({"response": {"allowed": allowed,
                                 "status": {"message": message},
                                 "patchType": "JSONPatch",
                                 "patch": base64_patch}})
if __name__ == '__main__':
    # this is without TLS
    # admission_controller.run(host='0.0.0.0', port=8001,ssl_context='adhoc')
    # this is using TLS
    admission_controller.run(host='0.0.0.0', port=8001,ssl_context=("/var/run/vn-affinity-admission-controller/tls.crt", "/var/run/vn-affinity-admission-controller/tls.key"))