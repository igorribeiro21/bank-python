from pydantic import BaseModel,constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def create_person_pj_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        faturamento: float
        idade: int
        nome_fantasia: constr(min_length=1) # type: ignore
        celular: constr(min_length=10, max_length=10) # type: ignore
        email_corporativo: constr(min_length=10) # type: ignore
        categoria: str
        saldo: float
    
    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
