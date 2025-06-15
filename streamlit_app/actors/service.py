from datetime import datetime
from typing import Any, List, Optional

from core.types import ActorDict, NationalityDict
from actors.repository import ActorRepository


class ActorService:

    def __init__(self) -> None:
        self.actor_repository = ActorRepository()

    def get_actors(self) -> List[ActorDict]:
        return self.actor_repository.get_actors()

    def create_actor(self, name: str, birthday: datetime, nationality: int) -> Optional[Any]:
        actor = {
            'name': name,
            'birthday': birthday,
            'nationality': nationality,
        }
        return self.actor_repository.create_actor(actor=actor)

    def get_nationalities(self) -> List[NationalityDict]:
        return self.actor_repository.get_nationalities()
