from BLL.main import * 

def main(): # function of main program
    try:
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = MainWindow() # initializes main window but login will show first
        sys.exit(app.exec_())
    finally:
        db = Database()    # terminates database by instantiating and closing manually
        db.closeDatabase()

if __name__ == '__main__':
    main()
    
   
