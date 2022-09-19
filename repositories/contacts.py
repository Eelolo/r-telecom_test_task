from typing import List
from .base import BaseRepository
from db.contacts import contacts
from models.contact import Contact, ContactIn
from datetime import datetime


class ContactRepository(BaseRepository):
    async def get_all(self, limit: int = 100, skip: int = 0) -> List[Contact]:
        query = contacts.select().limit(limit).offset(skip)
        contacts_data = await self.database.fetch_all(query=query)

        return contacts_data

    async def get_by_id(self, contact_id: int) -> Contact:
        query = contacts.select().where(contacts.c.id==contact_id)
        contact = await self.database.fetch_one(query=query)

        if not contact:
            return None
        else:
            return Contact.parse_obj(contact)

    async def create(self, c: ContactIn) -> Contact:
        contact = Contact(
            first_name=c.first_name,
            last_name=c.last_name,
            patronymic=c.patronymic,
            phone=c.phone,
            email=c.email,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        values = {**contact.dict()}
        values.pop('id', None)
        query = contacts.insert().values(**values)
        contact.id = await self.database.execute(query)

        return contact

    async def update(self, contact_id: int, c: ContactIn) -> Contact:
        contact = Contact(
            id=contact_id,
            first_name=c.first_name,
            last_name=c.last_name,
            patronymic=c.patronymic,
            phone=c.phone,
            email=c.email,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        values = {**contact.dict()}
        values.pop('id', None)
        values.pop('created_at', None)
        query = contacts.update().where(contacts.c.id==contact_id).values(**values)
        await self.database.execute(query)

        return contact

    async def delete(self, contact_id: int) -> Contact:
        query = contacts.delete().where(contacts.c.id==contact_id)
        contact = await self.database.execute(query=query)

        return contact
