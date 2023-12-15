import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from datetime import datetime, timedelta
import openpyxl
import os
import psutil
import shutil

class TimeTrackerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Time Tracker App")

        self.projects = []
        self.create_folders = False

        # Configurar la fuente
        font = ('Helvetica', 12)

        self.label = tk.Label(master, text="Proyectos y Tiempo Registrado", font=('Helvetica', 14), pady=10)
        self.label.pack()

        self.listbox = tk.Listbox(master, height=10, width=50, font=font, selectbackground='#4CAF50')
        self.listbox.pack()

        self.start_button = tk.Button(master, text="Iniciar Proyecto", command=self.start_project, font=font, background='#4CAF50', foreground='white', padx=10, pady=5)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Detener Tiempo", command=self.stop_project, font=font, background='#4CAF50', foreground='white', padx=10, pady=5)
        self.stop_button.pack(pady=5)

        self.resume_button = tk.Button(master, text="Continuar Proyecto", command=self.resume_project, font=font, background='#4CAF50', foreground='white', padx=10, pady=5)
        self.resume_button.pack(pady=5)

        self.add_folder_button = tk.Button(master, text="Agregar Carpeta", command=self.add_folder_to_project, font=font, background='#4CAF50', foreground='white', padx=10, pady=5)
        self.add_folder_button.pack(pady=5)

        self.add_file_button = tk.Button(master, text="Agregar Archivo", command=self.add_file_to_project, font=font, background='#4CAF50', foreground='white', padx=10, pady=5)
        self.add_file_button.pack(pady=5)

        self.export_button = tk.Button(master, text="Exportar a Excel", command=self.export_to_excel, font=font, background='#4CAF50', foreground='white', padx=10, pady=5)
        self.export_button.pack(pady=5)

        self.folder_checkbox = tk.Checkbutton(master, text="Crear carpeta para cada proyecto", variable=tk.BooleanVar(), command=self.toggle_folder_creation, font=font)
        self.folder_checkbox.pack(pady=5)

        self.update_listbox()

    def toggle_folder_creation(self):
        self.create_folders = not self.create_folders

    def start_project(self):
        project_name = simpledialog.askstring("Nuevo Proyecto", "Nombre del Proyecto:")
        if project_name:
            start_time = datetime.now()
            project_data = {'name': project_name, 'start_time': start_time, 'status': 'active', 'folders': [], 'files': []}

            # Preguntar al usuario por la carpeta de destino si está habilitada la opción
            if self.create_folders:
                folder_path = self.ask_for_folder(project_name)
                if folder_path:
                    project_data['folders'].append(folder_path)
                    os.makedirs(folder_path, exist_ok=True)

            self.projects.append(project_data)
            self.update_listbox()

    def stop_project(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            project_index = selected_index[0]
            if self.projects[project_index]['status'] == 'active':
                end_time = datetime.now()
                elapsed_time = end_time - self.projects[project_index]['start_time']
                self.projects[project_index]['elapsed_time'] = elapsed_time
                self.projects[project_index]['end_time'] = end_time
                self.projects[project_index]['status'] = 'closed'
                self.update_listbox()

    def resume_project(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            project_index = selected_index[0]
            if self.projects[project_index]['status'] == 'closed':
                self.projects[project_index]['status'] = 'active'
                self.projects[project_index]['start_time'] = datetime.now()
                self.update_listbox()

    def add_folder_to_project(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            project_index = selected_index[0]
            folder_name = simpledialog.askstring("Nueva Carpeta", "Nombre de la Carpeta:")
            if folder_name:
                folder_path = os.path.join(os.getcwd(), f"Proyecto_{project_index + 1}_{self.projects[project_index]['name']}", folder_name)
                self.projects[project_index]['folders'].append(folder_path)
                os.makedirs(folder_path, exist_ok=True)
                self.update_listbox()

    def add_file_to_project(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            project_index = selected_index[0]
            file_path = filedialog.askopenfilename(title="Seleccionar Archivo para el Proyecto")
            if file_path:
                destination_path = os.path.join(os.getcwd(), f"Proyecto_{project_index + 1}_{self.projects[project_index]['name']}")
                shutil.copyfile(file_path, os.path.join(destination_path, os.path.basename(file_path)))
                self.projects[project_index]['files'].append(destination_path)
                self.update_listbox()

    def ask_for_folder(self, default_folder_name):
        # Si la opción de crear carpetas está habilitada y hay dispositivos extraíbles, mostrarlos
        if self.create_folders and psutil.disk_partitions(all=True):
            drive = simpledialog.askstring("Seleccionar Unidad Extraíble", "Seleccione el dispositivo extraíble para crear la carpeta:")
            if drive:
                return filedialog.askdirectory(title="Seleccionar carpeta de destino", initialdir=os.path.join(drive, default_folder_name))
        else:
            return filedialog.askdirectory(title="Seleccionar carpeta de destino")

    def export_to_excel(self):
        if not self.projects:
            messagebox.showinfo("Exportar a Excel", "No hay proyectos para exportar.")
            return

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Proyecto", "Hora de Inicio", "Tiempo Transcurrido", "Hora Final", "Ruta de la Carpeta", "Carpetas", "Archivos"])

        for project in self.projects:
            project_name = project['name']
            start_time = project['start_time'].strftime("%Y-%m-%d %H:%M:%S")
            elapsed_time = self.format_timedelta(project['elapsed_time']) if 'elapsed_time' in project else ""
            end_time = project['end_time'].strftime("%Y-%m-%d %H:%M:%S") if 'end_time' in project else ""
            folder_path = project.get('folders', [])
            files = project.get('files', [])
            ws.append([project_name, start_time, elapsed_time, end_time, folder_path, files])

        filename = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if filename:
            wb.save(filename)
            messagebox.showinfo("Exportar a Excel", f"Datos exportados exitosamente a {filename}")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for project in self.projects:
            status = project.get('status', '')
            if 'elapsed_time' in project:
                elapsed_time_str = self.format_timedelta(project['elapsed_time'])
                end_time_str = project['end_time'].strftime("%Y-%m-%d %H:%M:%S") if 'end_time' in project else ""
                folder_path_str = "\n".join(project.get('folders', []))
                files_str = "\n".join(project.get('files', []))
                self.listbox.insert(tk.END, f"{project['name']} - Estado: {status}, Tiempo: {elapsed_time_str}, Hora Final: {end_time_str}, Ruta de la Carpeta: {folder_path_str}, Archivos: {files_str}")
            else:
                self.listbox.insert(tk.END, f"{project['name']} - Estado: {status}")

    def format_timedelta(self, delta):
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours} horas, {minutes} minutos"

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTrackerApp(root)
    root.mainloop()
