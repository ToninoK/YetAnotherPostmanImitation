from PyQt5 import QtCore

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QSizePolicy, QFrame


LAYOUT_MAPPER = {
    "vertical": QVBoxLayout,
    "horizontal": QHBoxLayout,
}


class Section(QFrame):

    def __init__(
            self, layout_type,
            v_stretch=1,
            h_stretch=1,
            v_policy=QSizePolicy.Expanding,
            h_policy=QSizePolicy.Expanding
    ):
        super(Section, self).__init__()
        self._layout = None
        self.setSizePolicy(self.build_size_policy(v_policy, h_policy, v_stretch, h_stretch))
        self._set_layout(LAYOUT_MAPPER[layout_type])

    def _set_layout(self, layout_object):
        self._layout = layout_object()
        self._layout.setAlignment(QtCore.Qt.AlignTop)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._layout)

    @staticmethod
    def build_size_policy(v_policy, h_policy, v_stretch, h_stretch):
        size_policy = QSizePolicy()
        size_policy.setHorizontalPolicy(h_policy)
        size_policy.setVerticalPolicy(v_policy)
        size_policy.setHorizontalStretch(h_stretch)
        size_policy.setVerticalStretch(v_stretch)
        return size_policy

    def add_widget(self, widget, v_policy=None, h_policy=None, v_stretch=None, h_stretch=None):
        if all([v_policy, h_policy, v_stretch, h_stretch]):
            widget.setSizePolicy(self.build_size_policy(v_policy, h_policy, v_stretch, h_stretch))
        self._layout.addWidget(widget)

    def set_spacing(self, spacing):
        self._layout.setSpacing(spacing)
