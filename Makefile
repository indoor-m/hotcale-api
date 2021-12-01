.PHONY: api
api:
	docker-compose exec api /bin/bash

.PHONY: test
test:
	docker-compose exec api python ../tools/test_data_injection.py

.PHONY: test-interval
test-interval:
	docker-compose exec api python ../tools/test_interval_data_injection.py

.PHONY: export-schema
export-schema:
	docker-compose exec api strawberry export-schema main