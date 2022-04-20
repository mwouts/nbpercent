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

# %% 56bffc67-14e7-4f0f-b28e-59e66dbb9fd7
import ipywidgets as widgets
from IPython.display import display

widgets.IntSlider()

# Out: {"data": {"application/vnd.jupyter.widget-view+json": "56bffc67-14e7-4f0f-b28e-59e66dbb9fd7_0.json", "text/plain": "56bffc67-14e7-4f0f-b28e-59e66dbb9fd7_0.txt"}, "output_type": "display_data"}

# %% 04cf0140-692b-4c9c-a490-6c092812bbee
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))

# Out: {"data": {"application/vnd.jupyter.widget-view+json": "04cf0140-692b-4c9c-a490-6c092812bbee_0.json", "text/plain": "04cf0140-692b-4c9c-a490-6c092812bbee_0.txt"}, "output_type": "display_data"}
# Out: {"data": {"application/vnd.jupyter.widget-view+json": "04cf0140-692b-4c9c-a490-6c092812bbee_1.json", "text/plain": "04cf0140-692b-4c9c-a490-6c092812bbee_1.txt"}, "output_type": "display_data"}
