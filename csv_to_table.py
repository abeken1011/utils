import click

@click.command()
@click.option('--path', help='Input CSV path')

def to_table(path):
    output_lines = ""
    with open(path, encoding = "utf_8") as f:
        for i, line in enumerate(f):
            template = "| " + line.replace(",", " | ").replace("\n", "") + " |" + "\n"
            if i == 1:
                output_lines += "|--|--|--|--|--|\n" + template
            else:
                output_lines += template

    out_path = "out_" + path
    fileobj = open(out_path, "w", encoding = "utf_8")
    fileobj.write(output_lines)
    fileobj.close()

if __name__ == '__main__':
    to_table()