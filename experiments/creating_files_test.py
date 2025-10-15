contents = ["Family guy is a funny TV series",
            "GOT is the best TV series",
            "Breaking Bad is the second best TV series "]

filenames = ["doc.txt", "opinion.txt", "report.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", "w")
    file.writelines(content)