from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy


LAYOUT_MAPPER = {
    "vertical": QVBoxLayout,
    "horizontal": QHBoxLayout,
}


class Section(QWidget):

    def __init__(
            self, layout_type,
            v_stretch=1,
            h_stretch=1,
            v_policy=QSizePolicy.Expanding,
            h_policy=QSizePolicy.Expanding
    ):
        super(Section, self).__init__()
        self._layout = None
        self._set_size_policy(v_policy, h_policy, v_stretch, h_stretch)
        self._set_layout(LAYOUT_MAPPER[layout_type])

    def _set_layout(self, layout_object):
        self._layout = layout_object()
        self.setLayout(self._layout)

    def _set_size_policy(self, v_policy, h_policy, v_stretch, h_stretch):
        size_policy = QSizePolicy()
        size_policy.setHorizontalPolicy(h_policy)
        size_policy.setVerticalPolicy(v_policy)
        size_policy.setHorizontalStretch(h_stretch)
        size_policy.setVerticalStretch(v_stretch)
        self.setSizePolicy(size_policy)

    def add_widget(self, widget):
        self._layout.addWidget(widget)
