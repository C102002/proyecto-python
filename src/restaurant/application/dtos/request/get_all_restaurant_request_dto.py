class GetAllRestaurantRequestDTO:
    def __init__(
        self,
        page: int = 1,
        per_page: int = 10
    ):
        """
        DTO for paginating the list of restaurants.

        :param page: Page number (1-indexed).
        :param per_page: Number of items per page.
        """
        self.page = page
        self.per_page = per_page

    @property
    def offset(self) -> int:
        """Number of records to skip: (page - 1) * per_page."""
        return (self.page - 1) * self.per_page

    @property
    def limit(self) -> int:
        """Number of records to fetch: per_page."""
        return self.per_page

    def __repr__(self):
        return (
            f"GetAllRestaurantRequestDTO("
            f"page={self.page!r}, "
            f"per_page={self.per_page!r}, "
            f"offset={self.offset!r}, "
            f"limit={self.limit!r})"
        )
