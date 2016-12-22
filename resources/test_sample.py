import numpy as np
def read_data(path, save=False, fname=None):
    """Read data to numpy array from path.

    Parameter
    ----------
    path : str. The path of the data file.
    save : boolean. Whether to save the data in npz format or just return it.
    fname : str. The file name to be used when save the data.

    Return
    -------
    data : numpy array.

    """
    data = np.genfromtxt(path)
    if save:
        np.save(fname, data)
    else:
        return data
	
if __name__ == '__main__':
    import sys
    import time

    # use time as file name
    time_str = []
    for t in time.localtime():
        time_str.append(str(t))
    s = '_'.join(time_str)
    n = len('19701101155930')
    s = s[:n+1]

    # if call from terminal, the data will be saved, with current time as file name.
    # if used as a module, then the data will not be saved.
    read_data(sys.argv[1], save=True, fname=s)
    #print 'execution done!'