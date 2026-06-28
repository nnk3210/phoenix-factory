"""
PAAL Exporter
"""

from phoenix_factory.paal.model import PAAL


class PAALExporter:

    @staticmethod
    def export(paal: PAAL) -> str:

        return f"""PAAL: {paal.version}

Project: {paal.project}

Asset: {paal.asset_name}

Category: {paal.category}

Part: {paal.part}

Output: {paal.output}

Background: {paal.background}

Canvas: {paal.canvas}

Pivot: {paal.pivot}

View: {paal.view}

Style: {paal.style}
"""