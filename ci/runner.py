import argparse
import os
import time
import sys
from subprocess import call
from pathlib import Path
from subprocess import check_output, call

class Branch:
    def __init__(self, name, hash, is_behind, repo):
        self.name = name
        self.hash = hash
        self.is_behind = is_behind
        self.repo = repo

    def checkout(self):
        self.repo._run(["git", "stash"])
        self.repo._run(["git", "checkout", self.name])
        self.repo._run(["git", "pull"])
        self.is_behind = False

    def __enter__(self):
        self.exit_branch = (
            check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
        )
        self.checkout()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.repo._run(["git", "checkout", self.exit_branch])
        return True

class Git:
    def _fetch(self, args):
        print("FETCH:", " ".join(args))
        return check_output(args).decode()

    def _run(self, args):
        print("RUN:", " ".join(args))
        call(args)

    @property
    def branches(self):
        self._run(["git", "fetch", "-p"])
        refs = [
            x.split() for x in self._fetch(["git", "for-each-ref"]).split("\n")[:-1]
        ]
        remote = {}
        local = {}
        for hash, _, url in refs:
            name = url.split("/")[-1]
            if "refs/remotes/origin" in url:
                remote[name] = hash
            elif "refs/heads/" in url:
                local[name] = hash
        del remote["HEAD"]
        branches = []
        for name, hash in remote.items():
            behind = local.get(name, None) != hash
            branches.append(Branch(name, hash, behind, self))
        return branches

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        default="ci/pipeline.py",
        help="instruction set for pyci, default='ci/pipeline.py'",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=60 * 60,  # every hour
        help="time to wait between querying the repo hosting service for changes. default = 3600 (seconds)",
    )
    args = parser.parse_args()
    repo = Git()
    while True:
        for b in repo.branches:
            if b.is_behind:
                with b:
                    pipeline = Path(args.file)
                    if pipeline.exists():
                        call([sys.executable, str(pipeline)])
                    else:
                        print("No pipeline to run")
        time.sleep(args.timeout)
