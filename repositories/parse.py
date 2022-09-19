from .base import BaseRepository
from models.parse import ParseModel


class ParseRepository(BaseRepository):
    async def return_arguments(self, args: ParseModel) -> ParseModel:
        return ParseModel(arg1=args.arg1, arg2=args.arg2)
