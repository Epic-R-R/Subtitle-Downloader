#!/usr/bin/python
import pip
import sys


def install(package):
    pip.main(['install', package])


def installing():
    import os, json, time, subprocess
    from yaspin import yaspin
    os.system("clear")
    with open('package.json', 'r') as fp:
        versions = json.load(fp)
    with yaspin(text="Start Preparing For Installation", color="cyan") as sp:
        time.sleep(5)
        sp.write("> All done")
        # finalize
        sp.ok("✔")
    with yaspin(text="Starting Installing For SsubDownloader", color="cyan") as sp:
        subprocess.call(["sudo", "dpkg", "-i", f"deb/SsubDownloader_{versions['versions'][-1]}-1.deb"])
        sp.write("> Installation Completed ")
        sp.ok("✔")
        print("💥 For Run Program Use This Command: ssubdownloader")


if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print("Use Python >= 3.5")
    else:
        while True:
            try:
                from yaspin import yaspin

                installing()
                break
            except ImportError:
                install('yaspin')
                continue
