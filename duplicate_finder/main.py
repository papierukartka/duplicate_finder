import find

import click


@click.command()
@click.option(
    "--path", default="./", prompt="Directory", help="Directory to search through."
)
def analyze(path):
    """Analyze given directory and files within & return it's metadata."""
    click.echo("%s" % find.dir_structure(path))


if __name__ == "__main__":
    analyze()
