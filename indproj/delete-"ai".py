prefixes = ["# ", "## ", "### ", "- "]
with open("theses.md", "r") as file:
    with open("theses.no-ai.md", "w") as outfile:
        for line in file:
            for prefix in prefixes:
                line = line.removeprefix(prefix)
            outfile.write(line)
