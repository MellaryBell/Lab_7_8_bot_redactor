import psycopg2
import sys

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                             QTableWidgetItem, QPushButton, QMessageBox)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._connect_to_db()
        self.setWindowTitle("Редактор")
        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)
        self._create_timetable_tab()
        self._create_teacher_tab()
        self._create_subject_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="telebot",
                                     user="postgres",
                                     password="12345",
                                     host="localhost",
                                     port="5432")
        self.cursor = self.conn.cursor()

    def _create_timetable_tab(self):
        self.timetable_tab = QWidget()
        self.tabs.addTab(self.timetable_tab, "Расписание")
        self.monday_gbox = QGroupBox("Понедельник")
        self.tuesday_gbox = QGroupBox("Вторник")
        self.wednesday_gbox = QGroupBox("Среда")
        self.thursday_gbox = QGroupBox("Четверг")
        self.friday_gbox = QGroupBox("Пятница")
        self.ttvbox = QVBoxLayout()
        self.tthbox1 = QHBoxLayout()
        self.tthbox2 = QHBoxLayout()
        self.ttvbox.addLayout(self.tthbox1)
        self.ttvbox.addLayout(self.tthbox2)
        self.tthbox1.addWidget(self.monday_gbox)
        self.tthbox1.addWidget(self.tuesday_gbox)
        self.tthbox1.addWidget(self.wednesday_gbox)
        self.tthbox1.addWidget(self.thursday_gbox)
        self.tthbox1.addWidget(self.friday_gbox)
        self._create_timetable_monday_table()
        self._create_timetable_tuesday_table()
        self._create_timetable_wednesday_table()
        self._create_timetable_thursday_table()
        self._create_timetable_friday_table()
        self.update_timetable_button = QPushButton("Update")
        self.tthbox2.addWidget(self.update_timetable_button)
        self.update_timetable_button.clicked.connect(self._update_timetable)
        self.timetable_tab.setLayout(self.ttvbox)

    def _create_teacher_tab(self):
        self.teacher_tab = QWidget()
        self.tabs.addTab(self.teacher_tab, "Учителя")
        self.teacher_gbox = QGroupBox("Учителя")
        self.tvbox = QVBoxLayout()
        self.thbox1 = QHBoxLayout()
        self.thbox2 = QHBoxLayout()
        self.tvbox.addLayout(self.thbox1)
        self.tvbox.addLayout(self.thbox2)
        self.thbox1.addWidget(self.teacher_gbox)
        self._create_teacher_table()
        self.update_teacher_button = QPushButton("Update")
        self.thbox2.addWidget(self.update_teacher_button)
        self.update_teacher_button.clicked.connect(self._update_teacher)
        self.teacher_tab.setLayout(self.tvbox)

    def _create_subject_tab(self):
        self.subject_tab = QWidget()
        self.tabs.addTab(self.subject_tab, "Предметы")
        self.subject_gbox = QGroupBox("Предметы")
        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        self.shbox1.addWidget(self.subject_gbox)
        self._create_subject_table()
        self.update_subject_button = QPushButton("Update")
        self.shbox2.addWidget(self.update_subject_button)
        self.update_subject_button.clicked.connect(self._update_subject)
        self.subject_tab.setLayout(self.svbox)

    def _create_timetable_monday_table(self):
        self.timetable_monday_table = QTableWidget()
        self.timetable_monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_monday_table.setColumnCount(9)
        self._update_timetable_monday_table()
        self.ttmvbox = QVBoxLayout()
        self.ttmvbox.addWidget(self.timetable_monday_table)
        self.monday_gbox.setLayout(self.ttmvbox)

    def _create_timetable_tuesday_table(self):
        self.timetable_tuesday_table = QTableWidget()
        self.timetable_tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_tuesday_table.setColumnCount(9)
        self._update_timetable_tuesday_table()
        self.tttuvbox = QVBoxLayout()
        self.tttuvbox.addWidget(self.timetable_tuesday_table)
        self.tuesday_gbox.setLayout(self.tttuvbox)

    def _create_timetable_wednesday_table(self):
        self.timetable_wednesday_table = QTableWidget()
        self.timetable_wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_wednesday_table.setColumnCount(9)
        self._update_timetable_wednesday_table()
        self.ttwvbox = QVBoxLayout()
        self.ttwvbox.addWidget(self.timetable_wednesday_table)
        self.wednesday_gbox.setLayout(self.ttwvbox)

    def _create_timetable_thursday_table(self):
        self.timetable_thursday_table = QTableWidget()
        self.timetable_thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_thursday_table.setColumnCount(9)
        self._update_timetable_thursday_table()
        self.ttthvbox = QVBoxLayout()
        self.ttthvbox.addWidget(self.timetable_thursday_table)
        self.thursday_gbox.setLayout(self.ttthvbox)

    def _create_timetable_friday_table(self):
        self.timetable_friday_table = QTableWidget()
        self.timetable_friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_friday_table.setColumnCount(9)
        self._update_timetable_friday_table()
        self.ttfvbox = QVBoxLayout()
        self.ttfvbox.addWidget(self.timetable_friday_table)
        self.friday_gbox.setLayout(self.ttfvbox)

    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.teacher_table.setColumnCount(5)
        self._update_teacher_table()
        self.tvbox1 = QVBoxLayout()
        self.tvbox1.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.tvbox1)

    def _create_subject_table(self):
        self.subject_table = QTableWidget()
        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.subject_table.setColumnCount(4)
        self._update_subject_table()
        self.svbox1 = QVBoxLayout()
        self.svbox1.addWidget(self.subject_table)
        self.subject_gbox.setLayout(self.svbox1)

    def _update_timetable_monday_table(self):
        self.timetable_monday_table.clear()
        self.timetable_monday_table.setHorizontalHeaderLabels(["id", "День", "Предмет", "Кабинет",
                                                               "Начало", "Учитель", "Неделя", "", ""])
        self.cursor.execute("SELECT * FROM public.timetable WHERE day='Понедельник' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_monday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_monday_table.setItem(i, 0,
                                                QTableWidgetItem(str(r[0])))
            self.timetable_monday_table.setItem(i, 1,
                                                QTableWidgetItem(str(r[1])))
            self.timetable_monday_table.setItem(i, 2,
                                                QTableWidgetItem(str(r[2])))
            self.timetable_monday_table.setItem(i, 3,
                                                QTableWidgetItem(str(r[3])))
            self.timetable_monday_table.setItem(i, 4,
                                                QTableWidgetItem(str(r[4])))
            self.timetable_monday_table.setItem(i, 5,
                                                QTableWidgetItem(str(r[5])))
            self.timetable_monday_table.setItem(i, 6,
                                                QTableWidgetItem(str(r[6])))
            self.timetable_monday_table.setCellWidget(i, 7, joinButton)
            self.timetable_monday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_monday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_monday_table(num))
        i += 1
        joinButton = QPushButton("Join")
        self.timetable_monday_table.setCellWidget(i, 7, joinButton)
        joinButton.clicked.connect(lambda state, num=i: self._add_record_to_timetable_monday_table(num))
        self.timetable_monday_table.resizeRowsToContents()

    def _update_timetable_tuesday_table(self):
        self.timetable_tuesday_table.clear()
        self.timetable_tuesday_table.setHorizontalHeaderLabels(["id", "День", "Предмет", "Кабинет",
                                                                "Начало", "Учитель", "Неделя", "", ""])
        self.cursor.execute("SELECT * FROM public.timetable WHERE day='Вторник1' OR day='Вторник2' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_tuesday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_tuesday_table.setItem(i, 0,
                                                 QTableWidgetItem(str(r[0])))
            self.timetable_tuesday_table.setItem(i, 1,
                                                 QTableWidgetItem(str(r[1])))
            self.timetable_tuesday_table.setItem(i, 2,
                                                 QTableWidgetItem(str(r[2])))
            self.timetable_tuesday_table.setItem(i, 3,
                                                 QTableWidgetItem(str(r[3])))
            self.timetable_tuesday_table.setItem(i, 4,
                                                 QTableWidgetItem(str(r[4])))
            self.timetable_tuesday_table.setItem(i, 5,
                                                 QTableWidgetItem(str(r[5])))
            self.timetable_tuesday_table.setItem(i, 6,
                                                 QTableWidgetItem(str(r[6])))
            self.timetable_tuesday_table.setCellWidget(i, 7, joinButton)
            self.timetable_tuesday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_tuesday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_tuesday_table(num))
        i += 1
        joinButton = QPushButton("Join")
        self.timetable_tuesday_table.setCellWidget(i, 7, joinButton)
        joinButton.clicked.connect(lambda state, num=i: self._add_record_to_timetable_tuesday_table(num))
        self.timetable_tuesday_table.resizeRowsToContents()

    def _update_timetable_wednesday_table(self):
        self.timetable_wednesday_table.clear()
        self.timetable_wednesday_table.setHorizontalHeaderLabels(["id", "День", "Предмет", "Кабинет",
                                                                  "Начало", "Учитель", "Неделя", "", ""])
        self.cursor.execute("SELECT * FROM public.timetable WHERE day='Среда1' OR day='Среда2' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_wednesday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_wednesday_table.setItem(i, 0,
                                                   QTableWidgetItem(str(r[0])))
            self.timetable_wednesday_table.setItem(i, 1,
                                                   QTableWidgetItem(str(r[1])))
            self.timetable_wednesday_table.setItem(i, 2,
                                                   QTableWidgetItem(str(r[2])))
            self.timetable_wednesday_table.setItem(i, 3,
                                                   QTableWidgetItem(str(r[3])))
            self.timetable_wednesday_table.setItem(i, 4,
                                                   QTableWidgetItem(str(r[4])))
            self.timetable_wednesday_table.setItem(i, 5,
                                                   QTableWidgetItem(str(r[5])))
            self.timetable_wednesday_table.setItem(i, 6,
                                                   QTableWidgetItem(str(r[6])))
            self.timetable_wednesday_table.setCellWidget(i, 7, joinButton)
            self.timetable_wednesday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_wednesday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_wednesday_table(num))
        i+=1
        joinButton = QPushButton("Join")
        self.timetable_wednesday_table.setCellWidget(self.timetable_wednesday_table.rowCount() + 1, 7, joinButton)
        joinButton.clicked.connect(lambda state,
                                          num=self.timetable_wednesday_table.rowCount() + 1: self._add_record_to_timetable_wednesday_table(
            num))
        self.timetable_wednesday_table.resizeRowsToContents()

    def _update_timetable_thursday_table(self):
        self.timetable_thursday_table.clear()
        self.timetable_thursday_table.setHorizontalHeaderLabels(["id", "День", "Предмет", "Кабинет",
                                                                 "Начало", "Учитель", "Неделя", "", ""])
        self.cursor.execute("SELECT * FROM public.timetable WHERE day='Четверг' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_thursday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_thursday_table.setItem(i, 0,
                                                  QTableWidgetItem(str(r[0])))
            self.timetable_thursday_table.setItem(i, 1,
                                                  QTableWidgetItem(str(r[1])))
            self.timetable_thursday_table.setItem(i, 2,
                                                  QTableWidgetItem(str(r[2])))
            self.timetable_thursday_table.setItem(i, 3,
                                                  QTableWidgetItem(str(r[3])))
            self.timetable_thursday_table.setItem(i, 4,
                                                  QTableWidgetItem(str(r[4])))
            self.timetable_thursday_table.setItem(i, 5,
                                                  QTableWidgetItem(str(r[5])))
            self.timetable_thursday_table.setItem(i, 6,
                                                  QTableWidgetItem(str(r[6])))
            self.timetable_thursday_table.setCellWidget(i, 7, joinButton)
            self.timetable_thursday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_thursday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_thursday_table(num))
        i += 1
        joinButton = QPushButton("Join")
        self.timetable_thursday_table.setCellWidget(self.timetable_thursday_table.rowCount() + 1, 7, joinButton)
        joinButton.clicked.connect(lambda state,
                                          num=self.timetable_thursday_table.rowCount() + 1: self._add_record_to_timetable_thursday_table(
            num))
        self.timetable_thursday_table.resizeRowsToContents()

    def _update_timetable_friday_table(self):
        self.timetable_friday_table.clear()
        self.timetable_friday_table.setHorizontalHeaderLabels(["id", "День", "Предмет", "Кабинет",
                                                               "Начало", "Учитель", "Неделя", "", ""])
        self.cursor.execute("SELECT * FROM public.timetable WHERE day='Пятница1' OR day='Пятница2' ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.timetable_friday_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.timetable_friday_table.setItem(i, 0,
                                                QTableWidgetItem(str(r[0])))
            self.timetable_friday_table.setItem(i, 1,
                                                QTableWidgetItem(str(r[1])))
            self.timetable_friday_table.setItem(i, 2,
                                                QTableWidgetItem(str(r[2])))
            self.timetable_friday_table.setItem(i, 3,
                                                QTableWidgetItem(str(r[3])))
            self.timetable_friday_table.setItem(i, 4,
                                                QTableWidgetItem(str(r[4])))
            self.timetable_friday_table.setItem(i, 5,
                                                QTableWidgetItem(str(r[5])))
            self.timetable_friday_table.setItem(i, 6,
                                                QTableWidgetItem(str(r[6])))
            self.timetable_friday_table.setCellWidget(i, 7, joinButton)
            self.timetable_friday_table.setCellWidget(i, 8, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_timetable_friday_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_timetable_friday_table(num))
        i += 1
        joinButton = QPushButton("Join")
        self.timetable_friday_table.setCellWidget(self.timetable_friday_table.rowCount() + 1, 7, joinButton)
        joinButton.clicked.connect(
            lambda state, num=self.timetable_thursday_table.rowCount() + 1: self._add_record_to_timetable_friday_table(
                num))
        self.timetable_friday_table.resizeRowsToContents()

    def _update_teacher_table(self):
        self.teacher_table.clear()
        self.teacher_table.setHorizontalHeaderLabels(["id", "Имя учителя", "Предмет", "", ""])
        self.cursor.execute("SELECT * FROM public.teacher ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.teacher_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.teacher_table.setItem(i, 0,
                                       QTableWidgetItem(str(r[0])))
            self.teacher_table.setItem(i, 1,
                                       QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem(i, 2,
                                       QTableWidgetItem(str(r[2])))
            self.teacher_table.setCellWidget(i, 3, joinButton)
            self.teacher_table.setCellWidget(i, 4, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_teacher_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_teacher_table(num))
        i += 1
        joinButton = QPushButton("Join")
        self.teacher_table.setCellWidget(i, 3, joinButton)
        joinButton.clicked.connect(lambda state, num=i: self._add_record_to_teacher_table(num))
        self.teacher_table.resizeRowsToContents()

    def _update_subject_table(self):
        self.subject_table.clear()
        self.subject_table.setHorizontalHeaderLabels(["Название", "id", "", ""])
        self.cursor.execute("SELECT * FROM public.subject ORDER BY id;")
        records = list(self.cursor.fetchall())
        self.subject_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Join")
            deleteButton = QPushButton("Delete")
            self.subject_table.setItem(i, 0,
                                       QTableWidgetItem(str(r[0])))
            self.subject_table.setItem(i, 1,
                                       QTableWidgetItem(str(r[1])))
            self.subject_table.setCellWidget(i, 2, joinButton)
            self.subject_table.setCellWidget(i, 3, deleteButton)
            joinButton.clicked.connect(lambda state, num=i: self._change_record_from_subject_table(num))
            deleteButton.clicked.connect(lambda state, num=i: self._delete_record_from_subject_table(num))
        i += 1
        joinButton = QPushButton("Join")
        self.subject_table.setCellWidget(i, 2, joinButton)
        joinButton.clicked.connect(lambda state, num=i: self._add_record_to_subject_table(num))
        self.subject_table.resizeRowsToContents()

    def _add_record_to_timetable_monday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_monday_table.columnCount() - 2):
            try:
                row.append(self.timetable_monday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("INSERT INTO public.timetable (id, day, subject, room, start,teacher_id, "
                            "weektype) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _add_record_to_timetable_tuesday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_tuesday_table.columnCount() - 2):
            try:
                row.append(self.timetable_tuesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("INSERT INTO public.timetable (id, day, subject, room, start,teacher_id, "
                            "weektype) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _add_record_to_timetable_wednesday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_wednesday_table.columnCount() - 2):
            try:
                row.append(self.timetable_wednesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("INSERT INTO public.timetable (id, day, subject, room, start,teacher_id, "
                            "weektype) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _add_record_to_timetable_thursday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_thursday_table.columnCount() - 2):
            try:
                row.append(self.timetable_thursday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("INSERT INTO public.timetable (id, day, subject, room, start,teacher_id, "
                            "weektype) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _add_record_to_timetable_friday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_friday_table.columnCount() - 2):
            try:
                row.append(self.timetable_friday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("INSERT INTO public.timetable (id, day, subject, room, start,teacher_id, "
                            "weektype) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _add_record_to_teacher_table(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount() - 2):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("INSERT INTO public.teacher (id, full_name, subject) VALUES (%s, %s, %s)",
                            (row[0], row[1], row[2]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _add_record_to_subject_table(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount() - 2):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("INSERT INTO public.subject (name, id) VALUES (%s,%s)",
                            (row[0], row[1]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _change_record_from_timetable_monday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_monday_table.columnCount() - 2):
            try:
                row.append(self.timetable_monday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("UPDATE public.timetable SET day=%s, subject=%s, room=%s, start=%s,"
                            " teacher_id=%s, weektype=%s, id=%s WHERE id=%s",
                            (row[1], row[2], row[3], row[4], row[5], row[6], row[0], row[0]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _change_record_from_timetable_tuesday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_tuesday_table.columnCount() - 2):
            try:
                row.append(self.timetable_tuesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("UPDATE public.timetable SET day=%s, subject=%s, room=%s, start=%s,"
                            " teacher_id=%s, weektype=%s, id=%s WHERE id=%s",
                            (row[1], row[2], row[3], row[4], row[5], row[6], row[0], row[0]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _change_record_from_timetable_wednesday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_wednesday_table.columnCount() - 2):
            try:
                row.append(self.timetable_wednesday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("UPDATE public.timetable SET day=%s, subject=%s, room=%s, start=%s,"
                            " teacher_id=%s, weektype=%s, id=%s WHERE id=%s",
                            (row[1], row[2], row[3], row[4], row[5], row[6], row[0], row[0]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _change_record_from_timetable_thursday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_thursday_table.columnCount() - 2):
            try:
                row.append(self.timetable_thursday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("UPDATE public.timetable SET day=%s, subject=%s, room=%s, start=%s,"
                            " teacher_id=%s, weektype=%s, id=%s WHERE id=%s",
                            (row[1], row[2], row[3], row[4], row[5], row[6], row[0], row[0]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _change_record_from_timetable_friday_table(self, rowNum):
        row = list()
        for i in range(self.timetable_friday_table.columnCount() - 2):
            try:
                row.append(self.timetable_friday_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("UPDATE public.timetable SET day=%s, subject=%s, room=%s, start=%s,"
                            " teacher_id=%s, weektype=%s, id=%s WHERE id=%s",
                            (row[1], row[2], row[3], row[4], row[5], row[6], row[0], row[0]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _change_record_from_teacher_table(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount() - 2):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        # try:
        self.cursor.execute("UPDATE public.teacher SET full_name=%s, subject=%s,id=%s WHERE id=%s",
                            (row[1], row[2], row[0], row[0]))
        self.conn.commit()
        # except:
        #     QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _change_record_from_subject_table(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount() - 2):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE public.subject SET name=%s,id=%s WHERE id=%s", (row[0], row[1], row[1]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Ошибка", "Корректно заполните все поля")

    def _delete_record_from_timetable_monday_table(self, rowNum):
        row = self.timetable_monday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM public.timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_timetable_tuesday_table(self, rowNum):
        row = self.timetable_tuesday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM public.timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_timetable_wednesday_table(self, rowNum):
        row = self.timetable_wednesday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM public.timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_timetable_thursday_table(self, rowNum):
        row = self.timetable_thursday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM public.timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_timetable_friday_table(self, rowNum):
        row = self.timetable_friday_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM public.timetable WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_teacher_table(self, rowNum):
        row = self.teacher_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM public.teacher WHERE id=%s", [row])
        self.conn.commit()

    def _delete_record_from_subject_table(self, rowNum):
        row = self.subject_table.item(rowNum, 0).text()
        self.cursor.execute("DELETE FROM public.subject WHERE name=%s", [row])
        self.conn.commit()

    def _update_timetable(self):
        self._update_timetable_monday_table()
        self._update_timetable_tuesday_table()
        self._update_timetable_wednesday_table()
        self._update_timetable_thursday_table()
        self._update_timetable_friday_table()

    def _update_teacher(self):
        self._update_teacher_table()

    def _update_subject(self):
        self._update_subject_table()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
