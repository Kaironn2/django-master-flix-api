from typing import Any, List, Optional

from .repository import ReviewRepository
from core.types import ReviewDict


class ReviewService:
    def __init__(self):
        self.review_repository = ReviewRepository()

    def get_reviews(self) -> List[ReviewDict]:
        return self.review_repository.get_reviews()

    def create_review(self, movie: int, stars: int, comment: str) -> Optional[Any]:
        review = dict(
            movie=movie,
            stars=stars,
            comment=comment,
        )
        return self.review_repository.create_review(
            review=review
        )
