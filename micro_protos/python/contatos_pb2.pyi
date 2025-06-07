from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TipoTelefone(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_TELEFONE_INDEFINIDO: _ClassVar[TipoTelefone]
    TIPO_MOVEL: _ClassVar[TipoTelefone]
    TIPO_FIXO: _ClassVar[TipoTelefone]
    TIPO_COMERCIAL: _ClassVar[TipoTelefone]

class CategoriaContato(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CATEGORIA_CONTATO_INDEFINIDO: _ClassVar[CategoriaContato]
    CATEGORIA_AMIGO: _ClassVar[CategoriaContato]
    CATEGORIA_FAMILIA: _ClassVar[CategoriaContato]
    CATEGORIA_COMERCIAL: _ClassVar[CategoriaContato]
    CATEGORIA_OUTROS: _ClassVar[CategoriaContato]
TIPO_TELEFONE_INDEFINIDO: TipoTelefone
TIPO_MOVEL: TipoTelefone
TIPO_FIXO: TipoTelefone
TIPO_COMERCIAL: TipoTelefone
CATEGORIA_CONTATO_INDEFINIDO: CategoriaContato
CATEGORIA_AMIGO: CategoriaContato
CATEGORIA_FAMILIA: CategoriaContato
CATEGORIA_COMERCIAL: CategoriaContato
CATEGORIA_OUTROS: CategoriaContato

class Telefone(_message.Message):
    __slots__ = ("numero", "tipo")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    numero: str
    tipo: TipoTelefone
    def __init__(self, numero: _Optional[str] = ..., tipo: _Optional[_Union[TipoTelefone, str]] = ...) -> None: ...

class Contato(_message.Message):
    __slots__ = ("id", "nome", "email", "telefones", "categoria")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TELEFONES_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    email: str
    telefones: _containers.RepeatedCompositeFieldContainer[Telefone]
    categoria: CategoriaContato
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., email: _Optional[str] = ..., telefones: _Optional[_Iterable[_Union[Telefone, _Mapping]]] = ..., categoria: _Optional[_Union[CategoriaContato, str]] = ...) -> None: ...

class ListaContatos(_message.Message):
    __slots__ = ("contatos",)
    CONTATOS_FIELD_NUMBER: _ClassVar[int]
    contatos: _containers.RepeatedCompositeFieldContainer[Contato]
    def __init__(self, contatos: _Optional[_Iterable[_Union[Contato, _Mapping]]] = ...) -> None: ...

class StatusResposta(_message.Message):
    __slots__ = ("sucesso", "mensagem")
    SUCESSO_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    sucesso: bool
    mensagem: str
    def __init__(self, sucesso: bool = ..., mensagem: _Optional[str] = ...) -> None: ...

class ConsultarContatoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListarContatosRequest(_message.Message):
    __slots__ = ("categoria", "nome")
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    categoria: CategoriaContato
    nome: str
    def __init__(self, categoria: _Optional[_Union[CategoriaContato, str]] = ..., nome: _Optional[str] = ...) -> None: ...
