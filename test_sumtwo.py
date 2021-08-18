from main import sumtwo

def test_one():
    input = 1
    expected = 2
    result = sumtwo(input)
    assert result == expected

def test_two():
    input = 2
    expected = 4
    result = sumtwo(input)
    assert result == expected

def test_ten():
    input = 10
    expected = 20
    result = sumtwo(input)
    assert result == expected
