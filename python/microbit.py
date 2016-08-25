import sys
sys.path.append('mb')
from Image import Image

if sys.version_info[0] < 3:
    import display
    import button_a
    from display import sleep
    from display import running_time
    import accelerometer

