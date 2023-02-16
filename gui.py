import subprocess

import cli


def ask(message, choices=None, options=None):
    options = {"text": f"<big>{message}</big>"} | (options or {})

    if choices is None:
        res = run("entry", options=options)
        res = res and res.strip()
    elif any(isinstance(choices, valid) for valid in (list, set, tuple)):
        res = ask_choices(choices, options=options)
    elif isinstance(choices, dict):
        res = ask_choices(list(choices.keys()), options=options)
        res = res and choices[res]
    else:
        raise Exception("Choices parameter not valid")

    return res


def ask_choices(choices, options=None):
    display_mapping = {
        c[:100]: c for c in choices
    }  # limit length of displayed options to prevent errors
    separator = "###"
    options = {"separator": separator, "no-headers": None} | (options or {})
    items = ["--column=text", "--column=@font@"] + [
        v for c in display_mapping for v in (c, "Monospace 15")
    ]
    res = run("list", args=items, options=options)
    res = res and res.split(separator)[0]
    res = res and display_mapping[res]
    return res


def run(subcommand, args=None, options=None):
    args = args or []
    options = {
        "geometry": "907x514+500+200",
        "title": "",
        "text-align": "center",
        "icon-theme": "Win11",
        "fontname": "Noto Sans 40",
    } | (options or {})
    result = cli.get("yad", f"--{subcommand}", *args, options, check=False)
    return result


def ask_yn(question):
    res = subprocess.run(("kdialog", "--yesno", question), capture_output=True)
    return res.returncode == 0
