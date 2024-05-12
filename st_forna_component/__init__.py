import streamlit.components.v1 as components
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))
forna_component = components.declare_component(
    "forna_component",
    path=parent_dir,
)