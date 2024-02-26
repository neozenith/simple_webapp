from invoke import task


@task
def css(C):
    """Build tailwind CSS"""
    c.run("tailwindcss -i input.css -o output.css --minify")