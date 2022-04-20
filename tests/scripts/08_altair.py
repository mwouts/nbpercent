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

# %% 62776339-23c5-4612-a1ad-fc477f2c77ef
import altair as alt
from vega_datasets import data

source = data.cars()

alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

# Out[1]: {"data": {"text/html": "62776339-23c5-4612-a1ad-fc477f2c77ef_0.html", "text/plain": "62776339-23c5-4612-a1ad-fc477f2c77ef_0.txt"}}

# %% 72a2fd6a-c6f1-460a-a38e-66652a1ac132
