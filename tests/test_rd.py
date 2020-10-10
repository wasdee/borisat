import pytest
from loguru import logger

from borisat import get_info
from borisat import is_exist


@pytest.fixture
def tax_id():
    return "0105558096348"

def test_get_info(tax_id):
    company = get_info(tax_id=tax_id)
    logger.info(company)
    assert company

def test_is_exists(tax_id):
    assert is_exist(tax_id=tax_id)