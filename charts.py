import matplotlib.pyplot as plt

def method_to_rating_bar(Method):
    figure= plt.figure()
    axis=figure.add_subplot(1,1,1)
    axis.bar( range(len(Method)), 
    [m[1] for m in Method],
    tick_label=[m[0] for m in Method]
    )
    return figure