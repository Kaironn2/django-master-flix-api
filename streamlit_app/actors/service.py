from datetime import datetime
from typing import Any, List, Optional

import streamlit as st

from core.types import ActorDict, NationalityDict
from actors.repository import ActorRepository


class ActorService:

    def __init__(self) -> None:
        self.actor_repository = ActorRepository()

    def get_actors(self) -> List[ActorDict]:
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.actor_repository.get_actors()
        st.session_state.actors = actors
        return actors

    def create_actor(self, name: str, birthday: datetime, nationality: int) -> Optional[Any]:
        actor = {
            'name': name,
            'birthday': birthday,
            'nationality': nationality,
        }
        new_actor = self.actor_repository.create_actor(actor=actor)
        st.session_state.actors.append(new_actor)
        return new_actor

    def get_nationalities(self) -> List[NationalityDict]:
        if 'nationalities' in st.session_state:
            return st.session_state.nationalities
        nationalities = self.actor_repository.get_nationalities()
        st.session_state.nationalities = nationalities
        return nationalities
