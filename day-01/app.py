import sys

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QWidget,
    QLineEdit,
    QFormLayout,
    QHBoxLayout,
    QPushButton,
    QGridLayout,
    QMessageBox
)

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.form_elements_layout = QFormLayout()
        #Here we are creating the elements
        self.label_loan = QLabel("Principal Loan amount")
        self.edit_loan = QLineEdit()

        self.label_interest = QLabel("Yearly interest rate(%)")
        self.edit_interest = QLineEdit()

        self.label_period = QLabel("Period in months")
        self.edit_period = QLineEdit()

        self.label_payment = QLabel("Monthly payment")
        self.total_payment = QLineEdit()
        self.total_payment.setReadOnly(True)

        # adding form elements to the QFormLayout
        self.form_elements_layout.addRow(self.label_loan, self.edit_loan)
        self.form_elements_layout.addRow(self.label_interest, self.edit_interest)
        self.form_elements_layout.addRow(self.label_period, self.edit_period)
        self.form_elements_layout.addRow(self.label_payment, self.total_payment)

        #creating buttons
        self.button_calculate = QPushButton("Calculate")
        self.button_clear = QPushButton("Clear")

        # Add button actions
        self.button_calculate.clicked.connect(self.on_button_calculate_click)
        self.button_clear.clicked.connect(self.on_button_clear_click)

        #layout for the buttons
        self.action_button_layout = QHBoxLayout()
        self.action_button_layout.addWidget(self.button_calculate)
        self.action_button_layout.addWidget(self.button_clear)

        # The main layout to attach
        self.main_layout = QGridLayout()
        self.main_layout.addLayout(self.form_elements_layout, 0, 0)
        self.main_layout.addLayout(self.action_button_layout, 1, 0)
        


        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)
        self.setFixedSize(400, 200)

    def on_button_calculate_click(self):
        if self.edit_loan.text() == "" or self.edit_interest.text() == "" or self.edit_period.text() == "":
            QMessageBox.about(self, "Missing Values", "Principal loan amount, yearly interest rate, or period in months is empty")
        else:
            loan = float(self.edit_loan.text())
            interest = float(self.edit_interest.text())
            interest_per_month = interest / (12 * 100)
            period = float(self.edit_period.text())
            emi = (loan * interest_per_month * (1 + interest_per_month) ** period) / ( (1 + interest_per_month) ** period - 1)
            self.total_payment.setText(str(emi))
            print(self.total_payment)

    def on_button_clear_click(self):  
        self.edit_loan.setText(self.edit_loan.clear())
        self.edit_interest.setText(self.edit_interest.clear())
        self.edit_period.setText(self.edit_period.clear())
        self.total_payment.setText(self.total_payment.clear()) 
        self.total_payment.setText(str(round(emi,2))) 


def main(args):
    app = QApplication(args)

    application = Window()
    application.setWindowTitle("EMI Cal")
    application.show()
    
    # Kill the window instance once closed
    app.exec_()

if __name__ == '__main__':
    main(sys.argv)