import grpc
import argparse

from tensorflow_serving.apis import model_service_pb2
from tensorflow_serving.apis import model_service_pb2_grpc
from tensorflow_serving.apis import model_management_pb2
from tensorflow_serving.config import model_server_config_pb2
from tensorflow_serving.util import status_pb2

from helper import load_config


def options():
    parser = argparse.ArgumentParser(
        description="Reload tensorflow serving server with new config")
    parser.add_argument(
        "-c", "--config", help="Serving config file", required=True)
    parser.add_argument(
        "-H", "--host", help="Tensorflow serving IP with Port", required=True)

    return parser.parse_args()


def main(config_path, host):

    models = load_config(config_path)

    channel = grpc.insecure_channel(host)
    stub = model_service_pb2_grpc.ModelServiceStub(channel)

    request = model_management_pb2.ReloadConfigRequest()

    model_server_config = model_server_config_pb2.ModelServerConfig()
    config_list = model_server_config_pb2.ModelConfigList()

    for model in models:
        image_config = config_list.config.add()
        image_config.name = model['config']['name']
        image_config.base_path = model['config']['base_path']
        image_config.model_platform = model['config']['model_platform']

    model_server_config.model_config_list.CopyFrom(config_list)
    request.config.CopyFrom(model_server_config)

    print(request.ListFields())
    print('Sending request')
    response = stub.HandleReloadConfigRequest(request, 30)
    if response.status.error_code == 0:
        print("Reload successful")
    else:
        print("Reload failed!")
        print(response.status.error_code)
        print(response.status.error_message)


if __name__ == "__main__":
    args = options()
    main(args.config, args.host)
