SHELL = /bin/bash
.SHELLFLAGS = -e -o pipefail -c
ANSIBLE_ARGS ?= $(ANSIBLE_OPTIONS)

ifdef ANSIBLE_TAGS
ANSIBLE_ARGS := $(ANSIBLE_ARGS) --tags='$(ANSIBLE_TAGS)'
endif

export PY_COLORS=1
export ANSIBLE_FORCE_COLOR=1

.PHONY: test
test:
	molecule test

.PHONY: debug
debug:
	molecule --debug test --destroy never

.PHONY: lint
lint:
	ec
	yamllint --strict --config-file .yamllint .
	ansible-lint --force-color .
	flake8 --show-source .

.PHONY: converge
converge:
	molecule converge -- $(ANSIBLE_ARGS)

.PHONY: verify
verify:
	molecule verify

.PHONY: destroy
destroy:
	molecule destroy
