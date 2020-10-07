main_window = """
    QWidget {
        background-color: #eeeeee;
    }"""

main_section = """
    QFrame {
        border: 1px solid gray
    }"""

title_label = """
    QLabel {
        font-weight: 450;
        font-size: 15px;
        color: #141414;
        padding: 10px;
        background-color: #dddddd;
        border: none;
        border-bottom: 1px solid #aaaaaa;
    }
    """

url_label = """
    QFrame {
        border: none;
    }
    """

url_type = lambda x: f"""
    QLabel {{
        color: {x[0]};
        font-size: 1em;
        font-weight: 525;
        background-color: {x[1]};
        border-left: 4px solid {x[0]};
        border-bottom: 1px solid #cccccc;
    }}"""

url_text = """
    QLabel {
        color: #444444;
        font-weight: 450;
        font-size: 14px;
        background-color: rgb(250, 250, 250);
        border-bottom: 1px solid #cccccc;
        padding: 5px;
    }
    QLabel::hover {
        background-color :#ffffff;
    }"""
