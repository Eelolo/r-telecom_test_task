from typing import List
from fastapi import APIRouter, Depends
from repositories.contacts import ContactRepository
from .depends import get_contact_repository
from models.contact import Contact


router = APIRouter()


@router.get('/', response_model=List[Contact])
async def list_contacts(
            contacts: ContactRepository = Depends(get_contact_repository),
            limit: int = 100,
            skip: int = 0
        ):
    contacts_data = await contacts.get_all(limit=limit, skip=skip)

    return contacts_data


@router.get('/{contact_id}')
async def get_contact(contact_id: int, contacts: ContactRepository = Depends(get_contact_repository)):
    contact = await contacts.get_by_id(contact_id=contact_id)

    return contact


@router.post('/{contact_id}', response_model=Contact)
async def create_contact(
            contact: Contact,
            contacts: ContactRepository = Depends(get_contact_repository)
        ):
    contact_data = await contacts.create(c=contact)

    return contact_data


@router.put('/{contact_id}')
async def update_contact(
            contact_id: int,
            contact: Contact,
            contacts: ContactRepository = Depends(get_contact_repository)
        ):
    contact_data = await contacts.update(contact_id=contact_id, c=contact)

    return contact_data


@router.delete('/{contact_id}')
async def delete_contact(
            contact_id: int,
            contacts: ContactRepository = Depends(get_contact_repository)
        ):
    contact_data = await contacts.delete(contact_id=contact_id)

    return contact_data
