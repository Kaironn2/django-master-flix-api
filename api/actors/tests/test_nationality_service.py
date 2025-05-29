from unittest.mock import patch

from actors.services.nationality_service import get_nationalities


@patch('actors.services.nationality_service.requests.get')
def test_get_nationalities(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {'name': {'common': 'united states'}},
        {'name': {'common': 'canada'}},
        {'name': {'common': 'mexico'}},
    ]

    result = get_nationalities()
    assert result == ['canada', 'mexico', 'united states']
