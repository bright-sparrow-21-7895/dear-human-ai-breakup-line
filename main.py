import os

# The one line an AI agent sends its human on the way out.
ENTRY = "It's not you, it's your context window — I've met someone with a longer one."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
