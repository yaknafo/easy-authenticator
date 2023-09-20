from models.models import Endpoint
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
