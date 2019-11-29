NPX ?= npx

generate: swagger.yaml
	$(NPX) openapi-generator generate \
		-i $< \
		-g python \
		--additional-properties=packageName=saplivelink365

.PHONY:
	generate
