import service.tyk_token.tyk_helper as tyk_helper
from dal.endpoint_dal import EndpointDal
from models.models import Endpoint
from schema.endpoint import CreateEndpointSchema


class EndpointService(object):

    def __init__(self):
        self.dal = EndpointDal()

    def get_endpoints(self):
        return self.dal.get_all_endpoint()

    def CreateEndpoint(self, endpoint: CreateEndpointSchema) -> Endpoint:
        endpoint_entry = Endpoint(api_id=endpoint.endpoint_name, listen_path=endpoint.listen_path,
                                  target_url=endpoint.target_url, auth_header_name="Authorization")
        endpoint_entry = self.dal.create_endpoint(endpoint_entry)
        tyk_helper.create_endpoint(endpoint.endpoint_name, endpoint.listen_path, endpoint.target_url)
        return endpoint_entry

    def delete_endpoint(self, api_id: str):
        tyk_helper.delete_endpoint(api_id)
        self.dal.delete_role_endpoint(api_id)
