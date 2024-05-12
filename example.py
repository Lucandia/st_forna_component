import streamlit as st
from colour import Color
from st_forna_component import forna_component

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    if "colors" not in st.session_state:
        st.session_state.colors = dict()

    st.title("Forna Component")

    ### main input fields
    dot_bracket = st.text_input("Dot Bracket structure", "(((...)))")
    sequence = st.text_input("Sequence", "NNNAAAUUU")

    ### checkboxes for the options
    col1, col2, col3 = st.columns(3)
    with col1:
        zoomable = st.checkbox("Zoomable", value=False, help = """Enable zooming in and out the structure""")
    with col2:
        animation = st.checkbox("Interact", value=False, help = """Enable interaction with the structure""")
    with col3:
        editable = st.checkbox("Editable", value=False, help="""
    Enable editing of the structure: \n
    **Add Node**: *right click* on the canvas and select the nucleotide. \n
    **Delete Node /  Change Node / Insert Node**: *right click* on the node and select the option. \n
    **Remove Pairing**: *shift click* on a pairing. \n
    **Create Pairing**: *shift click and drag* to connect two nodes. \n
    **Connect Two Strands**: *shift click and drag* the ends of the two strands. \n
    """)

    ### second row of options
    with col1:
        st.write('\n')
        st.write('\n')
        node_label = st.checkbox("Node label", value=False)
    with col2:
        height = st.slider("Frame height", 10, 800, 300)
    with col3:
        label_interval = st.slider("Label interval", 0, len(sequence), 2)

    ### color scheme options
    with col1, col2, col3:
        with col1: 
            st.write('\n')
            st.write('\n')
            color_scheme = st.selectbox("Select a color scheme", ["sequence", "structure", "positions", "color range", "custom"])

    colors = ''
    ### color scheme based on the sequence
    if color_scheme == "color range":
        color_scheme = "custom"
        with col2: # start color
            first = st.color_picker("Select a color", "#ff0000")
        with col3: # end color
            last = st.color_picker("Select a color", "#00ff00")
        # create the colors range
        first = Color(first)
        last = Color(last)
        color_range = [first] + list(first.range_to(last, len(dot_bracket)))
        # save the colors in the session state and create the colors string
        for i, c in enumerate(color_range):
            st.session_state.colors[i] = c.hex
            colors += str(i) + ":" + c.hex + " "
    ### custom colors for each nucleotide
    elif color_scheme == "custom":
        with col2: # select nucleotide index
            index = st.number_input("Select nucleotide index", 0, len(dot_bracket), 0)
        with col3: # select color
            color = st.color_picker("Select a color", "#ffffff")
        # save the color in the session state
        st.session_state.colors[index] = color
        # create the colors string
        for i, c in st.session_state.colors.items():
            colors += str(i) + ":" + c + " "
    ### display the custom colors
    else:
        colors = None

    return_value = forna_component(
                                    structure = dot_bracket,
                                    sequence = sequence,
                                    height = height,
                                    animation = animation,
                                    zoomable = zoomable,
                                    label_interval = label_interval,
                                    node_label = node_label,
                                    editable = editable,
                                    color_scheme = color_scheme,
                                    colors = colors,
                                    )
    
    
    st.write("Received value:", return_value)
    if return_value:
        st.write("Received sequence", return_value[0])
        st.write("Received structure", return_value[1])


    # '(((((((((((((((((((..[[[[[[.)))))(((((((((....)))))))))(((((....)))))))))))))))))))((((((((((((((....)))))))))(((((....)))))(((((((((..]]]]]].))))))))))))))'
    # 'NNNNKNNNNKNNNNKNNNNAACUAACCANNNNKNNNNNNNNKUUCGKNNNNNNNNNNNNKUUCGKNNNNNNNNKNNNNKNNNNKNNNNNNNNKNNNNUUCGNNNNKNNNNKNNNNUUCGNNNNKNNNNNNNNKAAGGUUAGAKNNNNNNNNNNNNK'