from app.claude_probe_marker import claude_probe_marker

def test_claude_probe_marker():
    assert claude_probe_marker() == 'claude-probe-ok'
