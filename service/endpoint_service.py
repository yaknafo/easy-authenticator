import service.tyk_token.tyk_helper as tyk_helper
from schema.endpoint import CreateEndpointSchema


class EndpointService(object):

    def CreateEndpoint(self, endpoint: CreateEndpointSchema):
        tyk_helper.create_endpoint(endpoint.endpoint_name, endpoint.listen_path, endpoint.target_url)
