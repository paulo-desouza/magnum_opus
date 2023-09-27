import subprocess

# prep magnum opus
# dnf.conf additions
subprocess.run(['echo', 'max_parallel_downloads=10', '>>', '/etc/dnf/dnf.conf'])
subprocess.run(['echo', 'fastestmirror=True', '>>', '/etc/dnf/dnf.conf'])

subprocess.run(['dnf', 'update'])



subprocess.run(['reboot')

