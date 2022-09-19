from repositories.contacts import ContactRepository
from db.base import database


def get_contact_repository() -> ContactRepository:
    return ContactRepository(database)
