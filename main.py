from pytube import YouTube
from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class YouTubeDownloader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('YT-VAD By Matuco19')
        self.setGeometry(200, 200, 400, 200)
        
        layout = QtWidgets.QVBoxLayout()
        
        self.url_label = QtWidgets.QLabel('Put your URL:')
        self.url_input = QtWidgets.QLineEdit(self)
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        
        self.media_type_label = QtWidgets.QLabel('Video or audio (video/audio):')
        self.media_type_combo = QtWidgets.QComboBox(self)
        self.media_type_combo.addItems(['audio', 'video'])
        layout.addWidget(self.media_type_label)
        layout.addWidget(self.media_type_combo)
        
        self.download_button = QtWidgets.QPushButton('Download', self)
        self.download_button.clicked.connect(self.download_media)
        layout.addWidget(self.download_button)
        
        self.message_box = QtWidgets.QTextEdit(self)
        self.message_box.setReadOnly(True)
        layout.addWidget(self.message_box)
        
        self.setLayout(layout)

    def download_media(self):
        url = self.url_input.text()
        media_type = self.media_type_combo.currentText()
        output_path = 'downloads'
        try:     
            yt = YouTube(url)

            if media_type == 'audio':
                media_stream = yt.streams.filter(only_audio=True).first()
            elif media_type == 'video':
                media_stream = yt.streams.filter(only_video=True).first()
            else:
                self.message_box.append("Not supported format, using audio type.")
                media_stream = yt.streams.filter(only_audio=True).first()
                return
            
            self.message_box.append(f"Downloading {media_type}: {yt.title}")
            media_stream.download(output_path)
            self.message_box.append("Finished Download!")
            
        except Exception as e:
            self.message_box.append(f"Shit! There is an error: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    downloader = YouTubeDownloader()
    downloader.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
