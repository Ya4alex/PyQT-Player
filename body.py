from player import Ui_MainWindow

import sys
import csv
import hashlib
import os
import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QAbstractItemView, QFileDialog
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

DIR = 'playlists/'
if not os.path.exists(DIR):
    os.mkdir('playlists')

if not os.path.exists('volume.txt'):
    with open('volume.txt', 'w') as file:
        file.write('100')

if not os.path.exists('list_of_playlists.csv'):
    with open('list_of_playlists.csv', 'w', newline='') as file:
        writer = csv.writer(
            file, delimiter=';', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['name', 'path'])


def file_hash_sum(path):
    fhash = hashlib.md5()
    with open(path, "rb") as FileObject:
        while True:
            data = FileObject.read(8192)
            if not data:
                break

            fhash.update(data)
    return fhash.hexdigets()


def hhmmss(ms):
    return str(datetime.timedelta(seconds=ms // 1000))


class Track(QListWidgetItem):
    def __init__(self, player, path, name=''):
        if not name:
            name = path.split('/')[-1]
            name = name[:name.rfind('.')]
        super().__init__(name)
        self.name = name
        self.player = player
        self.path = path

        # self.hsum = file_hash_sum(path)

    def set_name(self):
        self.name = self.text()

    def start_play(self):
        try:
            self.player.setMedia(QMediaContent(QUrl(self.path)))
        except Exception:
            print('с файдлом не все в порядке')


class Play_list(QListWidgetItem):
    def __init__(self, player, path, name=False):
        if not name:
            name = path
        super().__init__(name)
        self.name = name
        self.path = path
        self.tracks = []
        self.player = player

    def create(self):
        with open(DIR + self.path + '.csv', 'w', newline='') as file:
            writer = csv.writer(
                file, delimiter=';', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['name', 'path'])

    def download(self):
        with open(DIR + self.path + '.csv', encoding="utf8") as file:
            tracks_path = csv.DictReader(file, delimiter=';', quotechar='"')
            self.tracks = [Track(self.player, i['path'], i['name']) for i in tracks_path]

    def save(self):
        with open(DIR + self.path + '.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['name', 'path'])
            for track in self.tracks:
                writer.writerow([track.name, track.path])
        self.tracks.clear()

    def set_name(self):
        self.name = self.text()

    def __add__(self, track):
        self.tracks.append(track)

    def __sub__(self, track):
        del self.tracks[self.tracks.index(track)]


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_q.hide()
        self.setWindowIcon(QIcon('pictures/icon.png'))
        self.setWindowTitle('Player')
        self.centralwidget.installEventFilter(self)
        self.player = QMediaPlayer()

        # variables
        self.player_list = []
        self.is_play = False
        self.ch_playlist = False
        self.play_now = False
        self.cords = [False, False]  # list, index
        self.edit_items = []
        self.edit_lists = []

        # pictures
        self.paus.setText('')
        self.picture_play = QIcon('pictures/play1.png')
        self.picture_paus = QIcon('pictures/paus.png')
        self.paus.setIcon(self.picture_play)
        self.paus.setIconSize(QSize(49, 29))

        # init methods
        self.initui()
        self.download_playlists()

    def initui(self):
        # new, add and delete
        self.tracks.installEventFilter(self)
        self.playlists.installEventFilter(self)
        self.installEventFilter(self)

        self.new_playlist.clicked.connect(self.m_new_playlist)
        self.add_track.clicked.connect(self.m_add_track)
        self.delete_track.clicked.connect(self.delit)
        self.delete_playlist.clicked.connect(lambda: self.delit(True))
        self.save_changes.clicked.connect(self.close_editor)

        # navigation
        self.next.clicked.connect(self.play_next)
        self.befour.clicked.connect(lambda: self.play_next(True))
        self.paus.clicked.connect(self.start_and_stop)
        self.question.clicked.connect(lambda: self.label_q.show() if self.label_q.isHidden() else self.label_q.hide())

        # chose
        self.tracks.doubleClicked.connect(self.play_chosen_track)
        self.playlists.doubleClicked.connect(self.choose_playlist)

        # sound:
        self.timeline.valueChanged.connect(self.player.setPosition)
        self.timeline.setRange(0, 0)
        self.player.positionChanged.connect(self.update_position)
        self.player.durationChanged.connect(self.update_duration)

        self.volume.setRange(0, 100)
        self.volume.valueChanged.connect(self.player.setVolume)
        with open('volume.txt', 'r') as f:
            vol = int(f.read())
            self.volume.setValue(vol)
            self.player.setVolume(vol)
            self.volume_label.setText(str(vol))
        self.volume.valueChanged.connect(lambda: self.volume_label.setText(f'{self.volume.value()}'))

        # set Drag and Drop Mode
        self.tracks.setDragDropMode(QAbstractItemView.InternalMove)
        self.tracks.setDefaultDropAction(Qt.MoveAction)

        self.playlists.setDragDropMode(QAbstractItemView.InternalMove)
        self.playlists.setDefaultDropAction(Qt.MoveAction)

    # time line and time -------------------------------
    def update_position(self, position):
        if self.player.duration() == position != 0:
            self.play_next()

        self.timeline_label.setText(hhmmss(self.player.duration() - position))
        self.timeline.blockSignals(True)
        self.timeline.setValue(position)
        self.timeline.blockSignals(False)

    def update_duration(self, duration):
        self.timeline.setMaximum(duration)

    # navigation ---------------------------------------
    def play_next(self, reverse=False):
        if not self.play_now:
            return
        if reverse:
            nxt = -1
        else:
            nxt = 1
        if self.play_now in self.ch_playlist.tracks:
            self.synchronize()
            index = self.ch_playlist.tracks.index(self.play_now) + nxt
            if 0 <= index < self.tracks.count():
                self.set_play_now(self.tracks.item(index))
                self.cords[1] = index
                self.play_now.start_play()
                self.start_and_stop(True)
            else:
                pass

        else:
            index = self.player_list.index(self.play_now) + nxt
            if 0 <= index < len(self.player_list):
                self.set_play_now(self.player_list[index])
                self.cords[1] = index
                self.play_now.start_play()
                self.start_and_stop(True)
            else:
                pass

    def start_and_stop(self, new=False, stop=False):
        if (not self.is_play or new) and not stop:
            self.player.play()
            self.is_play = True

            self.paus.setIcon(self.picture_paus)
        else:
            self.is_play = False
            self.player.pause()

            self.paus.setIcon(self.picture_play)
        if stop:
            self.player.setMedia(QMediaContent())

    # chose --------------------------------------------
    def play_chosen_track(self):
        if self.cords[0]:
            self.cords[0].setBackground(QColor(222, 255, 243))
        self.cords = [self.ch_playlist, self.tracks.currentIndex().row()]
        self.set_play_now(self.tracks.currentItem())
        self.player_list.clear()
        self.start_and_stop(True)

    # выбор плейлиста, сохранение текущего, выгрузка выбранного
    def choose_playlist(self, new=True):
        if self.play_now and self.ch_playlist:
            if self.play_now in self.ch_playlist.tracks:
                self.synchronize()
                self.player_list = self.ch_playlist.tracks.copy()
                self.cords[1] = self.ch_playlist.tracks.index(self.play_now)

        if self.playlists.count() > 1 and new:
            self.synchronize()
            self.ch_playlist.save()
        self.tracks.clear()

        self.playlists.currentItem().download()
        self.set_ch_playlist(self.playlists.currentItem())
        self.show_playlist()

    # operations on playlists and traks ----------------
    def delit(self, list=False, all=False):
        if all:
            playlist = self.playlists.currentItem()
            if playlist == self.ch_playlist:
                self.synchronize()
                for i in range(self.tracks.count()):
                    item = self.tracks.item(i)
                    if item == self.play_now:
                        self.unset_play_now()
                    item = self.tracks.takeItem(self.tracks.indexFromItem(item).row())
                    self.tracks.removeItemWidget(item)
                    del item
        elif list:
            if self.playlists.currentItem():
                self.delit(False, True)
                item = self.playlists.currentItem()
                row = self.playlists.indexFromItem(item).row()
                if 0 < row < self.playlists.count():
                    self.playlists.setCurrentRow(row)
                    self.choose_playlist(False)
                os.remove(DIR + item.path + '.csv')
                item = self.playlists.takeItem(row)
                self.playlists.removeItemWidget(item)
                del item
        else:
            self.synchronize()
            item = self.tracks.currentItem()
            if not item:
                return
            if item == self.play_now:
                self.unset_play_now()
            self.ch_playlist.tracks.remove(item)

            row = self.tracks.indexFromItem(item).row()
            item = self.tracks.takeItem(row)
            self.tracks.removeItemWidget(item)
            del item

    def download_playlists(self):
        with open('list_of_playlists.csv', encoding="utf8") as file:
            tracks_path = csv.DictReader(file, delimiter=';', quotechar='"')
            for i in tracks_path:
                try:
                    playlist = Play_list(self.player, i['path'], i['name'])
                    playlist.download()
                    self.playlists.addItem(playlist)
                except FileNotFoundError:
                    print('нет csv файла:(' + i['path'] + i['name'] + ')')

        if self.playlists.count() > 0:
            self.ch_playlist = self.playlists.item(0)
            self.playlists.setCurrentItem(self.playlists.item(0))
            self.choose_playlist()

    def synchronize(self):
        for i in range(self.tracks.count()):
            self.ch_playlist.tracks[i] = self.tracks.item(i)

    def show_playlist(self):
        if self.cords[0] == self.ch_playlist:
            self.set_play_now(self.ch_playlist.tracks[self.cords[1]], True)
        for item in self.ch_playlist.tracks:
            self.tracks.addItem(item)

    def set_ch_playlist(self, list1):
        self.ch_playlist = list1

    def unset_play_now(self):
        if self.tracks.count() > 1:
            print(self.cords[1], self.tracks.count() - 1)
            if self.cords[1] == self.tracks.count() - 1:
                self.play_next(True)
            else:
                self.play_next()
                self.cords[1] -= 1
        else:
            self.cords[0].setBackground(QColor(222, 255, 243))
            self.cords = [False, False]
            self.play_now = False
            self.is_play = False
            self.start_and_stop(True, True)

    def set_play_now(self, item, not_new=False):
        if not not_new:
            item.start_play()

        if self.play_now:
            try:
                self.play_now.setBackground(QColor(222, 255, 243))
            except RuntimeError:
                pass

        self.play_now = item

        self.Track_name.setText(' ' + self.play_now.name)

        self.cords[0].setBackground(QColor(255, 197, 201))

        try:
            self.play_now.setBackground(QColor(255, 197, 201))
        except RuntimeError:
            pass

    # new, add, delete ---------------------------------
    def m_add_track(self, path=False):
        list = self.playlists.currentItem()
        if not path:
            path = QFileDialog.getOpenFileName(
                self, "Open file", "",
                "mp3 Audio (*.mp3)")[0]
            if not path:
                return

        track = Track(self.player, path)
        list + track

        if list == self.ch_playlist:
            self.tracks.addItem(track)

    def m_new_playlist(self):
        num = 0
        while num in [int(path[:-4]) for path in os.listdir(DIR)]:
            num += 1

        item = Play_list(self.player, str(num))
        item.create()
        self.playlists.addItem(item)
        self.playlists.setCurrentItem(item)
        self.choose_playlist()

    # key press ----------------------------------------

    def close_editor(self):
        for item in self.edit_items:
            self.tracks.closePersistentEditor(item)
            item.set_name()
        self.edit_items.clear()

        for item in self.edit_lists:
            self.playlists.closePersistentEditor(item)

            item.set_name()
        self.edit_items.clear()

    def eventFilter(self, obj, event):
        if obj is self.playlists:
            if event.type() == QEvent.ContextMenu:
                item = self.playlists.currentItem()
                self.close_editor()
                if item:
                    self.playlists.openPersistentEditor(item)
                    self.edit_lists.append(item)

        elif obj is self.tracks:
            if event.type() == QEvent.ContextMenu:
                item = self.tracks.currentItem()
                self.close_editor()
                if item:
                    self.tracks.openPersistentEditor(item)
                    self.edit_items.append(item)

        return super().eventFilter(obj, event)

    # exit_saave event
    def exit_and_save(self):
        if not self.playlists.count():
            return
        print(self.playlists.count())
        self.synchronize()
        self.ch_playlist.save()

        with open('volume.txt', 'w') as file:
            file.write(str(self.volume.value()))

        with open('list_of_playlists.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['name', 'path'])
            for i in range(self.playlists.count()):
                writer.writerow([self.playlists.item(i).name, self.playlists.item(i).path])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()

    sys.excepthook = except_hook

    app.exec()
    ex.exit_and_save()
    sys.exit()
