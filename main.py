from PySide import QtCore, QtGui
from mainwindow import Ui_TabWidget
from corp import gutenberg_corp

class MainWindow(QtGui.QTabWidget):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_TabWidget()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.num_sent)
        self.ui.comboBox.currentIndexChanged.connect(self.raw_text)
        self.ui.radioButton.clicked.connect(self.unic_words)
        self.ui.radioButton_2.clicked.connect(self.words_chars)
        self.ui.radioButton_3.clicked.connect(self.colloc)
        self.ui.radioButton_4.clicked.connect(self.longest_sent)
        self.ui.radioButton_5.clicked.connect(self.longest_words)
        self.ui.pushButton_6.clicked.connect(self.common_cont)
        self.ui.pushButton_7.clicked.connect(self.concordance)
        self.ui.pushButton.clicked.connect(self.word_len)
        self.ui.pushButton_2.clicked.connect(self.sent_len)
        self.ui.pushButton_9.clicked.connect(self.find_errors)
        self.ui.pushButton_10.clicked.connect(self.compare_cont)
        self.ui.pushButton_11.clicked.connect(self.plot_len_words)
        self.ui.pushButton_12.clicked.connect(self.plot_len_sents)
        self.ui.pushButton_13.clicked.connect(self.plot_words)
        self.ui.pushButton_14.clicked.connect(self.disp_plot)

    def current_text(self):
        n=self.ui.comboBox.currentText()
        text=gutenberg_corp(n)
        self.stats(text)
        return text

    def stats(self,text):
        tmp=text.statistics()
        self.ui.label_8.setText(str(tmp['chars']))
        self.ui.label_9.setText(str(tmp['words']))
        self.ui.label_10.setText(str(tmp['sents']))
        self.ui.label_11.setText(str(tmp['vocab']))
        self.ui.label_12.setText(str(tmp['avg_word']))
        self.ui.label_13.setText(str(tmp['avg_sent']))
        self.ui.label_14.setText(str(tmp['avg_vocab']))

    def raw_text(self):
        tmp=self.current_text()
        self.ui.textBrowser_2.clear()
        self.ui.textBrowser_3.clear()
        self.ui.textBrowser_4.clear()
        self.ui.textBrowser_5.clear()
        self.ui.textBrowser_6.clear()
        self.ui.textBrowser_7.clear()
        self.ui.textBrowser.setText(tmp.raw)

    def num_sent(self):
        tmp=self.current_text()
        num=self.ui.spinBox_3.value()
        sent=str(tmp.ins_sent(num))
        self.ui.textBrowser_5.setText(sent)
        
    def unic_words(self):
        tmp=self.current_text()
        out=str(tmp.least_common())
        self.ui.textBrowser_2.setText(out)

    def words_chars(self):
        tmp=self.current_text()
        out=str(tmp.all_words())
        self.ui.textBrowser_2.setText(out)
        
    def colloc(self):
        tmp=self.current_text()
        out=str(tmp.collocations())
        self.ui.textBrowser_2.setText(out)

    def longest_sent(self):
        tmp=self.current_text()
        out=str(tmp.longest_sent())
        self.ui.textBrowser_2.setText(out)

    def longest_words(self):
        tmp=self.current_text()
        out=str(tmp.get_words_with_max_len())
        self.ui.textBrowser_2.setText(out)
        
    def common_cont(self):
        tmp=self.current_text()
        word=str(self.ui.lineEdit.text())
        out=str(tmp.similar(word))
        self.ui.textBrowser_3.setText(out)

    def concordance(self):
        tmp=self.current_text()
        word=str(self.ui.lineEdit.text())
        out=str(tmp.concordance(word))
        self.ui.textBrowser_3.setText(out)

    def word_count(self):
        tmp=self.current_text()
        word=str(self.ui.lineEdit.text())
        out=str(tmp.word_count(word))
        self.ui.textBrowser_3.setText(out)

    def word_len(self):
        tmp=self.current_text()
        lenword=(self.ui.spinBox.value())
        out=str(tmp.get_words_with_given_len(lenword))
        self.ui.textBrowser_4.setText(out)

    def sent_len(self):
        tmp=self.current_text()
        lensent=self.ui.spinBox_2.value()
        out=str(tmp.giving_len_sent(lensent))
        self.ui.textBrowser_4.setText(out)
        
    def find_errors(self):
        tmp=self.current_text()
        count=self.ui.spinBox_4.value()
        word=str(self.ui.lineEdit_2.text())
        out=str(tmp.similar_words(word,count))
        self.ui.textBrowser_6.setText(out)

    def compare_cont(self):
        tmp=self.current_text()
        word1=str(self.ui.lineEdit_3.text())
        word2=str(self.ui.lineEdit_4.text())
        out=str(tmp.common_contexts([word1,word2]))
        self.ui.textBrowser_7.setText(out)

    def plot_len_words(self):
        tmp=self.current_text()
        tmp.plot_len_words()
        
    def plot_len_sents(self):
        tmp=self.current_text()
        tmp.plot_len_sents()

    def plot_words(self):
        tmp=self.current_text()
        tmp.plot_words()

    def disp_plot(self):
        tmp=self.current_text()
        word1=str(self.ui.lineEdit_5.text())
        word2=str(self.ui.lineEdit_6.text())
        word3=str(self.ui.lineEdit_7.text())
        word4=str(self.ui.lineEdit_8.text())
        word5=str(self.ui.lineEdit_9.text())
        tmp.disp_plot([word1,word2,word3,word4,word5])   
                                                
if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
