# kernelspec:
#   display_name: Python [conda env:nbpercent-dev] *
#   language: python
#   name: conda-env-nbpercent-dev-py
# language_info:
#   codemirror_mode:
#     name: ipython
#     version: 3
#   file_extension: .py
#   mimetype: text/x-python
#   name: python
#   nbconvert_exporter: python
#   pygments_lexer: ipython3
#   version: 3.10.4

# %% c5dfd916-da57-4d47-8111-ceb648afc0cd
from itables import init_notebook_mode

init_notebook_mode(all_interactive=True)

# Out: {"data": {"application/javascript": "c5dfd916-da57-4d47-8111-ceb648afc0cd_0.js", "text/plain": "c5dfd916-da57-4d47-8111-ceb648afc0cd_0.txt"}, "output_type": "display_data"}

# %% 00fd1611-7c5e-40df-81c1-0a59f3868302
from itables.sample_dfs import get_countries

df = get_countries()
df

# Out[2]: {"data": {"text/html": "00fd1611-7c5e-40df-81c1-0a59f3868302_0.html", "text/plain": "00fd1611-7c5e-40df-81c1-0a59f3868302_0.txt"}}

# %% 765eaac1-43ac-459e-b811-a6ef02b9bc87
