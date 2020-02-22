import os
import pickle
import matplotlib.pyplot as plt

def Visualize(pkldata,title,xlablel,ylabel,xscale,yscale,legend,figsize,location):
    if not os.path.exists(location):        
        os.makedirs(location)
    visual=pickle.load(open(pkldata, 'rb'))
    #Note: I always save the x label in visual[0], and the results from different methods in next indices visual[1], visual[2], ...
    if figsize is not None:
        plt.figure(figsize=figsize)
    if legend is not None:
        for i in range(len(visual)-1):         
            plt.plot(visual[0],visual[i+1],label=legend[i]) 
    else:
        for i in range(len(visual)-1):         
            plt.plot(visual[0],visual[i+1]) 
    plt.title(title)
    plt.xlabel(xlablel)
    plt.ylabel(ylabel)
    if xscale is not None:
        plt.xscale(xscale)
    if yscale is not None:
        plt.yscale(yscale)
    if legend is not None:
        plt.legend(loc='lower right')
    plt.savefig(location+title+'.pdf')
	
if __name__ == '__main__':
	epoch_list = [1,2,3,4,5]
	loss_list_train = [1.09,0.92,0.85,0.80,0.62]
	loss_list_test = [1.03,0.99,0.95,0.91,0.72]
	pickle.dump( ([epoch_list, loss_list_train, loss_list_test]), open( 'pkldata.pkl', "wb" ) )        
	Visualize('pkldata.pkl','Loss History','epoch','Loss',None,'log',['train loss', 'test loss'],(15,7),'Figures/')
