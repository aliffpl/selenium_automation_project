def assert_equal(actual, expected, message=None):
    if message is None:
        message = f"Expected '{expected}', got '{actual}'"
    assert actual == expected, message

def assert_true(expr, message=None):
    if message is None:
        message = f"Expected expression to be True, got {expr}"
    assert expr, message

def assert_false(expr, message=None):
    if message is None:
        message = f"Expected expression to be False, got {expr}"
    assert not expr, message
