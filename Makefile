
IMAGE := parquet-factory-image:1.0
.PHONY: build
build:
	@echo "Building image..."
	@docker build -t ${IMAGE} -f parquetfactory.Dockerfile .
	@echo "Building image and opening shell..."
	@docker run -it \
			--network="host" \
			-w /app \
			-v ${PWD}/parquet_factory:/app \
			-v ~/.aws/:/root/.aws \
			${IMAGE} /bin/bash