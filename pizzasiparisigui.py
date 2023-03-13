import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Pizza Siparişi")

    # Pizza boyutu seçimi
    size_label = tk.Label(window, text="Pizza Boyutu Seçin:")
    size_label.pack()

    size_var = tk.StringVar(value="orta")
    size_radios = [("Küçük", "kucuk"), ("Orta", "orta"), ("Büyük", "buyuk")]
    for text, value in size_radios:
        size_radio = tk.Radiobutton(window, text=text, variable=size_var, value=value)
        size_radio.pack()

    # Pizza türü seçimi
    type_label = tk.Label(window, text="Pizza Türü Seçin:")
    type_label.pack()

    type_var = tk.StringVar(value="mozarella")
    type_radios = [("Mozarella", "mozarella"), ("Sucuklu", "sucuklu"), ("Karışık", "karisik")]
    for text, value in type_radios:
        type_radio = tk.Radiobutton(window, text=text, variable=type_var, value=value)
        type_radio.pack()

    # Sos seçimi
    sos_label = tk.Label(window, text="Sos Seçin:")
    sos_label.pack()

    sos_vars = {}
    sos_checkboxes = [("Zeytin Sos", "zeytin"), ("Mantar Sos", "mantar"), ("Keci Peyniri Sos", "keci"),
                      ("Et Sos", "et"), ("Soğan Sos", "sogan"), ("Mısır Sos", "misir")]
    for text, value in sos_checkboxes:
        sos_var = tk.BooleanVar(value=False)
        sos_checkbox = tk.Checkbutton(window, text=text, variable=sos_var)
        sos_vars[value] = sos_var
        sos_checkbox.pack()

    # Sipariş onaylama
    def place_order():
        selected_size = size_var.get()
        selected_type = type_var.get()
        selected_sos = [sos for sos, var in sos_vars.items() if var.get()]
        order_str = f"Boyut: {selected_size}\nTür: {selected_type}\nSoslar: {', '.join(selected_sos)}"

        order_window = tk.Toplevel(window)
        order_window.title("Sipariş Detayları")
        order_label = tk.Label(order_window, text=order_str)
        order_label.pack()

    order_button = tk.Button(window, text="Sipariş Ver", command=place_order)
    order_button.pack()

    window.mainloop()

if __name__ == '__main__':
    main()
