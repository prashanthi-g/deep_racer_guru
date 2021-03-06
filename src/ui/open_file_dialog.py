import tkinter as tk
from src.ui.dialog import Dialog
from src.log.log import Log
import os


class OpenFileDialog(Dialog):

    def body(self, master):
        model_names = []
        model_files = {}

        for f in os.listdir(os.curdir):
            if f.endswith(".meta"):
                log = Log()
                log.load_meta(f)

                if log.log_meta.world_name == self.parent.current_track.world_name:
                    model_name = log.log_meta.model_name
                    model_names.append(model_name)
                    model_files[model_name] = f

        row = 0

        for model_name in sorted(model_names):
            f = model_files[model_name]

            log = Log()
            log.load_meta(f)

            callback = lambda file_name=f: self.callback_open_file(file_name)

            episode_stats = log.log_meta.episode_stats

            progress_percent = str(round(log.log_meta.episode_stats.average_percent_complete)) + " %"
            success_percent = str(round(episode_stats.success_count / episode_stats.episode_count * 100)) + " %"

            self.place_in_grid(row, 0, tk.Button(master, text=log.log_meta.model_name, command=callback))
            self.place_in_grid(row, 1, tk.Label(master, text=log.log_meta.race_type))
            self.place_in_grid(row, 2, tk.Label(master, text=log.log_meta.job_type))
            self.place_in_grid(row, 3, tk.Label(master, text=log.log_meta.episode_stats.episode_count))
            self.place_in_grid(row, 4, tk.Label(master, text=log.log_meta.episode_stats.best_steps))
            self.place_in_grid(row, 5, tk.Label(master, text=log.log_meta.episode_stats.average_steps))
            self.place_in_grid(row, 6, tk.Label(master, text=progress_percent))
            self.place_in_grid(row, 7, tk.Label(master, text=success_percent))


            #

            row += 1


    def buttonbox(self):
        box = tk.Frame(self)

        tk.Button(box, text="Cancel", width=10, command=self.cancel).pack()

        self.bind("<Return>", self.cancel)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def apply(self):
        pass

    def validate(self):
        return True

    def place_in_grid(self, row, column, widget):
        widget.grid(row=row, column=column, sticky=tk.W, padx=10, pady=5)

    def callback_open_file(self, file_name):
        self.cancel()
        self.parent.callback_open_this_file(file_name)


