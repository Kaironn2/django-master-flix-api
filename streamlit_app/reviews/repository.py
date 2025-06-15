from typing import Any, Optional

from core.base_repository import BaseRepository
from core.types import ReviewCreateDict, ReviewDict


class ReviewRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self._reviews_url = self._base_url + 'reviews/'

    def get_reviews(self) -> ReviewDict:
        return self._handle_retrieve(self._reviews_url)

    def create_review(self, review: ReviewCreateDict) -> Optional[Any]:
        return self._handle_create(
            url=self._reviews_url,
            data=review
        )
