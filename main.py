import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk
import rubickMethod as rubik
import blockMethod as block
from PIL import Image


class MainApplication:
    def __init__(self, app):
        self.app = app
        self.app.geometry('%sx%s' % (int(self.app.winfo_screenwidth() / 2.5), int(app.winfo_screenheight() / 2.5)))
        self.app.resizable(width=False, height=False)
        self.listFilenames = []
        self.listFirstKeyFilenames = []
        self.listSecondKeyFilenames = []
        self.UsingFunc = {'Блочное': [block.block_encrypt_image, block.block_decrypt_image], 'Рубик': [rubik.rubik_encrypt_image, rubik.rubik_decrypt_image]}

        self.choose_label_text = tk.StringVar()
        self.choose_label_text.set("Выберите изображение для шифровки:")
        self.encrypt_text = tk.StringVar()
        self.encrypt_text.set("Зашифровать")

        self.fist_key_label_text = tk.StringVar()
        self.fist_key_label_text.set("Выберите путь сохранения ключа первого метода:")

        self.second_key_label_text = tk.StringVar()
        self.second_key_label_text.set("Выберите путь сохранения ключа второго метода:")

        self.first_method_label_text = tk.StringVar()
        self.first_method_label_text.set("Выберите первый способ шифрования:")

        self.second_method_label_text = tk.StringVar()
        self.second_method_label_text.set("Выберите второй способ шифрования:")

        self.app.title("scramblingElistratov")

        # Mode
        self.selection_value = tk.IntVar()
        self.selection_value.set(1)
        self.mode_label = tk.Label(self.app, text="Выберите режим шифрования:", font=('Helvetica', 9))
        self.mode_radio_e = tk.Radiobutton(self.app, text="Шифрование", variable=self.selection_value, value=1,
                                           command=self.selection)
        self.mode_radio_d = tk.Radiobutton(self.app, text="Дешифрование", variable=self.selection_value, value=2,
                                           command=self.selection)

        self.selection_dimension = tk.IntVar()
        self.selection_dimension.set(1)
        self.mode_label_dimension = tk.Label(self.app, text="Выберите режим обработки:", font=('Helvetica', 9))
        self.mode_radio_once = tk.Radiobutton(self.app, text="Одиночное", variable=self.selection_dimension, value=1,
                                           command=self.selection)
        self.mode_radio_double = tk.Radiobutton(self.app, text="Двойное", variable=self.selection_dimension, value=2,
                                           command=self.selection)

        # Способ
        self.first_method_label = tk.Label(self.app, textvariable=self.first_method_label_text, font=('Helvetica', 9))
        self.second_method_label = tk.Label(self.app, textvariable=self.second_method_label_text, font=('Helvetica', 9))
        self.encryption_methods = ('Блочное', 'Рубик')
        self.selected_method = tk.StringVar()
        self.selected_method_second = tk.StringVar()

        self.method_combobox = ttk.Combobox(self.app, textvariable=self.selected_method, state='readonly')
        self.method_combobox['values'] = self.encryption_methods
        self.method_combobox.current(0)

        self.method_combobox_second = ttk.Combobox(self.app, textvariable=self.selected_method_second, state='readonly')
        self.method_combobox_second['values'] = self.encryption_methods
        self.method_combobox_second.current(0)

        # Выбор изображения
        self.choose_label = tk.Label(self.app, textvariable=self.choose_label_text, font=('Helvetica', 10))
        self.choose_entry = tk.Entry(self.app)
        self.choose_entry.config(state=tk.DISABLED)
        self.add_button = tk.Button(self.app, text="Выбрать изображение", command=self.chooseImg)

        # Папка вывода
        self.output_label = tk.Label(self.app, text="Выберите путь сохранения изображения", font=('Helvetica', 10))
        self.output_entry = tk.Entry(self.app)
        self.output_entry.config(state=tk.DISABLED)
        self.output_button = tk.Button(self.app, text="Выберите папку",
                                       command=lambda: self.chooseDestination(self.output_entry))

        # Первый ключ
        self.first_key_label = tk.Label(self.app, textvariable=self.fist_key_label_text, font=('Helvetica', 10))
        self.first_key_entry = tk.Entry(self.app)
        self.first_key_entry.config(state=tk.DISABLED)
        self.first_key_output_button_file = tk.Button(self.app, text="Выберите текстовый документ",
                                                 command=self.chooseKeyFirstFile)

        self.first_key_output_button_folder = tk.Button(self.app, text="Выберите папку",
                                                      command=lambda: self.chooseKeyFirstFolder(self.first_key_entry))

        # Второй ключ
        self.second_key_label = tk.Label(self.app, textvariable=self.second_key_label_text, font=('Helvetica', 10))
        self.second_key_entry = tk.Entry(self.app)
        self.second_key_entry.config(state=tk.DISABLED)
        self.second_key_output_button_file = tk.Button(self.app, text="Выберите текстовый документ",
                                                 command=self.chooseKeySecondFile)
        self.second_key_output_button_folder = tk.Button(self.app, text="Выберите папку",
                                                       command=lambda: self.chooseKeySecondFolder(self.second_key_entry))


        # Encrypt Button
        self.encrypt_button = tk.Button(self.app, textvariable=self.encrypt_text, font=('Helvetica', 9), command=self.encryptButton)

        # Grid
        self.app.grid_columnconfigure(3, weight=1)
        self.app.grid_rowconfigure(11, weight=1)

        self.mode_label.grid(row=0, column=0, padx=(8, 0), pady=(10, 5), sticky='wn')
        self.mode_radio_e.grid(row=0, column=1, padx=(4, 0), pady=(10, 0), sticky='wn')
        self.mode_radio_d.grid(row=0, column=2, padx=(4, 0), pady=(10, 0), sticky='wn')

        self.mode_label_dimension.grid(row=1, column=0, padx=(8, 0), pady=(10, 5), sticky='wn')
        self.mode_radio_once.grid(row=1, column=1, padx=(4, 0), pady=(10, 0), sticky='wn')
        self.mode_radio_double.grid(row=1, column=2, padx=(4, 0), pady=(10, 0), sticky='wn')

        self.first_method_label.grid(row=2, column=0, padx=(8, 0), pady=(10, 5), sticky='wn', columnspan=3, rowspan=2)
        self.method_combobox.grid(row=2, column=2, padx=(8, 0), pady=(10, 5), sticky='wn', columnspan=1)

        self.choose_label.grid(row=4, column=0, padx=(8, 0), pady=(5, 5), sticky='wn', columnspan=3)
        self.choose_entry.grid(row=5, column=0, sticky='wens', padx=(10, 5), pady=(0, 0), columnspan=3, rowspan=1)
        self.add_button.grid(row=5, column=3, sticky='wn', padx=(5, 0))

        self.first_key_label.grid(row=6, column=0, padx=(8, 0), pady=(5, 5), sticky='wn', columnspan=3)
        self.first_key_entry.grid(row=7, column=0, sticky='wens', padx=(10, 5), pady=(5, 5), columnspan=3)
        self.first_key_output_button_folder.grid(row=7, column=3, sticky='wn', padx=(5, 10))

        self.output_label.grid(row=10, column=0, padx=(8, 0), pady=(5, 0), sticky='wn', columnspan=3)
        self.output_entry.grid(row=11, column=0, sticky='wen', padx=(10, 5), pady=(5, 5), columnspan=3)
        self.output_button.grid(row=11, column=3, sticky='wn', padx=(5, 10))
        #
        # self.progress_label.grid(row=18, column=0, sticky='swn', padx=(7, 0), pady=(20, 10), columnspan=3)
        #
        self.encrypt_button.grid(row=12, column=0, sticky='senw', padx=(10, 10), pady=(20, 10))

    def selection(self):
        if self.selection_value.get() == 1:
            self.choose_label_text.set("Выберите изображение для шифрации")
            self.encrypt_text.set("Зашифровать")
            self.fist_key_label_text.set("Выберите путь сохранения ключа первого метода:")
            self.second_key_label_text.set("Выберите путь сохранения ключа второго метода:")
            self.first_method_label_text.set("Выберите первый способ шифрования:")
            self.second_method_label_text.set("Выберите второй способ шифрования:")

            self.first_key_output_button_file.grid_forget()
            self.first_key_output_button_folder.grid(row=7, column=3, sticky='wn', padx=(5, 10))
            self.second_key_output_button_file.grid_forget()


        else:
            self.choose_label_text.set("Выберите изображение для дешифрации")
            self.encrypt_text.set("Расшифровать")
            self.fist_key_label_text.set("Выберите путь использования ключа первого метода:")
            self.second_key_label_text.set("Выберите путь использования ключа второго метода:")
            self.first_method_label_text.set("Выберите первый способ дешифрования:")
            self.second_method_label_text.set("Выберите второй способ дешифрования:")

            self.first_key_output_button_file.grid(row=7, column=3, sticky='wn', padx=(5, 10))
            self.first_key_output_button_folder.grid_forget()
            self.second_key_output_button_folder.grid_forget()

        if self.selection_dimension.get() == 1:
            self.method_combobox_second.grid_forget()
            self.second_method_label.grid_forget()

            self.second_key_label.grid_forget()
            self.second_key_entry.grid_forget()

            self.second_key_output_button_file.grid_forget()
            self.second_key_output_button_folder.grid_forget()

        else:
            self.second_method_label.grid(row=3, column=0, padx=(8, 0), pady=(10, 5), sticky='wn', columnspan=3,
                                         rowspan=2)
            self.method_combobox_second.grid(row=3, column=2, padx=(8, 0), pady=(10, 5), sticky='wn', columnspan=1)

            self.second_key_label.grid(row=8, column=0, padx=(8, 0), pady=(5, 5), sticky='wn', columnspan=3)
            self.second_key_entry.grid(row=9, column=0, sticky='wen', padx=(10, 5), pady=(5, 5), columnspan=3)
            if self.selection_value.get() == 1:
                self.second_key_output_button_folder.grid(row=9, column=3, sticky='wn', padx=(5, 10))
            else:
                self.second_key_output_button_file.grid(row=9, column=3, sticky='wn', padx=(5, 10))

    def chooseImg(self):
        filename = fd.askopenfilenames(title='Выберите изображение')
        for i in filename:
            self.listFilenames.clear()
            self.listFilenames.append(i)
            self.choose_entry.config(state=tk.NORMAL)
            self.choose_entry.delete(0, tk.END)
            self.choose_entry.insert(tk.INSERT, i+'\n')
            self.choose_entry.config(state=tk.DISABLED)

    def chooseKeyFirstFolder(self, target_entry):
        directory = fd.askdirectory(title="Выберите папку")
        if directory:
            target_entry.config(state=tk.NORMAL)
            target_entry.delete(0, tk.END)
            target_entry.insert(0, directory)
            target_entry.config(state=tk.DISABLED)

    def chooseKeySecondFolder(self, target_entry):
        directory = fd.askdirectory(title="Выберите папку")
        if directory:
            target_entry.config(state=tk.NORMAL)
            target_entry.delete(0, tk.END)
            target_entry.insert(0, directory)
            target_entry.config(state=tk.DISABLED)

    def chooseKeyFirstFile(self):
        filename = fd.askopenfilenames(title='Выберите текстовый документ с ключом')
        for i in filename:
            self.listFirstKeyFilenames.clear()
            self.listFirstKeyFilenames.append(i)
            self.first_key_entry.config(state=tk.NORMAL)
            self.first_key_entry.delete(0, tk.END)
            self.first_key_entry.insert(tk.INSERT, i+'\n')
            self.first_key_entry.config(state=tk.DISABLED)

    def chooseKeySecondFile(self):
        filename = fd.askopenfilenames(title='Выберите текстовый документ с ключом')
        for i in filename:
            self.listSecondKeyFilenames.clear()
            self.listSecondKeyFilenames.append(i)
            self.second_key_entry.config(state=tk.NORMAL)
            self.second_key_entry.delete(0, tk.END)
            self.second_key_entry.insert(tk.INSERT, i+'\n')
            self.second_key_entry.config(state=tk.DISABLED)

    def chooseDestination(self, target_entry):
        directory = fd.askdirectory(title="Выберите папку")
        if directory:
            target_entry.config(state=tk.NORMAL)
            target_entry.delete(0, tk.END)
            target_entry.insert(0, directory)
            target_entry.config(state=tk.DISABLED)

    # Получить разрешение картинки
    def get_image_size(self, image):
        x, y = Image.open(image).size
        return x

    # Получить все делители разрешения картинки
    def get_divisors(self, num):
        result = {1, num}
        for divisor in range(2, num // 2 + 1):
            if num % divisor == 0:
                result.add(divisor)
        return sorted(result)

    # Кнопка после которой происходит процесс шифрования/дешифрования
    def encryptButton(self):
        if self.selection_dimension.get() == 1:
            self.UsingFunc[self.method_combobox.get()][self.selection_value.get() - 1](self.listFilenames[0], self.get_divisors(self.get_image_size(self.listFilenames[0]))[1], 1, self.first_key_entry.get().replace("\n", ""), f"{self.output_entry.get()}/output.png")
        else:
            if self.selection_value.get() == 1:
                self.UsingFunc[self.method_combobox.get()][self.selection_value.get() - 1](self.listFilenames[0], self.get_divisors(self.get_image_size(self.listFilenames[0]))[1], 1, self.first_key_entry.get().replace("\n", ""), f"{self.output_entry.get()}/temp_image.png")
                self.UsingFunc[self.method_combobox.get()][self.selection_value.get() - 1](f"{self.output_entry.get()}/temp_image.png", self.get_divisors(self.get_image_size(self.listFilenames[0]))[1], 2, self.second_key_entry.get().replace("\n", ""),f"{self.output_entry.get()}/output.png")
            else:
                self.UsingFunc[self.method_combobox.get()][self.selection_value.get() - 1](self.listFilenames[0], self.get_divisors(self.get_image_size(self.listFilenames[0]))[1], 2, self.second_key_entry.get().replace("\n", ""), f"{self.output_entry.get()}/temp_image.png")
                self.UsingFunc[self.method_combobox.get()][self.selection_value.get() - 1](f"{self.output_entry.get()}/temp_image.png", self.get_divisors(self.get_image_size(self.listFilenames[0]))[1], 1, self.first_key_entry.get().replace("\n", ""), f"{self.output_entry.get()}/output.png")


app = tk.Tk()
main_app = MainApplication(app)
app.mainloop()