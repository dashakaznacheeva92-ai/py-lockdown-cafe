from app.cafe import Cafe
from app.errors import (VaccineError, NotVaccinatedError,
                        OutdatedVaccineError, NotWearingMaskError
                        )


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    all_vaccinated = True

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except NotVaccinatedError:
            masks_to_buy += 1
            all_vaccinated = False
        except (VaccineError, OutdatedVaccineError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_to_buy += 1

    if not all_vaccinated:
        return "All friends should be vaccinated"

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
