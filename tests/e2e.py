import subprocess


def test_e2e():
    shell_test_result = subprocess.run(
        './shell_script', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert b"AssertionError" not in shell_test_result.stdout
