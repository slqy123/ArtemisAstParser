import click
import os


@click.command()
@click.argument('src', type=str)
@click.option('-o', '--output', type=str, default='./result.json', help='output path')
@click.option('-e', '--encoding', type=str, default='utf-8', help='encoding of your input file')
def parse(src: str, output: str, encoding: str):
    """
    Parse .ast files to json files

    src could be either file or directory, if src is a directory then output should also be a directory
    """

    if not os.path.exists(src):
        click.echo("invalid source file")
        return

    if os.path.isdir(src):
        if not os.path.exists(output):
            os.mkdir(output)
        if not os.path.isdir(output):
            click.echo('Output path must be a directory if your input is a directory')
            return
        srcs = [os.path.join(src, n) for n in os.listdir(src)]
    else:
        srcs = [src]

    from ast import Ast
    ast = Ast()
    for src in srcs:
        dst = output
        if os.path.isdir(output):
            dst = os.path.join(output, os.path.basename(src).rsplit('.', 1)[0] + '.json')
        print(src)
        with open(src, encoding=encoding) as f:
            ast.parse(f.read(), encoding=encoding, save_path=dst)


if __name__ == '__main__':
    parse()
