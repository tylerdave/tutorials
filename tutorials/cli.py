import click

from . import tutorials

def list_lesson_ids():
    return ["{0:03}".format(i) for i in range(10)]

@click.group()
@click.option('--status-file', type=click.Path())
@click.option('--verbose', '-v')
@click.pass_context
def tutorial(ctx, status_file, verbose):
    """
    Runs a tutorial.
    """
    ctx.obj = {'verbose': verbose}

@tutorial.command()
@click.argument('lesson_id', type=click.Choice(list_lesson_ids()))
@click.pass_context
def lesson(ctx, lesson_id):
    """
    Run tests to check given LESSON_ID.
    """
    pass

@tutorial.command(name='lesson-ids')
@click.pass_context
def lesson_ids(ctx):
    """
    Output a list of all LESSON_IDs.
    """
    pass

@tutorial.command()
@click.pass_context
def next(ctx):
    """
    Run the next lesson.
    """
    pass

@tutorial.command()
@click.option('--yes', is_flag=True, help="Assume Y to confirmation prompts.")
@click.pass_context
def reset(ctx, yes):
    """
    Reset the status for all lessons (start-over)
    """
    pass

@tutorial.command()
@click.argument('lesson_id', type=click.Choice(list_lesson_ids()))
@click.pass_context
def solve(ctx, lesson_id):
    """
    Copy solution for LESSON_ID into place.
    """
    pass

@tutorial.command()
@click.pass_context
def status(ctx):
    """
    Show the status of the tutorial lessons.
    """
    pass

@tutorial.command()
@click.pass_context
def list(ctx):
    """
    List lessons
    """
    # TODO: maybe change to lessons?


if __name__ == '__main__':
    tutorial()
