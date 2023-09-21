from fastapi import FastAPI


def configure_routes(app: FastAPI):
    @app.get("/lands")
    def list_land():
        pass

    @app.get("/land")
    def get_land():
        pass

