import json

from typing import Dict

CHART_PATH = "chart.json"


class Chart:

    chart = None

    def __init__(self, swap=False):
        self.chart = self.load_chart()
        if swap:
            self.chart = self.swap_chart()

    def __getitem__(self, item):
        return self.chart[item]

    @classmethod
    def load_chart(cls) -> Dict[str, str]:
        with open(CHART_PATH) as ch:
            chart = ch.read()
        return json.loads(chart)

    @classmethod
    def swap_chart(cls):
        cls.chart = {v: k for k, v in cls.load_chart().items()}
        return cls.chart
