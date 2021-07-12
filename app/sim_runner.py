from simrunner.app.lib.api import get_next_sim, send_report
import os
import subprocess
import time

class SimRunner(object):
    def __init__(self):
        if not os.getenv('API_TIMEOUT'): raise Exception('API_TIMEOUT env is required.')
        if not os.getenv('API_TIMEOUT_STEP'): raise Exception('API_TIMEOUT_STEP env is required.')
        if not os.getenv('WORKSPACE_ROOT'): raise Exception('WORKSPACE_ROOT env is required.')
        self.reset_timer()

    def reset_timer(self):
        self.abort_timer = int(os.getenv('API_TIMEOUT'))

    def decrement_timer(self, t=None):
        if not t:
            self.abort_timer -= int(os.getenv('API_TIMEOUT_STEP'))
            time.sleep(int(os.getenv('API_TIMEOUT_STEP')))
        else:
            self.abort_timer -= int(t)

    def run(self):
        
        while self.abort_timer > 0:
            next_sim = get_next_sim()
            if next_sim == 'empty':
                self.decrement_timer()
            else:
                self.reset_timer()
                workspace_path = os.path.abspath(os.getenv('WORKSPACE_ROOT'))

                start = time.monotonic()
                os.chdir(workspace_path)
                subprocess.run('bazel run //mcSim/simulations:{0}-sim'.format(next_sim).split(' '))
                end = time.monotonic()

                self.decrement_timer(end - start)

if __name__ == '__main__':
    simrunner = SimRunner()
    simrunner.run()