from abc import ABC, abstractmethod

from src.common.application.notifier.notifier import Notifier

class LoggerNotifier(Notifier):

    def notify(self,message:str) -> None:
        print(f"Notificacion Entrante: {message}")