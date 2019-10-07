from bs4 import BeautifulSoup

from .utils.constants import BASE_URL
from .utils.helpers import get_session, request


def get_team(team):
    """
    :desc: Retrieves team information.
    :param: `team` Name of the team.
    :return: `resps` response information array
    """

    session = get_session()
    url = BASE_URL + '/teams/view/' + team
    req_obj = request(session, 'GET', url)
    resps = []

    if req_obj.status_code == 200:
        soup = BeautifulSoup(req_obj.text, 'html.parser')
        header = soup.find_all('table')[1].text.strip()
        details = header + '\n' + soup.find_all('table')[2].text.strip()

        resps = [{'data': details}]

    elif req_obj.status_code == 404:
        resps = [{'code': 404,
                  'data': 'Team not found.'}]

    elif req_obj.status_code == 503:
        resps = [{'code': 503,
                  'data': 'Service unavailable.'}]

    return resps
