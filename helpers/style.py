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

url_bar = """
    QFrame#urlBar {
        margin: auto;
        margin-bottom: 0px;
        margin-top: 30px;    
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

type_dropdown = """
    QComboBox {
        margin: 0px;
        color: #141414;
        padding-left: 7px;
        font-weight: 450;
        background-color: white
    }"""

url_entry = """
    QTextEdit {
        margin: 0;
        color: #141414;
        border: 1px solid #aaaaaa;
        border-left: 0px;
        background-color: white;
        vertical-align: center;
        font-size: 14px
    }"""

send_button = """
    QPushButton {
        color: #141414;
        margin: 0;
        border: 1px solid #aaaaaa;
        border-left: 0px;
        font-weight: 450;
        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 white);
    }"""