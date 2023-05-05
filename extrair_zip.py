import zipfile
import PySimpleGUI as sg
import os

class Application:
    def extract_file(self):
        zip_file_path = os.path.abspath('Tux-unofficial 3.03.zip')
        extract_dir = 'C://Users//Hix_x//Desktop'
        
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extract('"tux unofficial 3.03"', path=extract_dir)

    def run(self):
        layout = [
            [sg.Button('Extrair Arquivo')],
        ]

        window = sg.Window('Extrair Arquivo', layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'Extrair Arquivo':
                self.extract_file()

        window.close()

if __name__ == '__main__':
    app = Application()
    app.run()
