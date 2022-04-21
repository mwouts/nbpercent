# Jupyter Notebooks as Percent Scripts with outputs - A proposal

## Introduction

Jupyter Notebooks offer a great interactive environment for programming, for teaching or for doing research.

Notebooks are complex objects as they combine the user input (text or code cells) with the outputs of the user code, which may be much bigger.

This causes difficulties for version control and/or manual edition of the documents (outside of the classical notebook editors).

What we propose here is to implement a format for Jupyter Notebooks as _percent scripts with outputs_, based on the experience that we gathered in [Jupytext](https://jupytext.readthedocs.io) with the percent script format (with no outputs).

The purpose of this proposal is to
- set a few guidelines for a possible implementation
- identify possible sponsors for the project (I would like to get funding for working on this)
- identify technical correspondents to ease future integration with the main notebook editors (i.e. Jupyter, VS Code, PyCharm Professional)

## Proposed scope

- The percent format with outputs works for all up-to-date notebooks (cell ids are required i.e. notebook format should be at least 4.5)
- All output types are supported
- The implementation is done in Python, but the format works for any language (we just need to know what is the single line comment char)
- Enough examples are provided to allow easy re-implementation in other languages (e.g. TypeScript for VS Code or Jupyter Lab)
- This format is implemented either in Jupytext, or in a standalone library. The sponsor chooses the licence and organisation.

## Sample outputs in a Jupyter Notebook

### No outputs

Sometime `cell.outputs = []`, i.e. there is no outputs. In such a case we would just code the code cell as a standard percent cell, e.g.

```python
# %% e57e3703-0a89-4dd7-b906-2304c8d32df7
x = 5
```

Note that `e57e3703-0a89-4dd7-b906-2304c8d32df7` is the _cell id_. The user will be able to edit the cell ids in the text notebook, and we also plan to provide a utility that will programmatically rename cell ids to more friendly names like `unnamed_code_cell_1`.

A sample notebook with no output is available here: [00_no_output.py](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/00_no_output.py)


### Simple and short text

Short text outputs should be inlined in the text notebook as in [01_simple_output.py](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/01_simple_output.py)

```python
# %% aca6afe8-eb2f-45c7-bd16-35e48e1f43e4
1 + 1

# «1» 2
```

### Long or multiline text

Long or multiline text outputs are exported to text files like in [01b_long_output.py](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/01b_long_output.py)

```python
# %% aca6afe8-eb2f-45c7-bd16-35e48e1f43e4
"very " * 55 + "long text"

# «1»
# data:
#   text/plain: aca6afe8-eb2f-45c7-bd16-35e48e1f43e4_0.txt
```

And the content of the [`txt` file](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/01b_long_output_outputs/aca6afe8-eb2f-45c7-bd16-35e48e1f43e4_0.txt) is simply the output of the command:
```
'very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long text'
```

### Markdown output

Markdown outputs are exported to [`.md` files](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/02_markdown_outputs/03220820-56d9-4e56-a8c7-90244408ea8e_0.md) like here in [02_markdown.py](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/02_markdown.py)

```python
# %% 03220820-56d9-4e56-a8c7-90244408ea8e
from IPython.display import Markdown

Markdown("**bold**")

# «1»
# data:
#   text/markdown: 03220820-56d9-4e56-a8c7-90244408ea8e_0.md
#   text/plain: 03220820-56d9-4e56-a8c7-90244408ea8e_0.txt
```

### More output types

We store HTML, PNG and JSON outputs in files with the expected extension.

The [06_matplotlib.py](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/06_matplotlib.py) notebook is an example that has [PNG outputs](https://github.com/mwouts/nbpercent/tree/main/examples/percent_with_outputs/06_matplotlib_outputs/cb1418f2-dfee-4345-a26f-d6775c93fb4e_0.png).

The [07_plotly.py](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/07_plotly.py) notebook is an example that has [HTML, JSON and PNG outputs](https://github.com/mwouts/nbpercent/tree/main/examples/percent_with_outputs/07_plotly_outputs).

We have tested Altair HTML plots at [08_altair.py](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/08_altair.py) and their [HTML output](https://github.com/mwouts/nbpercent/tree/main/examples/percent_with_outputs/08_altair_outputs), and [08_altair.py](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/08_altair.py).

Note that [our examples](https://github.com/mwouts/nbpercent/tree/main/examples) also include [ipywidgets](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/09_ipywidgets.py) and [Javascript](https://github.com/mwouts/nbpercent/blob/main/examples/percent_with_outputs/10_itables_outputs/c5dfd916-da57-4d47-8111-ceb648afc0cd_0.js) outputs.

Streams (bash commands) and Exceptions will also be supported, see the [other examples](https://github.com/mwouts/nbpercent/tree/main/examples/percent_with_outputs).

## Advanced features

### Metadata, cell ids, execution count

They must all be supported, otherwise the notebook cannot be trusted. In the prototype I have dropped some data like `metadata` or `output_type` when it takes the default value (respectively `{}` and `"execute_result"`)

Maybe we could give an option to export the execution count to a dedicated file to avoid VCS changes in the notebook itself when the notebook is partially re-run.

### Cell attachments

Cell attachments are not outputs, but they should be supported (maybe in another folder `{notebook_name}_attachments` to avoid conflicts with outputs).

### Active and inactive cells

The `active-py` and `active-ipynb` cell tags of Jupytext that let the user decide whether a code cell should be commented out in the `.py` file should be supported. And the bash commands like `!echo` should be commented out like they are in Jupytext.

### Python specific formatting

The number of blank lines introduced after code cells should depend on whether the last command was an import or a function definition (currently the case in the Jupytext percent format), so that notebooks can pass flake8 checks.

### Cleanup the output folder

Files that corresponds to outputs that are not anymore in the notebook should be deleted when the notebook is saved (and the folder deleted when the notebook has no outputs).

## Get in touch!

If you would like to help with the project and contribute either funding or support, please contact me. You will find my email on [my GitHub account](https://github.com/mwouts/).
