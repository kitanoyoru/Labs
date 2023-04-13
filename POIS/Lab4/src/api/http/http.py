import json

import requests

from requests.sessions import Session
from requests.adapters import HTTPAdapter, Retry


class HttpFirstLabAPI:
    def __init__(self, host = "http://localhost:8080") -> None:
        self._control_url = host + "/control"
        self._session = self.__init_session()

    def send_drought_action(self) -> dict:
        data = json.dumps({"action": 1})
        headers={"Content-Type": "application/json"}

        self._session.post(self._control_url, data=data, headers=headers)

        return self.__get_latest()

    def send_irrigation_action(self) -> dict:
        data = json.dumps({"action": 2})
        headers={"Content-Type": "application/json"}

        self._session.post(self._control_url, data=data, headers=headers)

        return self.__get_latest()

    def get_info(self) -> None:
        return self.__get_latest()

    def __get_latest(self) -> dict:
        response = self._session.get(self._control_url)
        data = response.json()["message"]["fruit_garden"]
        return data

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

