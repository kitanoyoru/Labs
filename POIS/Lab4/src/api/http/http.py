import requests

from requests.sessions import Session
from requests.adapters import HTTPAdapter, Retry


class HttpFirstLabAPI:
    def __init__(self, host = "http://localhost:8080") -> None:
        self._control_url = host + "/control"
        self._session = self.__init_session()

    def send_drought_action(self) -> None:
        data = {"action": 1}
        self._session.post(self._control_url, data=data)

    def send_irrigation_action(self) -> None:
        data = {"action": 2}
        self._session.post(self._control_url, data=data)

    def get_info(self) -> None:
        response = self._session.get(self._control_url)
        return response.json()

    def __init_session(self, retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None,) -> Session:
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)

        session.mount('http://', adapter)
        session.mount('https://', adapter)

        return session

