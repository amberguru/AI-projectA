#include <X11/Xlib.h>
#include <stdio.h>

int main() {
    Display *display = XOpenDisplay(NULL);
    if (!display) {
        fprintf(stderr, "Cannot open display\n");
        return 1;
    }

    int screen = DefaultScreen(display);
    Window root = RootWindow(display, screen);

    // Create a window covering the entire screen
    Window window = XCreateSimpleWindow(display, root, 0, 0,
                                        DisplayWidth(display, screen),
                                        DisplayHeight(display, screen),
                                        0, 0, 0);

    // Set window attributes to make it transparent
    XSelectInput(display, window, ButtonPressMask);
    XSetWindowBackground(display, window, 0);
    XClearWindow(display, window);
    XMapWindow(display, window);

    XEvent event;
    while (1) {
        XNextEvent(display, &event);
        if (event.type == ButtonPress) {
            printf("Mouse clicked at X: %d, Y: %d\n", event.xbutton.x, event.xbutton.y);
        }
    }

    XCloseDisplay(display);
    return 0;
}

