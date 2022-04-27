import datetime
from progress.bar import IncrementalBar
import time


class ProgressBar(IncrementalBar):
    message = 'Progress'
    suffix  = '%(percent).1f%% (%(index)d/%(max)d) -- %(elapsed_min)s (eta: %(eta_min)s)'

    def formatTime(self, seconds):
        return str(datetime.timedelta(seconds=seconds))

    @property
    def elapsed_min(self):
        return self.formatTime(self.elapsed)

    @property
    def eta_min(self):
        return self.formatTime(self.eta)

if __name__=='__main__':
    counter = 10
    bar     = ProgressBar('Processing', max=counter)

    for i in range(counter):
        bar.next()
        time.sleep(1)

    bar.finish()
