GIT ?= git
NPX ?= npx

GIT_REMOTE := $(shell $(GIT) remote get-url origin)
GIT_USER_ID := govau
GIT_REPO_ID := $(shell basename $(GIT_REMOTE) .git)

generate: swagger.yaml
	$(NPX) openapi-generator generate \
		-i $< \
		-g python \
		--git-user-id $(GIT_USER_ID) \
		--git-repo-id $(GIT_REPO_ID) \
		--additional-properties=packageName=saplivelink365

.PHONY:
	generate
