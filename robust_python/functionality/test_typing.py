from robust_python.functionality.protobuf.person import Person


def test_person():
    try:
        person = Person(
            id='test_id'
        )
        raise AssertionError('TypeError should be raised')
    except TypeError:
        pass
    
    person = Person(
        id=123,
        name='Bill'
    )
    person.name = 'Michael'
    person.email = 'test@test.com'
    assert 'Michael' == person.name
    assert 123 == person.id
