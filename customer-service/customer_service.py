from flask import jsonify, Flask
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)

CONTEXT_PATH = "/customer-service"
SERVER_PORT = 5000
EUREKA_SERVICE = 'http://localhost:8761/eureka'

eureka_client.init(
    eureka_server=EUREKA_SERVICE,
    app_name="CUSTOMER-SERVICE",
    instance_port=SERVER_PORT
)

@app.route(f'{CONTEXT_PATH}/customers', methods=["GET"])
def get_customer():
    customers = [
        {"id": 1, "name": "Kamal"},
        {"id": 2, "name": "Nima"}
    ]
    return jsonify(customers)


if __name__ == "__main__":
    app.run(port=SERVER_PORT, debug=True)