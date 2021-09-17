import matplotlib.pyplot as plt


class Pie_Plot_Noise():
    @staticmethod
    def create_plot(noise, identified):
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Ruído', 'Tarefas identificadas'
        sizes = [noise, identified]
        explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
        colors = ['IndianRed','SkyBlue']


        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=False, startangle=90, colors=colors)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        # plotting legend
        ax1.legend()
        fig1.savefig("figures/" + "cir_noise" + ".pdf", format="pdf")
        #plt.show()


if __name__ == '__main__':
    Pie_Plot_Noise.create_plot(noise=None, identified=None)
