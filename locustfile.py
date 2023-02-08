from locust import HttpUser, task


class ISamplesLocust(HttpUser):
    @task
    def test_map_view(self):
        # map view (with rows turned down)
        self.client.get("/isamples_central/thing/stream?rows=100&fl=id,source,"
                        "x:producedBy_samplingSite_location_longitude,y:producedBy_samplingSite_location_latitude,"
                        "z:producedBy_samplingSite_location_cesium_height,"
                        "$gdfunc&gdfunc=geodist%28producedBy_samplingSite_location_ll%2C-17.451466233002286%2C-149"
                        ".8169236266867%29&sort=$gdfunc%20asc")

    @task
    def test_table_view(self):
        # table view
        self.client.get("/isamples_central/thing/select?q=*:*&fl=searchText authorizedBy producedBy_resultTimeRange "
                        "hasContextCategory curation_accessContraints curation_description_text curation_label "
                        "curation_location curation_responsibility description_text id informalClassification "
                        "keywords label hasMaterialCategory producedBy_description_text "
                        "producedBy_hasFeatureOfInterest producedBy_label producedBy_responsibility "
                        "producedBy_resultTime producedBy_samplingSite_description_text producedBy_samplingSite_label "
                        "producedBy_samplingSite_location_elevationInMeters producedBy_samplingSite_location_latitude "
                        "producedBy_samplingSite_location_longitude producedBy_samplingSite_placeName registrant "
                        "samplingPurpose source sourceUpdatedTime producedBy_samplingSite_location_rpt "
                        "hasSpecimenCategory&fq=-relation_target:*&facet.field=authorizedBy&facet.field"
                        "=hasContextCategory&facet.field=hasMaterialCategory&facet.field=registrant&facet.field"
                        "=source&facet.field=hasSpecimenCategory&&f.hasContextCategory.facet.sort=count&f"
                        ".hasMaterialCategory.facet.sort=count&f.registrant.facet.sort=count&f.source.facet.sort"
                        "=index&f.hasSpecimenCategory.facet.sort=count&rows=20&facet.limit=-1&facet.sort=index&&start"
                        "=20&facet=on&wt=json")

    @task
    def test_table_view_with_search_text(self):
        # table view with search text
        self.client.get("/isamples_central/thing/select?q=*:*&fl=searchText%20authorizedBy"
                        "%20producedBy_resultTimeRange%20hasContextCategory%20curation_accessContraints"
                        "%20curation_description_text%20curation_label%20curation_location%20curation_responsibility"
                        "%20description_text%20id%20informalClassification%20keywords%20label%20hasMaterialCategory"
                        "%20producedBy_description_text%20producedBy_hasFeatureOfInterest%20producedBy_label"
                        "%20producedBy_responsibility%20producedBy_resultTime"
                        "%20producedBy_samplingSite_description_text%20producedBy_samplingSite_label"
                        "%20producedBy_samplingSite_location_elevationInMeters"
                        "%20producedBy_samplingSite_location_latitude%20producedBy_samplingSite_location_longitude"
                        "%20producedBy_samplingSite_placeName%20registrant%20samplingPurpose%20source"
                        "%20sourceUpdatedTime%20producedBy_samplingSite_location_rpt%20hasSpecimenCategory&fq"
                        "=searchText%3Atucson&fq=-relation_target%3A*&facet.field=authorizedBy&facet.field"
                        "=hasContextCategory&facet.field=hasMaterialCategory&facet.field=registrant&facet.field"
                        "=source&facet.field=hasSpecimenCategory&&f.hasContextCategory.facet.sort=count&f"
                        ".hasMaterialCategory.facet.sort=count&f.registrant.facet.sort=count&f.source.facet.sort"
                        "=index&f.hasSpecimenCategory.facet.sort=count&rows=20&facet.limit=-1&facet.sort=index&&start"
                        "=20&facet=on&wt=json")
