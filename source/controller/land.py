from fastapi import FastApi


def configure_routes(app: FastApi):
    @app.get("/lands")
    def list_land():
        pass

    @app.get("/land")
    def get_land():
        pass

