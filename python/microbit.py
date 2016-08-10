import sys
sys.path.append('mb')
import Image

if sys.version_info[0] < 3:
    import display
    import button_a
    from display import sleep
    import accelerometer

