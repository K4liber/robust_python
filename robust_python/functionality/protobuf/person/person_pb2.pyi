from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Person(_message.Message):
    __slots__ = ["email", "id", "name", "phones"]
    class PhoneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class PhoneNumber(_message.Message):
        __slots__ = ["number", "type"]
        NUMBER_FIELD_NUMBER: ClassVar[int]
        TYPE_FIELD_NUMBER: ClassVar[int]
        number: str
        type: Person.PhoneType
        def __init__(self, number: Optional[str] = ..., type: Optional[Union[Person.PhoneType, str]] = ...) -> None: ...
    EMAIL_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    PHONES_FIELD_NUMBER: ClassVar[int]
    PHONE_TYPE_HOME: Person.PhoneType
    PHONE_TYPE_MOBILE: Person.PhoneType
    PHONE_TYPE_UNSPECIFIED: Person.PhoneType
    PHONE_TYPE_WORK: Person.PhoneType
    email: str
    id: int
    name: str
    phones: _containers.RepeatedCompositeFieldContainer[Person.PhoneNumber]
    def __init__(self, name: Optional[str] = ..., id: Optional[int] = ..., email: Optional[str] = ..., phones: Optional[Iterable[Union[Person.PhoneNumber, Mapping]]] = ...) -> None: ...
