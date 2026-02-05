import sys
SEED = 1234
IMAGE_PATH = "images/"

def activate_seed():
    """Set the random SEED from command-line arguments or fall back to default value shown on top."""
    global SEED, DEBUG
    if (len(sys.argv)) > 1:
        SEED = sys.argv[1]