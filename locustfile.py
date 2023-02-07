from locust import HttpUser, task


class ISamplesLocust(HttpUser):
    @task
    def test_isamples(self):
        self.client.get("/isamples_central/thing/stream?rows=100&fl=id,source,"
                        "x:producedBy_samplingSite_location_longitude,y:producedBy_samplingSite_location_latitude,"
                        "z:producedBy_samplingSite_location_cesium_height,"
                        "$gdfunc&gdfunc=geodist%28producedBy_samplingSite_location_ll%2C-17.451466233002286%2C-149"
                        ".8169236266867%29&sort=$gdfunc%20asc")