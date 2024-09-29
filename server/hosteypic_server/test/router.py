from fastapi import APIRouter
from hosteypic_server.test.schemas import STest

router = APIRouter(prefix='/test', tags=['Test'])

@router.get('/data')
async def get_test(id: int) -> STest:
    test_data = {
        'id': id,
        'username': 'Golovach',
        'phone_number': '+79206538525',
        'email': 'golovach@mail.ru',
        'year': '2023',
        'random_num': '52',
        'optional_field': 'Hello World!'
    }
    
    return test_data

@router.post('/data')
async def send_test(request_body: STest) -> STest:
    return request_body