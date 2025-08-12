import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

tabview = customtkinter.CTkTabview(app)
tabview.pack(pady=20, padx=20, fill="both", expand=True)

tab_1 = tabview.add("Tab 1")
tab_2 = tabview.add("Tab 2")

label_tab1 = customtkinter.CTkLabel(tab_1, text="This text is left-aligned in Tab 1.", anchor="w")
label_tab1.pack(pady=10, padx=10, fill="x")

label_tab2 = customtkinter.CTkLabel(tab_2, text="This text is also left-aligned in Tab 2.", anchor="w")
label_tab2.pack(pady=10, padx=10, fill="x")

app.mainloop()
