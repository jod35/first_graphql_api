from sqlalchemy.orm.session import Session
from models import User,engine
from sqlalchemy.orm import sessionmaker


Session=sessionmaker()

local_session=Session(bind=engine)


users=[
    {
        'email':'johndoe@gmail.com',
        'first_name':'John',
        'last_name':'Doe',
    },
    {
        'email':'jeanbillie@gmail.com',
        'first_name':'Billy',
        'last_name':'Jean',
    },
    {
        'email':'johndoe@gmail.com',
        'first_name':'John',
        'last_name':'Doe',
    },
    {
        'email':'lebronjames@gmail.com',
        'first_name':'Lebron',
        'last_name':'James',
    },
    {
        'email':'bensimmens@gmail.com',
        'first_name':'Ben',
        'last_name':'Simmens',
    },
    {
        'email':'thirteen@gmail.com',
        'first_name':'John',
        'last_name':'Sventy',
    },
]

for user in users:
    user_obj=User(email=user['email'],first_name=user['first_name'],
        last_name=user['last_name']
    )

    local_session.add(user_obj)

    local_session.commit()