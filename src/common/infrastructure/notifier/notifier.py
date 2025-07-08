from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from src.common.application.notifier.notifier import Notifier

console = Console()

class RichLoggerNotifier(Notifier):
    """
    Notifier que usa Rich para imprimir un panel coloreado con timestamp.
    """

    def notify(self, message: str) -> None:
        # Genera timestamp
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Crea un encabezado estilizado
        header = Text.assemble(
            ("🔔 Notification ", "bold white on blue"),
            (f"{now}", "italic yellow")
        )

        # Imprime un panel con borde y colores
        console.print(
            Panel(
                message,
                title=header,
                border_style="magenta",
                padding=(1, 2)
            )
        )
