"""Configurações necessarias"""

from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY

marvel = Marvel(PUBLIC_KEY=PUBLIC_KEY, PRIVATE_KEY=PRIVATE_KEY)

SECRET_KEY = '*********'

SQLALCHEMY_DATABASE_URI = "*************"