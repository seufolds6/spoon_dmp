import numpy as np

def save_traj(n, filename, task_name):
    if task_name == "scooping":
        x = np.linspace(0.1, 2, n)
        y = x*(x - 1)
    elif task_name == "flattening":
        t = np.linspace(0, 1, n)
        x = np.full(n, 0.5)
        y = 0.0 + t
    elif task_name == "flipping":
        theta = np.linspace(np.pi / 100, np.pi, n)
        x = 0.5 * np.cos(theta) + 0.5
        y = np.sin(theta)
    elif task_name == "stirring":
        theta = np.linspace(np.pi / 8, 3 * np.pi, n)
        x = np.cos(theta)
        y = np.sin(theta)
    
    # Create the n x 3 position array
    positions = np.column_stack((x, y))
    
    # Save the array to a file
    np.save(filename, positions)
    print(f"Array saved to {filename}.npy")

save_traj(n=100, filename='../data/scooping', task_name="scooping")
save_traj(n=100, filename='../data/flattening', task_name="flattening")
save_traj(n=100, filename='../data/flipping', task_name="flipping")
save_traj(n=100, filename='../data/stirring', task_name="stirring")