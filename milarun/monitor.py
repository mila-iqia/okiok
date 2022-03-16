import time
from threading import Thread

import GPUtil


class GPUMonitor(Thread):
    def __init__(self, runner, delay):
        super().__init__(daemon=True)
        self.runner = runner
        self.stopped = False
        self.delay = delay
        # self.data = {
        #     g.id: dict(
        #         load=[],
        #         memory=[],
        #         temperature=[]
        #     )
        #     for g in GPUtil.getGPUs()
        # }

    def run(self):
        while not self.stopped:
            # for g in GPUtil.getGPUs():
            #     data = self.data[g.id]
            #     data["load"].append(g.load)
            #     data["memory"].append(g.memoryUsed)
            #     data["temperature"].append(g.temperature)
            self.runner.give(gpudata=GPUtil.getGPUs())
            time.sleep(self.delay)

    def stop(self):
        self.stopped = True
