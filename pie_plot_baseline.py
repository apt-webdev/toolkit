import matplotlib.pyplot as plt


class Pie_Plot_Base():
    @staticmethod
    def create_plot(identified, baseline):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Tarefas identificadas', 'Tarefas classificadas'
        sizes = [identified, baseline]
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
        colors = ['IndianRed', 'SkyBlue']
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90, colors=colors)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        # plotting legend
        ax1.legend()
        fig1.savefig("figures/" + "cir_classi" + ".pdf", format="pdf")
        plt.show()


if __name__ == '__main__':
    Pie_Plot_Base.create_plot(identified=None, baseline= None)
