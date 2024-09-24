import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_sigil(sigil_data):
    fig, ax = plt.subplots()
    
    # Set the plot limits
    ax.set_xlim(-sigil_data['max_size'], sigil_data['max_size'])
    ax.set_ylim(-sigil_data['max_size'], sigil_data['max_size'])
    
    # Draw each line in the sigil
    for line in sigil_data['lines']:
        start = line['start']
        end = line['end']
        width = line['width']
        velocity_x = line['velocity_x']
        velocity_y = line['velocity_y']
        
        # Draw the line
        ax.plot([start[0], end[0]], [start[1], end[1]], linewidth=width, color='red')
        
        # Draw the velocity arrow
        mid_point = [(start[0] + end[0]) / 2, (start[1] + end[1]) / 2]
        ax.arrow(mid_point[0], mid_point[1], velocity_x / 100, velocity_y / 100, head_width=0.5, head_length=0.5, fc='blue', ec='blue')
    
    # Draw circles at the start and end points of each line
    for line in sigil_data['lines']:
        start = line['start']
        end = line['end']
        
        ax.add_patch(patches.Circle(start, radius=0.5, color='black'))
        ax.add_patch(patches.Circle(end, radius=0.5, color='black'))
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def process_json_data(json_data):
    processed_data = {
        'max_size': json_data['max_size'],
        'lines': []
    }
    
    for line in json_data['lines']:
        processed_line = {
            'start': tuple(line['start']),
            'end': tuple(line['end']),
            'width': line['width'],
            'velocity_x': line['velocity_x'],
            'velocity_y': line['velocity_y']
        }
        processed_data['lines'].append(processed_line)
    
    return processed_data
    
def load_sigil_from_json(file_path):
    with open(file_path, 'r') as file:
        sigil_data = json.load(file)

    sigil_data = process_json_data(sigil_data)
    return sigil_data

if __name__ == "__main__":
    while True:
        sigil_file_path = input("Enter the path to the JSON file containing the sigil: ")
        try:
            sigil_data = load_sigil_from_json(sigil_file_path)
            break
        except FileNotFoundError:
            print("The file was not found. Please try again.")

    sigil_data = load_sigil_from_json(sigil_file_path)
    
    draw_sigil(sigil_data)