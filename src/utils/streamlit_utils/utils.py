
import streamlit as st
import base64

def write_emptyline(num,pos=None):
    if pos:
        for i in range(num):
            pos.write(' ')
    else:
        for i in range(num):
            st.write(' ')

def version_info(version):

    st.markdown(

            """
            <style>
            .bottom-right {
            position: fixed;
            bottom: 0;
            right: 0;
            margin-bottom: 10px;
            margin-right: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True,

        )
    st.markdown(

        f"""
        <p class="bottom-right">Version : {version}</p>
        """,

        unsafe_allow_html=True,

    )

def render_logo(svg_path:str,height_logo:int, width_logo :int,pos_top :int, pos_left:int):
    """_summary_

    Args:
        svg_path (str): svg file path
        height_logo (int): height of the logo in pixels
        width_logo (int): width of the logo in pixels
        pos_top (int): position coordinate on top ( can be negetive)
        pos_left (int):  position coordinate on lect ( can be negetive)
    """
    with open(svg_path, "r") as f:
        svg_logo = f.read()

    b64 = base64.b64encode(svg_logo.encode('utf-8')).decode("utf-8")
    html = rf'<img src="data:image/svg+xml;base64,%s" style="position: absolute; top: {pos_top}px; left: {pos_left}px; width: {width_logo}px; height: {height_logo}px;"/>' % b64
    st.write(html, unsafe_allow_html=True)

def render_text(text:str, font_size:int, pos_top:int, pos_left:int):
    """_summary_

    Args:
        text (str): The text to display
        font_size (int): font size in pixels
        pos_top (int): position coordinate on top ( can be negetive)
        pos_left (int):  position coordinate on lect ( can be negetive)
    """

    html = rf'<p style="position: absolute; top: {pos_top}px; left: {pos_left}px; font-size: {font_size}px; font-weight: bold;">{text}</p>'

    st.write(html, unsafe_allow_html=True)


def tool_tip_icon(message):
    style = """
    <style>

    .tooltip {

        position: center;
        display: inline-block;
        cursor: pointer;
        width: 20px; /* Width of the circle */
        height: 20px; /* Height of the circle */
        border-radius: 50%; /* Make it circular */
        border: 2px solid black;
        background-color: white; /* Background color */
        text-align: center;
        line-height: 16px; /* Center the text vertically */
        font-size: 16px; /* Font size of the question mark */
        color: black;

    }


    .tooltip .tooltiptext {
        visibility: hidden;
        background-color: white;
        color: black;
        text-align: left;
        border-radius: 10px;
        padding: 20px;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Position the tooltip above the icon */
        left: 0%;
        margin-left: -100px; /* Center the tooltip */
        opacity: 0;
        transition: opacity 0.3s;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);

    }


    .tooltip:hover .tooltiptext {

        visibility: visible;

        opacity: 1;

    }

    </style>

    """
    html_code = f"""

    {style}
    <div class="tooltip">
    &#63; <!-- HTML entity for question mark -->
    <span class="tooltiptext">
    {message}
    </span>
    </div>

    """


    # Display the HTML in Streamlit

    st.markdown(html_code, unsafe_allow_html=True)