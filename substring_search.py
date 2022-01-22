def substring_test(full_string ,substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

substring_test('fulltext', 'some_value')
