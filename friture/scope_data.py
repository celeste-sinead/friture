#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2021 Timothée Lecomte

# This file is part of Friture.
#
# Friture is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as published by
# the Free Software Foundation.
#
# Friture is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Friture.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtQml import QQmlListProperty # type: ignore

from friture.axis import Axis
from friture.curve import Curve

class Scope_Data(QtCore.QObject):
    show_legend_changed = QtCore.pyqtSignal(bool)
    plot_items_changed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self._plot_items = []
        self._horizontal_axis = Axis(self)
        self._vertical_axis = Axis(self)
        self._show_legend = True

    @pyqtProperty(QQmlListProperty, notify=plot_items_changed) # type: ignore
    def plot_items(self):
        return QQmlListProperty(Curve, self, self._plot_items)

    def insert_plot_item(self, index, plot_item):
        self._plot_items.insert(index, plot_item)
        self.plot_items_changed.emit()

    def add_plot_item(self, plot_item):
        self._plot_items.append(plot_item)
        plot_item.setParent(self) # take ownership
        self.plot_items_changed.emit()

    def remove_plot_item(self, plot_item):
        self._plot_items.remove(plot_item)
        self.plot_items_changed.emit()

    @pyqtProperty(Axis, constant=True) # type: ignore
    def horizontal_axis(self):
        return self._horizontal_axis

    @pyqtProperty(Axis, constant=True) # type: ignore
    def vertical_axis(self):
        return self._vertical_axis

    @pyqtProperty(bool, notify=show_legend_changed) # type: ignore
    def show_legend(self):
        return self._show_legend

    @show_legend.setter # type: ignore
    def show_legend(self, show_legend):
        if self._show_legend != show_legend:
            self._show_legend = show_legend
            self.show_legend_changed.emit(show_legend)
