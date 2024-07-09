import cv2
import argparse



# Global list to store clicked coordinates
clicked_coords = []


def click_event(event, x, y, flags, param):
    """
    Callback function to handle mouse events.
    
    When the left mouse button is clicked, the coordinates (x, y) are added to
    the clicked_coords list and a small red circle is drawn at the click location
    on the image displayed in the window.
    
    Parameters:
        event: The type of mouse event.
        x: The x-coordinate of the mouse event.
        y: The y-coordinate of the mouse event.
        flags: Any relevant flags passed by OpenCV.
        param: Additional parameters (in this case, the image).
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        # Append the coordinates to the global list
        clicked_coords.append((x, y))
        print(f"Clicked coordinates: ({x}, {y})")
        
        # Draw a small red circle at the clicked location
        cv2.circle(param, (x, y), 3, (0, 0, 255), -1)
        
        # Update the image window with the new circle
        cv2.imshow("Image", param)

def interactive_mode_display(image_path):
    """
    Opens an image and allows the user to click on it to get pixel coordinates.
    
    This function opens an image from the given path, displays it in a window,
    and allows the user to click on the image to get the pixel coordinates. Each
    click will be marked with a small red circle. The function will continue
    running until the user presses the 'q' key to quit. After quitting, the
    function returns a list of all clicked coordinates.
    
    Parameters:
        image_path: Path to the image file.
    
    Returns:
        List of tuples containing the coordinates of each click.
    """
    # Read the image from the given path
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image. Check the path or format.")
        return

    # Display the image in a window
    cv2.imshow("Image", image)
    
    # Set the mouse callback function to handle click events
    cv2.setMouseCallback("Image", click_event, image)
    print("Click on the image to get the pixel coordinates. Press 'q' to quit.")

    while True:
        # Wait for the 'q' key to be pressed to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()
    
    # Return the list of clicked coordinates
    return clicked_coords


def display_location(image_path, location=(100, 50)):
    """
    Displays an image with a user-specified location marked by a red circle.

    Parameters:
    image_path (str): The path to the image file.
    location (tuple): Coordinates of the location to mark.
    """
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image. Check the path or format.")
        return
    
    height, width, _ = image.shape
    
    if not (0 <= location[0] < width and 0 <= location[1] < height):
        print("ERROR: The coordinates are outside the image.")
        return

    print(f"Location coordinates: {location}")

    cv2.circle(image, location, 5, (0, 0, 255), -1)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pixel to Coordinates Conversion")
    parser.add_argument('--image', type=str, default='images/default_image.jpg', help='Path to the input image')
    parser.add_argument('--interactive', action='store_true', help='Enable interactive mode to click and get coordinates')
    parser.add_argument('--location', type=int, nargs=2, default=[100, 50], help='Default location coordinates (x y)')
    args = parser.parse_args()

    if args.interactive:
        coords = interactive_mode_display(args.image)
        if coords:
            print("Final clicked coordinates: ", coords)
    else:
        display_location(args.image, tuple(args.location))