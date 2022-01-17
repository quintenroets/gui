import cli
import subprocess


def ask(message, choices=None, options=None):
    options = {'text': f'<big>{message}</big>'} | (options or {})

    if choices is None:
        res = run('entry', options=options)
        res = res and res.strip()
    elif isinstance(choices, list):
        res = ask_choices(choices)
    elif isinstance(choices, dict):
        res = ask_choices(
            list(choices.keys())
        )
        res = res and choices[res]
    else:
        raise Exception('Choices parameter not valid')

    return res


def ask_choices(choices, options=None):
    separator = '###'
    options = {
        'separator': separator,
        'no-headers': None
    } | (options or {})
    items = ['--column=text', '--column=@font@'] + [v for c in choices for v in (c, 'Monospace 15')]
    res = run('list', args=items, options=options)
    res = res and res.split(separator)[0]
    return res


def run(subcommand, args=None, options=None):
    args = args or []
    options = {
        'geometry': '907x514+500+200',
        'title': '',
        'text-align': 'center',
        'icon-theme': 'Win11',
        'fontname': 'Noto Sans 40',
    } | (options or {})
    result = cli.get('yad', f'--{subcommand}', *args, options, check=False)
    return result


def ask_yn(question):
    res = subprocess.run(('kdialog', '--yesno', question), capture_output=True)
    return res.returncode == 0
