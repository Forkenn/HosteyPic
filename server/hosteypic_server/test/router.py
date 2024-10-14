from fastapi import APIRouter, Depends
from hosteypic_server.test.schemas import STest
from hosteypic_server.auth.manager import RoleManager
from hosteypic_server.users.models import User

current_moderator = RoleManager(is_moderator=True)

router = APIRouter(prefix='/test', tags=['Test'])

@router.get('/data')
async def get_test(id: int, user: User = Depends(current_moderator)) -> STest:
    test_data = {
        'id': id,
        'username': user.username,
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