import time

from functions_dir.base import Base
from . import constant as const

CALCULATE_ENERGY_REQUIREMENTS = const.CALCULATE_ENERGY_REQUIREMENTS_URL


class CalculateEnergyRequirements(Base):
    def fill_base_metabolism(self):
        self.implicitly_wait(2)
        time.sleep(5)
        shadow_root_1 = self.execute_script(
            """return document.querySelector("td-calculator")
            .shadowRoot.querySelector("iron-pages[attr-for-selected='name']")"""
        )

        print(shadow_root_1)
