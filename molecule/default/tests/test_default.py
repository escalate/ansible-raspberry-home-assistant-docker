"""Role testing files using testinfra"""


def test_read_only_directories(host):
    """Check read-only directories"""
    f = host.file("/etc/home-assistant")
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_writeable_directories(host):
    """Check writeable directories"""
    d = host.file("/var/lib/home-assistant")
    assert d.is_directory
    assert d.user == "home-assistant"
    assert d.group == "home-assistant"
    assert d.mode == 0o700


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
