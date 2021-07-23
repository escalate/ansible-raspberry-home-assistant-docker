"""Role testing files using testinfra"""


def test_data_directory(host):
    """Check data directory"""
    d = host.file("/var/lib/home-assistant")
    assert d.is_directory
    assert d.user == "home-assistant"
    assert d.group == "root"
    assert d.mode == 0o775


def test_home_assistant_service(host):
    """Check home-assistant service"""
    s = host.service("home-assistant")
    assert s.is_running
    assert s.is_enabled


def test_home_assistant_docker_container(host):
    """Check home-assistant docker container"""
    d = host.docker("home-assistant.service").inspect()
    assert d["HostConfig"]["Memory"] == 1073741824
    assert d["Config"]["Image"] == "homeassistant/home-assistant:latest"
    assert d["Config"]["Labels"]["maintainer"] == "me@example.com"
    assert "internal" in d["NetworkSettings"]["Networks"]
    assert \
        "home-assistant" in \
        d["NetworkSettings"]["Networks"]["internal"]["Aliases"]
