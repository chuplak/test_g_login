

chrome = 'https://www.google.com/'

def test_1(driver, context):
    """
    Description of this test
    """
    context['page'] = driver.get(chrome)
    assert chrome in driver.current_url
