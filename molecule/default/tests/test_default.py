"""Role testing files using testinfra"""


def test_data_directory(host):
    """Check data directory"""
    d = host.file("/var/lib/home-assistant")
    assert d.is_directory
    assert d.user == "home-assistant"
    assert d.group == "root"
    assert d.mode == 0o775


def test_backup_directory(host):
    """Check backup directory"""
    b = host.file("/var/backups/home-assistant")
    assert b.is_directory
    assert b.user == "home-assistant"
    assert b.group == "root"
    assert b.mode == 0o775


def test_home_assistant_config(host):
    """Check Home Assistant config file"""
    f = host.file("/var/lib/home-assistant/configuration.yaml")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = "default_config: {}"
    assert config in f.content_string


def test_home_assistant_secrets(host):
    """Check Home Assistant secrets file"""
    f = host.file("/var/lib/home-assistant/secrets.yaml")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    config = "password: Secr3t"
    assert config in f.content_string


def test_home_assistant_service(host):
    """Check Home Assistant service"""
    s = host.service("home-assistant")
    assert s.is_running
    assert s.is_enabled


def test_home_assistant_docker_container(host):
    """Check Home Assistant docker container"""
    d = host.docker("home-assistant").inspect()
    assert d["HostConfig"]["Memory"] == 1073741824
    assert d["Config"]["Image"] == (
        "ghcr.io/home-assistant/home-assistant"
        ":latest"
    )
    assert d["Config"]["Labels"]["maintainer"] == "me@example.com"
    assert "PACKAGES=iputils" in d["Config"]["Env"]
    assert "internal" in d["NetworkSettings"]["Networks"]
    assert \
        "home-assistant" in \
        d["NetworkSettings"]["Networks"]["internal"]["Aliases"]


def test_backup(host):
    """Check if the backup runs successfully"""
    cmd = host.run("/usr/local/bin/backup-home-assistant.sh")
    assert cmd.succeeded


def test_backup_cron_job(host):
    """Check backup cron job"""
    f = host.file("/var/spool/cron/crontabs/root")
    assert "/usr/local/bin/backup-home-assistant.sh" in f.content_string


def test_restore(host):
    """Check if the restore runs successfully"""
    cmd = host.run("/usr/local/bin/restore-home-assistant.sh")
    assert cmd.succeeded
