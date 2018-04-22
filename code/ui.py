import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPen, qRed, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel

import numpy as np

import utils

class ImageLabel(QLabel):
    def image(self):
        qImage = self.pixmap().toImage()

        img = np.zeros((qImage.height(), qImage.width()), dtype="int32")
        
        for j in range(qImage.height()):
            for i in range(qImage.width()):
                gray = qRed(qImage.pixel(i, j))
                img[j][i] = gray

        return img

    def setImage(self, img):
        qImage = QImage(img.shape[1], img.shape[0], QImage.Format_RGB888)

        for j in range(qImage.height()):
            for i in range(qImage.width()):
                gray = img[j][i]
                qImage.setPixelColor(i, j, QColor(gray, gray, gray))

        qPixmap = QPixmap(qImage)
        self.setPixmap(qPixmap)

class DigitLabel(ImageLabel):
    def __init__(self):
        super().__init__()

        self.x_old = None
        self.y_old = None

        self.factor = 10

        self.size = 200
        self.qPenSize = 10

        self.resetImage()

    def resetImage(self):
        image = np.zeros((self.size, self.size), dtype="int32")
        self.setImage(image)

    def mousePressEvent(self, event):
        self.x_old = event.x()
        self.y_old = event.y()

    def mouseMoveEvent(self, event):
        qPen = QPen(QColor(255, 255, 255), self.qPenSize, Qt.SolidLine)

        qPainter = QPainter()
        qPainter.begin(self.pixmap())
        qPainter.setPen(qPen)
        qPainter.drawLine(self.x_old, self.y_old, event.x(), event.y())
        qPainter.end()

        self.update()

        self.x_old = event.x()
        self.y_old = event.y()

def build(model):
    def classify(event=None):
        nonlocal digit_label, prepro_digit_labels, classif_labels, model

        img = digit_label.image()
        imgs = utils.preprocess(img)

        for i, img in enumerate(imgs):
            prepro_digit_labels[i].setImage(img)

        x = utils.format_x([imgs[-1]])
        y = model.predict(x)
        
        distr = y[0]
        claz = np.argmax(distr)

        for i, (class_label, proba_label) in enumerate(classif_labels):
            if i == claz:
                class_label.setStyleSheet("background-color: orange; padding: 2px 3px")
                proba_label.setStyleSheet("background-color: orange; padding: 2px 3px")
            else:
                class_label.setStyleSheet("background-color: white; padding: 2px 3px")
                proba_label.setStyleSheet("background-color: white; padding: 2px 3px")
                        
            percentage = round(distr[i]*100, 1)
            proba_label.setText(str(percentage)+"%")

    def reset():
        nonlocal digit_label

        digit_label.resetImage()

        classify()

    app = QApplication(sys.argv)

    digit_grid = QGridLayout()

    digit_label = DigitLabel()
    digit_label.mouseReleaseEvent = classify
    digit_grid.addWidget(digit_label, 0, 0, utils.NUM_PROCESS_STEPS, 1, Qt.AlignCenter)

    prepro_digit_labels = []
    
    for i in range(utils.NUM_PROCESS_STEPS):
        row = i

        prepro_digit_label = ImageLabel()
        digit_grid.addWidget(prepro_digit_label, row, 1, Qt.AlignCenter)

        prepro_digit_labels.append(prepro_digit_label)

    reset_button = QPushButton("Reset")
    reset_button.clicked.connect(reset)

    classif_grid = QGridLayout()

    classif_labels = []

    for i in range(utils.NUM_CLASSES):
        class_label = QLabel(str(i))
        class_label.setStyleSheet("padding: 2px 4px")
        classif_grid.addWidget(class_label, i, 0, Qt.AlignCenter)
        
        proba_label = QLabel()
        classif_grid.addWidget(proba_label, i, 1, Qt.AlignCenter)

        classif_labels.append([class_label, proba_label])

    reset()

    grid = QGridLayout()
    grid.addLayout(digit_grid, 0, 0)
    grid.addWidget(reset_button, 1, 0)
    grid.addLayout(classif_grid, 2, 0)

    w = QWidget()
    w.setWindowTitle("Digit classifier")
    w.setLayout(grid)
    w.show()

    sys.exit(app.exec_())