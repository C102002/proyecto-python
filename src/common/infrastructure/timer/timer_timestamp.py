from src.common.application import ITimer
import time

class TimerTimestamp(ITimer):

    def get_time(self, time1: float, time2: float) -> float:
        return time2 - time1
    
    def set_time(self) -> float:
        return time.time()
    
