import numpy as np

def save_traj(n, filename, task_name):
    if task_name == "scooping":
        x = np.linspace(0.1, 2, n)
        y = x*(x - 1)
    elif task_name == "flattening":
        x = np.linspace(0, 1, n)
        y = x
    elif task_name == "flipping":
        x = np.linspace(-0.4, 2, n)
        y = -x*(x - 1)
    elif task_name == "stirring":
        theta = np.linspace(np.pi/8, 5*np.pi/2, n)
        x = 4*np.cos(theta) - 2
        y = 4*np.sin(theta) - 2
    
    # Create the n x 3 position array
    positions = np.column_stack((x, y))
    
    # Save the array to a file
    np.save(filename, positions)
    print(f"Array saved to {filename}.npy")

save_traj(n=100, filename='../data/scooping', task_name="scooping")
save_traj(n=100, filename='../data/flattening', task_name="flattening")
save_traj(n=100, filename='../data/flipping', task_name="flipping")
save_traj(n=100, filename='../data/stirring', task_name="stirring")
