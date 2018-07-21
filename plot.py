import numpy as np
import os
import matplotlib.pyplot as plt
#Defining Function
def boxplot_distance(data_to_plot):#an array of data for each month
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chartimages")
    #data_to_plot = [collectn_1,collectn_2,collectn_3,collectn_4]
    fig = plt.figure(0,figsize=(9,6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot,0,'',patch_artist='True')

    #changing colours
    for box in bp['boxes']:
            #outline color
            box.set( color='#7570b3', linewidth=2)
            #fill color
            box.set( facecolor = '#1b9e77')
    #whiskers
    for whisker in bp['whiskers']:
            whisker.set( color ='#7570b3', linewidth =2)

    for cap in bp['caps']:
            cap.set( color ='#7570b3', linewidth =2)

    for median in bp['medians']:
            median.set( color ='#b2df8a', linewidth=2)

    for flier in bp['fliers']:
            flier.set(marker ='o',color = '#e7298a', alpha= 0.5)
    ax.yaxis.grid(True)
    ax.set_title('Boxplots for average distances covered by owls')
    ax.set_xlabel('Month')
    ax.set_ylabel('Distance(km)')
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    #plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d KM'))
    fig.savefig(os.path.join(directory,'boxplot1.png'),bbox_inches='tight')
    print('done')
    #plt.show()

def boxplot_speed(data_to_plot):#an array of data for each month
    #data_to_plot = [collectn_1,collectn_2,collectn_3,collectn_4]
    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chartimages")
    fig = plt.figure(1,figsize=(9,6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot,0,'',patch_artist='True')

    #changing colours
    for box in bp['boxes']:
            #outline color
            box.set( color='#7570b3', linewidth=2)
            #fill color
            box.set( facecolor = '#1b9e77')
    #whiskers
    for whisker in bp['whiskers']:
            whisker.set( color ='#7570b3', linewidth =2)

    for cap in bp['caps']:
            cap.set( color ='#7570b3', linewidth =2)

    for median in bp['medians']:
            median.set( color ='#b2df8a', linewidth=2)

    for flier in bp['fliers']:
            flier.set(marker ='o',color = '#e7298a', alpha= 0.5)
    ax.yaxis.grid(True)
    ax.set_title('Boxplots for average speed for owls per month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Speed(mps)')
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    #plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d MPS'))
    fig.savefig(os.path.join(directory,'boxplot2.png'),bbox_inches='tight')
    print('done')
    #plt.show()

def graph_speed_distance(data_to_plot):
   #data_to_plot = {months,distance,speed}
   directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chartimages")
   plt.figure(2,figsize=(9,6))
   fig, ax1 = plt.subplots()
   ax1.plot(data_to_plot['months'],data_to_plot['averageDistances'], 'b-',label = 'distance')
   ax1.set_xlabel('Month')
   # Make the y-axis label, ticks and tick labels match the line color.
   ax1.set_ylabel('Distance(km)', color='b',)
   ax1.tick_params('y', colors='b')
   ax2 = ax1.twinx()
   ax2.plot(data_to_plot['months'],data_to_plot['averageSpeeds'], 'r--',label = 'speed')
   ax2.set_ylabel('Speed(mps)', color='r')
   ax2.tick_params('y', colors='r')
   #plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%d MPS'))
   plt.title("Average owl speed and distance covered per month")
   plt.legend()

   fig.savefig(os.path.join(directory,'dist_speed.png'),bbox_inches='tight')
   ##plt.show()

def graph_distance(data_to_plot):
   #data_to_plot = {months,distance_OwlID1,distance_OwlID2,distance_OwlID3,distance_OwlID4}
   directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chartimages")
   fig = plt.figure(5,figsize=(9,6))
   for owl in data_to_plot['owls']:
        plt.plot(data_to_plot['months'],owl['averageDistances'], label=owl['label'])
   plt.xlabel('Months')
   plt.ylabel('Distance(km)')
   plt.title("Average Distance covered per owl per month")
   plt.legend()
   fig.savefig(os.path.join(directory,'distancegraph.png'),bbox_inches='tight')
   # plt.show()

def graph_speed(data_to_plot):
   #data_to_plot = {months,speed_OwlID1,distance_OwlID2,distance_OwlID3,distance_OwlID4}
   directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chartimages")
   fig = plt.figure(6,figsize=(9,6))
   for owl in data_to_plot['owls']:
        plt.plot(data_to_plot['months'],owl['averageSpeeds'], label=owl['label'])
   plt.xlabel('Months')
   plt.ylabel('Speed(mps)')
   plt.title("Average speed covered per owl per month")
   plt.legend()
   fig.savefig(os.path.join(directory,'speedgraph.png'),bbox_inches='tight')
   #plt.show()
