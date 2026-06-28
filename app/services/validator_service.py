class ValidatorService:

    def unique(self, page, xpath):

        return page.locator(
            f"xpath={xpath}"
        ).count() == 1