from .kernels import handlers as kernels_handlers, websocket as kernels_websocket
from .kernelspecs import handlers as kernelspecs_handlers

from jupyter_server.extension.application import ExtensionApp


class KernelsExtensionApp(ExtensionApp):

    name = "jupyter_server_kernels"

    kernels_available = False

    def initialize_settings(self):
        self.initialize_configurables()
        self.settings.update(dict(kernels_available=True))

    def initialize_handlers(self):
        self.handlers.extend(kernels_websocket.default_handlers)
        self.handlers.extend(kernels_handlers.default_handlers)
        self.handlers.extend(kernelspecs_handlers.default_handlers)
        self.serverapp.web_app.settings["kernels_available"] = self.settings[
            "kernels_available"
        ]
