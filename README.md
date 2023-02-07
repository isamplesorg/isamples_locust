# isamples_locust
Locust load tests for iSamples UI
## Run the tests
* `poetry shell`
* `locust --headless --users 1 --spawn-rate 1 -H https://hyde.cyverse.org` (change the host for comparisons -- e.g. https://iscaws.isample.xyz)
