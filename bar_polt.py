import numpy as np
import matplotlib.pyplot as plt

def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


class BarPlot:
    @staticmethod
    def create_bar_plot(baseline_time, median_users):
        labels = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11']
        baseline_time = [float(x) for x in baseline_time]
        base_std = baseline_time
        median_std = median_users
        ind = np.arange(len(baseline_time))  # the x locations for the groups
        width = 0.35  # the width of the bars
        fig, ax = plt.subplots(figsize=(10,6))


        rects1 = ax.bar(ind - width/2, baseline_time, width, #yerr=base_std,
                        color='SkyBlue', label='baseline')
        rects2 = ax.bar(ind + width/2, median_users, width, #err=median_std,
                        color='IndianRed', label='mediana')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Tempo (s)')
        ax.set_title('Baseline e Mediana do tempo de execução das Tarefas')
        ax.set_xlabel('Tarefas')
        ax.set_xticks(ind)
        ax.set_xticklabels(labels)
        ax.legend()

        def autolabel(rects, xpos='center'):
            """
            Attach a text label above each bar in *rects*, displaying its height.

            *xpos* indicates which side to place the text w.r.t. the center of
            the bar. It can be one of the following {'center', 'right', 'left'}.
            """

            xpos = xpos.lower()  # normalize the case of the parameter
            ha = {'center': 'center', 'right': 'left', 'left': 'right'}
            offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                        '{}'.format(height),  ha=ha['center'], va='bottom')

        autolabel(rects1, "left")
        autolabel(rects2, "right")
        fig.tight_layout()
        plot_name = 'baseline_median_tasks'
        fig.savefig("figures/" + plot_name + ".pdf", format="pdf")
        plt.show()

if __name__ == '__main__':
    BarPlot.create_bar_plot(baseline_time=None , median_users=None)