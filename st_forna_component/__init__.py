import streamlit.components.v1 as components
import os

parent_dir = os.path.dirname(os.path.abspath(__file__))
_component_func = components.declare_component(
    "st_forna_component",
    path=parent_dir,
)

def forna_component(structure, sequence: str='', animation: bool=False, zoomable: bool=True, label_interval: int=10, node_label: bool=False, editable: bool=False, color_scheme: str='sequence', colors: list=None, height: int=500, key: str=None):
    """
    Generate a Forna component.

    Args:
        structure (str): The structure of the component.
        sequence (str, optional): The sequence of the component. Defaults to an empty string.
        animation (bool, optional): Whether to enable animation. Defaults to False.
        zoomable (bool, optional): Whether the component is zoomable. Defaults to True.
        label_interval (int, optional): The interval for displaying labels. Defaults to 10.
        node_label (bool, optional): Whether to display node labels. Defaults to False.
        editable (bool, optional): Whether the component is editable. Defaults to False.
        color_scheme (str, optional): The color scheme to use. Defaults to 'sequence'.
        colors (list, optional): The list of colors to use. Defaults to None.
        height (int, optional): The height of the component. Defaults to 500.
        key (str, optional): The key for the component. Defaults to None.

    Returns:
        tuple: A tuple containing the structure and sequence of the component.
    """
    recieved_values = _component_func(structure=structure, sequence=sequence, animation=animation, zoomable=zoomable, label_interval=label_interval, node_label=node_label, editable=editable, color_scheme=color_scheme, colors=colors, height=height, key=key)
    if editable and recieved_values:
        return recieved_values[1], recieved_values[0]
    else:
        return structure, sequence