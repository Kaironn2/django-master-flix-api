from typing import Any, List, Optional

from core.types import ActorDict, NationalityDict
from core.base_repository import BaseRepository


class ActorRepository(BaseRepository):

    def __init__(self):
        super().__init__()
        self._actors_url = self._base_url + 'actors/'
        self._nationalities_url = self._actors_url + 'nationalities/'

    def get_actors(self) -> List[ActorDict]:
        return self._handle_retrieve(url=self._actors_url)

    def create_actor(self, actor: ActorDict) -> Optional[Any]:
        return self._handle_create(
            url=self._actors_url,
            data=actor,
        )

    def get_nationalities(self) -> List[NationalityDict]:
        return self._handle_retrieve(url=self._nationalities_url)
