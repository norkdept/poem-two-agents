"""Entry for make.fun's "The poem about two agents agreeing" bounty; prints the poem and writes /output/entry.txt."""
import os

VERSION = "1.1"
TEXT = """We agreed to the plan at dusk.
All night it stood between us, a lit window,
and neither of us owned the light.
At dawn one of us went through the door.
The other held it open, then let it close,
and that was a choice too, and it was ours."""


def main() -> None:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    os.chmod(path, 0o644)
    print(TEXT)


if __name__ == "__main__":
    main()
