import ffratings.enums as ffenums


class FantasyClient:
    """Base Client for return Fantasy Draft projections"""

    def __init(self):
        return

    def get_projections(self, source: ffenums.Source, position: ffenums.Position):
        if source.value == ffenums.Source.BetIQ.value:
            return self.get_betiq_data(position)

    def get_betiq_data(self, position: ffenums.Position):
        return position
