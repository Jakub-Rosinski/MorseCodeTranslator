from chart.chart import Chart


class Telegraph(Chart):
    def __init__(self, swap):
        super().__init__()
        self.encoder = Chart()
        self.decoder = Chart(swap=swap)
