import matplotlib.pyplot as plt
import numpy


class TaskPlot():
    def create_plot(id_task, baseline_name, baseline_time, u1, u2, u3, u4):
        fig = plt.figure()  #figsize=(10,5)

        # line 1 points - baseline
        xb = range(0, 5)

        #yb=[24,24,24,24,24]
        #baseline = [24,39,46,60,35,59,7,14,73,43,42]
        baseline = baseline_time[id_task]
        print(baseline)
        plt.axhline(y=int(baseline), linestyle="--", color="darkslategrey", lw=2, label='baseline')

        # line 1 points - Angela
        y1 = u1
        x1 = range(1, len(y1)+1)
        # plotting the line 1 points
        plt.plot(x1, y1, label="user1",marker='o', markerfacecolor='turquoise', color='green',  markersize=5, linewidth=2)

        # line 2 points - Armando+¨¨
        y2 = u2
        x2 = range(1, len(y2)+1)
        # plotting the line 2 points
        plt.plot(x2, y2, label="user2",marker='o', markerfacecolor='skyblue', color='blue',  markersize=5, linewidth=2)

        # line 2 points - Catarina
        y3 = u3
        x3 = range(1, len(y3)+1)
        # plotting the line 2 points
        plt.plot(x3, y3, label="user3", marker='o', markerfacecolor='lightcoral', color='brown',  markersize=5, linewidth=2)

        # line 2 points - Eva
        y4 = u4
        x4 = range(1, len(y4)+1)
        # plotting the line 2 points
        plt.plot(x4, y4, label="user4", marker='o', markerfacecolor='peachpuff', color='darkorange',  markersize=5, linewidth=2)
        # markerfacecolor='blue', color='skyblue'

        # setting x and y axis range
        #plt.xlim(0, 5)
        # naming the x axis
        plt.xlabel('Nº de execuções')
        # naming the y axis
        plt.ylabel('Tempo (s)')
        # giving a title to my graph
        plt.title(baseline_name[id_task])

        # show a legend on the plot
        fig_name = baseline_name[id_task]
        plt.legend()
        fig.savefig("figures/" + fig_name + ".pdf", format="pdf")

        #plt.show()

'''if __name__ == '__main__':
    # function to show the plot
    TaskPlot.create_plot()
    plt.show()'''