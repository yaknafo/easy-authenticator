from models.models import Endpoint, RoleEndpoint
from utils.db_connector import get_session


class EndpointDal(object):

    def __init__(self):
        self.model = Endpoint

    def get_all_endpoint(self):
        session = get_session()
        endpoints = session.query(self.model).all()
        session.close()
        return endpoints

    def create_endpoint(self, endpoint: Endpoint) -> Endpoint:
        session = get_session()
        session.add(endpoint)
        session.commit()
        endpoint_db = session.query(self.model).filter_by(api_id=endpoint.api_id).first()
        session.close()
        return endpoint_db

    def delete_role_endpoint(self, api_id: str) -> None:
        session = get_session()
        endpoint_to_delete = session.query(self.model).filter_by(api_id=api_id).first()

        if endpoint_to_delete:

            # Query the database to find the role by its ID
            role_endpoints_to_delete = session.query(RoleEndpoint).filter_by(api_id=api_id)
            for re in role_endpoints_to_delete:
                session.delete(re)
            session.delete(endpoint_to_delete)
            session.commit()
        session.close()
