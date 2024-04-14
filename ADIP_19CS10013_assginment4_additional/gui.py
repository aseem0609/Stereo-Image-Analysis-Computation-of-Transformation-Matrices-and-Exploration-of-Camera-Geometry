import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class ImageCorrespondenceSelector:
    def __init__(self, master):
        self.master = master
        self.master.title("Select Corresponding Points")

        self.fig, self.axs = plt.subplots(1, 2)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.points = [[], []]  # Store points for image 1 and image 2
        self.images = [None, None]
        self.load_buttons = [None, None]
        
        for i in range(2):
            self.load_buttons[i] = tk.Button(master, text=f"Load Image {i+1}", command=lambda i=i: self.load_image(i))
            self.load_buttons[i].pack(side=tk.LEFT)
            self.axs[i].set_title(f"Image {i+1}")
        
        self.canvas.mpl_connect('button_press_event', self.onclick)

    def load_image(self, idx):
        file_path = filedialog.askopenfilename()
        image = plt.imread(file_path)
        self.images[idx] = image
        self.axs[idx].imshow(image)
        self.fig.canvas.draw_idle()

    def onclick(self, event):
        if event.inaxes in self.axs:
            idx = self.axs.tolist().index(event.inaxes)
            self.points[idx].append((event.xdata, event.ydata))
            event.inaxes.plot(event.xdata, event.ydata, 'ro')
            self.fig.canvas.draw_idle()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCorrespondenceSelector(root)
    root.mainloop()
