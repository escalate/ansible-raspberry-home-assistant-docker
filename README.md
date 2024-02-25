[![Test](https://github.com/escalate/ansible-raspberry-home-assistant-docker/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/escalate/ansible-raspberry-home-assistant-docker/actions/workflows/test.yml)

# Ansible Role: Raspberry - Home Assistant (Docker)

An Ansible role that manages [Home Assistant](https://www.home-assistant.io/) Docker container with systemd on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/escalate/ansible-raspberry-home-assistant-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

* Roles: [requirements.yml](https://github.com/escalate/ansible-raspberry-home-assistant-docker/blob/master/requirements.yml)
* Collections: [requirements.yml](https://github.com/escalate/ansible-raspberry-home-assistant-docker/blob/master/requirements.yml)

## Installation

```
$ ansible-galaxy role install escalate.home_assistant
```

## Example Playbook

```
- hosts: all
  roles:
    - role: escalate.home_assistant
      tags: homeassistant
```

## License

MIT
