import logging
import re
import json
from typing import Set, Dict, Optional

import requests
from requests.exceptions import RequestException

logger = logging.getLogger(__name__)

class SubdomainFinder:
    """
    A class to find subdomains for a given domain using the crt.sh API.
    """
    BASE_URL = "https://crt.sh/"

    def __init__(self, domain: str, headers: Dict[str, str], complete_scan: bool = False):
        """
        Initializes the SubdomainFinder.

        Args:
            domain (str): The target domain.
            headers (Dict[str, str]): HTTP headers for the request.
            complete_scan (bool): If True, includes expired certificates in the scan.
        """
        self.domain = self._validate_domain(domain)
        self.complete_scan = complete_scan
        self.session = requests.Session()
        self.session.headers.update(headers)
        logger.debug("SubdomainFinder initialized for domain '%s' with complete_scan=%s", self.domain, self.complete_scan)

    @staticmethod
    def _validate_domain(domain: str) -> str:
        """
        Validates the domain format.

        Args:
            domain (str): The domain to validate.

        Returns:
            str: The validated domain.

        Raises:
            ValueError: If the domain format is invalid.
        """
        pattern = re.compile(r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})+$')
        if not pattern.match(domain):
            raise ValueError(f"Invalid domain format: {domain}")
        return domain.lower()
    
    def _make_request(self) -> Optional[requests.Response]:
        """
        Makes a request to the crt.sh API.

        Returns:
            Optional[requests.Response]: The response object if successful, otherwise None.
        
        Raises:
            ConnectionError: If a network-related error occurs.
        """
        params = {'q': self.domain, 'output': 'json'}
        if not self.complete_scan:
            params['exclude'] = 'expired'
        
        logger.info("Querying crt.sh for domain: %s", self.domain)
        try:
            response = self.session.get(self.BASE_URL, params=params, timeout=None)
            response.raise_for_status()
            logger.debug("Successfully received response from crt.sh (Status: %d)", response.status_code)
            return response
        except RequestException as e:
            logger.error("Failed to connect to crt.sh: %s", e)
            raise ConnectionError(f"A network error occurred while contacting crt.sh: {e}") from e
    
    @staticmethod
    def _parse_response(response_text: str) -> Set[str]:
        """
        Parses the JSON response from crt.sh to extract unique subdomains.

        Args:
            response_text (str): The JSON response text.

        Returns:
            Set[str]: A set of unique subdomains.
        """
        subdomains = set()
        try:
            data = json.loads(response_text)
            for entry in data:
                names = entry.get('name_value', '').split('\n')
                for name in names:
                    if name and not name.startswith('*.'):
                        subdomains.add(name.strip())
            logger.debug("Parsed %d unique subdomains from the response.", len(subdomains))
            return subdomains
        except json.JSONDecodeError:
            logger.error("Failed to decode JSON response from crt.sh.")
            return set()

    def discover(self) -> Set[str]:
        """
        Orchestrates the subdomain discovery process.

        Returns:
            Set[str]: A set of found subdomains.
        """
        response = self._make_request()
        if response:
            return self._parse_response(response.text)
        return set()