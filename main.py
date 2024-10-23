import trio

from delivery_app import DeliveryApp

app = DeliveryApp()
trio.run(app.async_run, 'trio')
