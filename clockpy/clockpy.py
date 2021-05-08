from time import time


class Clockpy:
    def __init__(self):
        self.start = time()
        self.values = [self.start]
        self.times = [0]
        self.labels = ['Start']


    def checkpoint(self, label = None):     
        self.values.append(time())
        self.times.append(self.values[-1] - self.values[-2])
        self.labels.append(label)
        

    def checkpoints(self):
        return { (f'Checkpoint {i} ({self.labels[i]})' if self.labels[i] else f'Checkpoint {i}'): self.times[i] for i in range(1, len(self.times)) }


    def total(self):
        return sum(self.times)


    def shorter(self):
        min_index = self.times.index(min(self.times[1:]))
        check_label = f'Checkpoint {min_index} ({self.labels[min_index]}):' if self.labels[min_index] else f'Checkpoint {min_index}:'

        print(f'{check_label} {min(self.times[1:])}')
    

    def longer(self):
        max_index = self.times.index(max(self.times))
        check_label = f'Checkpoint {max_index} ({self.labels[max_index]}):' if self.labels[max_index] else f'Checkpoint {max_index}:'

        print(f'{check_label} {max(self.times)}')


    def describe(self):
        checks = self.checkpoints()
        print('Total time:', self.total())
        print('Max time:', max(checks.values()))
        print('Min time:', min(checks.values()))
        