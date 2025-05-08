import matplotlib.pyplot as plt
import calendar
from datetime import datetime


def calendargen(inputdates):
    # Define the year and month you want to plot
    year = 2024
    month = 7  # July

    # Create a figure with a specific size to make it big
    fig, ax = plt.subplots(figsize=(16, 8))

    # Load your preferred wallpaper image
    wallpaper_path = 'gradient.png'
    wallpaper = plt.imread(wallpaper_path)

    # Set the wallpaper as the figure background
    ax.imshow(wallpaper, aspect='auto', extent=[0, 7, -6, 1], zorder=-1,alpha=1)

    # Use Calendar to get an array of weeks for the month
    cal = calendar.monthcalendar(year, month)

    # Define blue tones for styling
    light_blue = '#ccddff'
    dark_blue = '#3344cc'
    header_color = '#002266'

    # Special events dates (YYYY, MM, DD)
    special_events = inputdates


    # Set font properties
    font_properties = {'family': 'sans-serif', 'weight': 'bold', 'size': 18}
    font_properties_highlight = {'family': 'sans-serif', 'weight': 'bold', 'size': 24}

    # Plot each day in the calendar
    for i, week in enumerate(cal):
        for j, day in enumerate(week):
            if day != 0:
                # Plot the day
                ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, fill=False, edgecolor='#afd7d9', linewidth=2))
                

                # Highlight the special event days and if not just normal day
                if (year, month, day) in special_events:
                    ax.add_patch(plt.Rectangle((j, -i-1), 1, 1, fill=True, color='#eab676', alpha=0.65))
                    ax.text(j+0.5, -i-1+0.5, str(day), ha='center', va='center', color='#afd7d9', **font_properties_highlight)
                else:
                    ax.text(j+0.5, -i-1+0.5, str(day), ha='center', va='center', color='#afd7d9', **font_properties)

    # Set the limits and labels
    ax.set_xlim(0, 7)
    ax.set_ylim(-len(cal)-1, 1)  # Adjusted to account for the removal of the weekday headers
    ax.set_aspect('equal')

    # Hide the axes
    ax.axis('off')

    # Add month and year at the top with increased font size
    ax.text(3.5, 0.7, f'{calendar.month_name[month]} {year}', ha='center', va='center', 
            fontsize=26, color='#afd7d9', weight='bold')

    # Save the figure
    plt.savefig('calendar_carwash.png', bbox_inches='tight', dpi=96)
    plt.close()
    