from locust import HttpUser, task


class ISamplesPostgresLocust(HttpUser):
    @task
    def test_get_thing(self):
        self.client.get("/isamples_central/thing/IGSN%3AODP02BWAO?full=false&format=full")

    @task
    def test_get_some_things(self):
        self.client.get("/isamples_central/thing/?offset=0&limit=10&status=200")

    @task
    def test_get_some_things_with_authority(self):
        self.client.get("/isamples_central/thing/?offset=0&limit=10&status=200&authority=SESAR")

    @task
    def test_get_metrics(self):
        self.client.get("/isamples_central/metrics")
