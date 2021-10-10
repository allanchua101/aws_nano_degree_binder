def days_until_launch(current_day, launch_day):
    """"Returns the days left before launch.
    
    current_day (int) - current day in integer
    launch_day (int) - launch day in integer
    """
    output = launch_day - current_day

    if output <= 0:
      return 0
    
    return output
