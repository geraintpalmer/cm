import json
import nbformat
import pathlib
import tempfile

from nbconvert import RSTExporter


def convert_rst(nb_path, tags_to_ignore=["hide"]):
    """
    Convert a notebook to rst
    """
    contents = nb_path.read_text()
    nb = json.loads(contents)

    error_cols = ['\x1b[0;31m', '\x1b[0m', '\x1b[0;32m', '\x1b[0;34m', '\x1b[0;36m']

    body = ''
    for cell in nb["cells"]:
        if cell['cell_type'] != 'code':
            for line in cell['source']:
                body += line.replace('$', '$$')
        if cell['cell_type'] == 'code':
            if "tags" not in cell["metadata"] or 'hide' not in cell["metadata"]["tags"]:
                body += "{% highlight python %}\n"
                for line in cell['source']:
                    if line[:4] == '    ':
                        body += '... '
                        body += line
                    elif line[:4] in ['}', ')', ']']:
                        body += '... '
                        body += line
                    elif line == '\n':
                        body += '\n'
                    else:
                        body += '>>> '
                        body += line
                body += '\n'
                if len(cell['outputs']) == 1:
                    if 'data' in cell['outputs'][0]:
                        for l in cell['outputs'][0]['data']['text/plain']:
                            body += l
                    elif 'text' in cell['outputs'][0]:
                        for l in cell['outputs'][0]['text']:
                            body += l
                    else:
                        for l in cell['outputs'][0]['traceback']:
                            for col in error_cols:
                                l = l.replace(col, '')
                            body += l
                            body += '\n'
                    body += '\n'
                body += "{% endhighlight %}"
        body += '\n\n'

    with open('chapters/' + nb_path.name.split('.')[0] + '.md', 'w') as f:
        f.write(body)

    cells = []
    for cell in nb["cells"]:
        if "tags" not in cell["metadata"] or all(
            tag not in cell["metadata"]["tags"] for tag in tags_to_ignore
        ):
            if cell["cell_type"] == "code":
                cell['outputs'] = []
            cells.append(cell)
    nb["cells"] = cells

    with (nb_path.parent / 'student' / nb_path.name).open(mode='w') as f:
        f.write(json.dumps(nb))




if __name__ == "__main__":
    nb_dir = pathlib.Path("chapters/nbs")
    worksheet_paths = sorted(nb_dir.glob("*ipynb"))
    for worksheet in worksheet_paths:
        convert_rst(worksheet)
